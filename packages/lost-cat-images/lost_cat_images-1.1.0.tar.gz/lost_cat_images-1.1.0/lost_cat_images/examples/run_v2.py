from datetime import datetime
import logging
import glob
import json
import re
import os
import sys

import cv2 as cv
import networkx as nx
import numpy as np
import pandas as pd

from dotenv import load_dotenv
from inspect import getmembers, isclass
from networkx.readwrite import json_graph
from lost_cat.utils.path_utils import get_filename, fast_scan
# inlcuded so they can be loaded into the handlers....
from lost_cat_office.parsers.pdf_parser import PDFParser
from lost_cat_images.parsers.image_parser import EXIFParser
from lost_cat_images.utils import (boxes, text, grids, grayscale, threshold,
                                   color_segmentation, denoise, run_rules,
                                   ellipse,
                                   NumpyArrayEncoder, json_numpy_obj_hook)
from lost_cat_images.utils.extract import extract_contours
from lost_cat_images.utils.image_templates import create_targets
from lost_cat_images.utils.utils_grids import extract_tables
from lost_cat_images.utils.utils_words import pivot_text

logger = logging.getLogger(__name__)
load_dotenv()


def get_files(uri: str, exts: list = [], regex: str = None):
    """Will return the immediate files in the specified folder"""
    if regex:
        regobj = re.compile(pattern=regex, flags=re.IGNORECASE)
    files = []
    uri_glob = os.path.join(uri, "*")
    for f in glob.glob(uri_glob):
        _, ext = os.path.splitext(f)
        if os.path.isdir(f):
            continue

        isregex = False
        isext = (ext.lower() in exts) if len(ext) > 0 else True
        if  m := regobj.match(f):
            isregex = True
        elif not regex:
            isregex = True

        logger.info("F: %s E: %s R: %s",f,isext, isregex)

        if isext and isregex:
            files.append(f)

    return files

def process_image(image: np.array, config: dict) -> dict:
    """Process the image based on the config provided"""

    image_return = np.array(image).copy()

    images = {}
    data = config.get('data',{})

    shape_data = []
    text_data = []
    word_data = {}
    mapping_data = {}
    ellipse_data = []
    graph_data = []
    grid_data = []
    table_data = []

    # flags
    isGray = False
    isBW = False
    has_text = False
    has_boxes = False
    hasGrids = False

    processes = config.get("process",[])

    if "segmentation" in processes:
        # segment the image
        config_sg = config.get("segemtation", {}).copy()
        data_sg = color_segmentation(image=image_return, config=config_sg)
        for img_label, img_data in data_sg.get('images',{}).items():
            if img_label == 'processed':
                image_return = img_data.copy()
                images['segment'] = image_return.copy()
            else:
                images[f'SG.{img_label}'] = img_data.copy()

    if "text" in processes:
        # get the text...
        image_return, text_data = extract_text(image, config, image_return,
                                               images, data)

        if text_data and len(text_data) > 0:
            word_data = pivot_text(words=text_data)
            logger.info("Pivot: T: %s -> %s WD: %s -> %s", type(text_data),
                        len(text_data), type(word_data), len(word_data))
            data['tx.words'] = word_data
            logger.info("Words: %s %s", type(word_data), len(word_data))
            has_text = True

    if "denoise" in processes:
        # blur the image
        config_dn = config.get("denoise", {}).copy()
        data_dn = denoise(image=image_return, config=config_dn)
        for img_label, img_data in data_dn.get('images',{}).items():
            if img_label == 'processed':
                image_return = img_data.copy()
                images['denoise'] = image_return.copy()
            else:
                images[f'DN.{img_label}'] = img_data.copy()
        data_dn = None

    if "grayscale" in processes:
        # convert to grayscale:
        config_gs = config.get("grayscale", {}).copy()
        data_gs = grayscale(image=image_return, config=config_gs)
        for img_label, img_data in data_gs.get('images',{}).items():
            if img_label == 'processed':
                image_gray = img_data.copy()
                images['gray'] = image_return.copy()
                isGray = True
            else:
                images[f'TT.{img_label}'] = img_data.copy()
        data_gs = None

    if "threshold" in processes and isGray is True:
        # now create a binary image...
        config_tt = config.get("threshold", {}).copy()
        data_tt = threshold(image=image_gray, config=config_tt)
        for img_label, img_data in data_tt.get('images',{}).items():
            if img_label == 'processed':
                image_bw = img_data.copy()
                images['bw'] = image_bw.copy()
                isBW = True
            else:
                images[f'TT.{img_label}'] = img_data.copy()
        data_tt = None

    if "contours" in processes and isBW is True:
        # fetch the contours for the images
        extract_imagecontours(config, images, data, image_bw, image)

    # find the targets
    if "boxes" in processes and isBW is True:
        shape_data, has_boxes = extract_boxes(image, config, images, data,
                                             image_bw)

    if "grids" in processes and has_boxes is True:
        ex_data = extract_grids(image, config, images, data, shape_data,
                                word_data)
        shape_data, mapping_data, graph_data, grid_data, table_data = ex_data

    if "tables" in processes and len(table_data) > 0:
        config_tb = config.get("tables", {}).copy()
        # add the extra data to the config
        config_tb['tables'] = table_data
        config_tb['graph'] = graph_data

        rule_data = []
        for f_obj in config_data.get("paths",{}).get("rules",[]):
            rulepath = get_filename(f_obj)
            if not os.path.exists(rulepath):
                logger.error("Missing Rule file %s", rulepath)
                continue

            # load the json into a rule
            with open(rulepath, 'r', encoding="utf-8") as fp:
                rule_set = json.load(fp=fp, object_hook=json_numpy_obj_hook)
                for rule in rule_set.get("tables", []):
                    rule_data.append(rule)

        config_tb['rules'] = rule_data
        logger.info("Found: Rules: %s", len(rule_set))

        data_tb = extract_tables(image=image_gray, config=config_tb)

        for img_label, img_data in data_tb.get('images',{}).items():
            images[f'tb.{img_label}'] = img_data.copy()

        # save the table_data
        for data_label, data_value in data_tb.get('data',{}).items():
            data[f'tb.{data_label}'] = data_value

        table_data = data_tb.get('data',{}).get("export")

    # "ellipse"
    if "ellipses" in processes and has_text is True:
        ellipse_data = extract_ellipses(image, config, images, data, text_data)

    # rules
    if "rules" in processes and has_boxes is True:
        extract_rules(image, config, images, data, shape_data, word_data,
                      mapping_data, ellipse_data, graph_data,
                      grid_data, table_data)

    return {
        'images': images,
        'data': data
    }

def extract_rules(image, config, images, data, shape_data, word_data,
                  mapping_data, ellipse_data, graph_data, grid_data,
                  table_data):
    config_rr = config.get("rules", {}).copy()
    config_rr['words'] = word_data
    config_rr['shapes'] = shape_data
    config_rr['mapping'] = mapping_data

    config_rr['graph'] = graph_data
    config_rr['tables'] = table_data
    config_rr['grids'] = grid_data
    config_rr['ellipses'] = ellipse_data
    config_rr['export'] = data.get("data", {}).get("tb.exports")

        # load the rules from the json files
    rule_data = []
    for f_obj in config_data.get("paths",{}).get("rules",[]):
        rulepath = get_filename(f_obj)
        if not os.path.exists(rulepath):
            logger.error("Missing Rule file %s", rulepath)
            continue

            # load the json into a rule
        with open(rulepath, 'r', encoding="utf-8") as fp:
            if 'data' not in config_data:
                config_data['data'] = {}
            rule_data.append(json.load(fp=fp, object_hook=json_numpy_obj_hook))

    config_rr['rules'] = rule_data
    data_rr = run_rules(image=image, config=config_rr)

    for img_label, img_data in data_rr.get('images',{}).items():
        images[f'rr.{img_label}'] = img_data.copy() if img_data else None

    for data_label, data_value in data_rr.get("data",{}).items():
        data[f'rr.{data_label}'] = data_value

def extract_ellipses(image, config, images, data, text_data):
    config_el = config.get("ellipse", {}).copy()
    config_el["image"] = image.copy()
    config_el['texts'] = text_data
    data_el = ellipse(image=image, config=config_el)

    for img_label, img_data in data_el.get('images',{}).items():
        images[f'el.{img_label}'] = img_data.copy()

    for data_label, data_value in data_el.get("data",{}).items():
        data[f'el.{data_label}'] = data_value

    ellipse_data = data_el.get("data", {}).get("ellipses", [])

    data_el = None
    return ellipse_data

def extract_grids(image, config, images, data, shape_data, word_data):
    config_gr = config.get("grids", {}).copy()
    config_gr['shapes'] = shape_data
    config_gr['texts'] = word_data
    data_gr = grids(image=image, config=config_gr)

    for img_label, img_data in data_gr.get('images',{}).items():
        images[f'gr.{img_label}'] = img_data.copy()

    for data_label, data_value in data_gr.get("data",{}).items():
        data[f'gr.{data_label}'] = data_value

    shape_data = None
    if len(data_gr.get('data', {}).get('shapes',[])) > 0:
        shape_data = data_gr.get('data', {}).get('shapes')

    # get the grid infomations
    grid_data = None
    if len(data_gr.get('data', {}).get('grids',[])) > 0:
        grid_data = data_gr.get('data', {}).get('grids')

    # tables
    table_data = None
    if len(data_gr.get('data', {}).get('tables',[])) > 0:
        table_data = data_gr.get('data', {}).get('tables')

        # mapping
    mapping_data = None
    if len(data_gr.get('data', {}).get('mapping',[])) > 0:
        mapping_data = data_gr.get('data', {}).get('mapping')

    # graph
    graph_data = None
    if len(data_gr.get('data', {}).get('graph',[])) > 0:
        graph_data = data_gr.get('data', {}).get('graph')

    data_gr = None
    return shape_data,mapping_data,graph_data,grid_data,table_data

def extract_boxes(image, config, images, data, image_bw):
    targets, offsets = create_targets(size=7, bleed=1)
    config_bb = config.get("boxes", {}).copy()
    config_bb["image"] = image.copy()
    config_bb["targets"] = targets
    config_bb["offsets"] = offsets
    data_bb = boxes(image=image_bw, config=config_bb)

    for img_label, img_data in data_bb.get('images',{}).items():
        images[f'bb.{img_label}'] = img_data.copy()

    for data_label, data_value in data_bb.get("data",{}).items():
        data[f'bb.{data_label}'] = data_value

    shape_data = []
    has_boxes = False
    if len(data_bb.get('data', {}).get('shapes')) > 0:
        shape_data = data_bb.get('data', {}).get('shapes')
        has_boxes = True

    data_bb = None
    return shape_data,has_boxes

def extract_imagecontours(config, images, data, image_bw, image):
    config_ct = config.get("contours", {}).copy()
    config_ct['image'] = image.copy()

    data_ct = extract_contours(image=image_bw, config=config_ct)

    for img_label, img_data in data_ct.get('images',{}).items():
        images[f'ct.{img_label}'] = img_data.copy()

    for data_label, data_value in data_ct.get("data",{}).items():
        data[f'ct.{data_label}'] = data_value

    if len(data_ct.get('data', {}).get('contours')) > 0:
        contour_data = data_ct.get('data', {}).get('shapes')
        hasContours = True

def extract_text(image, config, image_return, images, data):
    if text_data := data.get("tx.texts",[]):
            # use cache...
        logger.warning("TEXT: cache...")
    else:
            # refresh...
        logger.warning("TEXT: refresh...")
        config_tx = config.get("text", {}).copy()
        config_tx["image"] = image.copy()
        data_tx = text(image=image_return, config=config_tx)

        for img_label, img_data in data_tx.get('images',{}).items():
            if img_label == 'processed':
                image_return = img_data.copy()
            else:
                images[f'tx.{img_label}'] = img_data.copy()

        for data_label, data_value in data_tx.get("data",{}).items():
            data[f'tx.{data_label}'] = data_value

        text_data = data_tx.get('data', {}).get('texts')
    return image_return,text_data

def process_filelist(files: list, config:dict, handlers:dict, base_paths: list) -> dict:
    """"""
    try:
        dest_path = get_filename(file_dict=config.get("paths", []).get("destination", {}))
    except TypeError:
        dest_path = os.path.expandvars(os.path.join("data", "twseu"))
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    for fidx, f in enumerate(files):
        # put a stop gate in...
        if stop_at := int(config.get('count')):
            if 0 < stop_at <= fidx:
                break

        exts = list(handlers.keys())
        if '.png' not in exts:
            exts.append('.png')

        if not f.lower() not in exts:
            continue

        folder_path, filename = os.path.split(f)
        name, ext = os.path.splitext(filename)
        ext = ext.lower()

        if filename.lower() in config.get('paths', {}).get('ignore', []):
            logger.warning("Skiping %s", f)
            continue

        # get the folder path...
        prefix = ""
        for base_path in base_paths:
            if folder_path.startswith(base_path):
                prefix = '.'.join(folder_path[len(base_path)+1:len(f)].split(os.sep))
                if prefix is None or prefix == "":
                    prefix = os.path.basename(base_path)
                break

        if len(prefix) > 1:
            save_path = os.path.join(dest_path, prefix)
        else:
            save_path = dest_path

        if not os.path.exists(save_path):
            logger.info('Create: %s', save_path)
            os.makedirs(save_path)

        images = []
        if ext in handlers:
            # get the images from pdf
            logger.info("File[%s]: %s %s-> %s", fidx, f, ext, 'lost-cat')

            # a list of handlers and the oibject pointer
            try:
                obj = handlers.get(ext)[0](uri=f)
                if func := obj.avail_functions().get('screenshots'):
                    images = func(dpi=600)
            except Exception as ex:
                logger.error(ex)
                print(f'{fidx}: {f} => {ex}')
                continue

        elif ext in ['.png']:
            images.append(cv.imread(f))

        else:
            logger.info("SKIPPING: File[%s]: %s", fidx, f)
            continue

        logger.info("File[%s]: %s -> %s", fidx, f, len(images))

        for iidx, img in enumerate(images):
            # check for cache data....
            if 'data' in config:
                del config['data']

            for cache in config.get('caches',[]):
                cachename = os.path.join(save_path, f'{name}.{iidx}.{cache}.json')
                logging.info('Checking: %s', cachename)
                if os.path.exists(cachename):
                    with open(cachename, 'r', encoding="utf-8") as fp:
                        if 'data' not in config:
                            config['data'] = {}

                        config['data'][cache] = json.load(fp=fp, object_hook=json_numpy_obj_hook)
                        logger.info('\tloading: %s -> %s', cache, cachename)

            img =  np.array(img).copy()
            data = process_image(image=img, config=config)
            if "errors" in data:
                print("errors:")
                for err in data.get("errors",[]):
                    print(f"\t{err}")
                break

            for label, img_res in data.get("images",{}).items():
                if label.lower() in config.get('exports', {}).get('images',{}):
                    logger.info('Saving image %s %s %s', name, fidx, label)
                    cv.imwrite(os.path.join(save_path, f'{name}.{iidx}.{label}.png'), img_res)

            for label, data_val in data.get("data",{}).items():
                if label.lower() in config.get('exports', {}).get('data',{}):
                    if isinstance(data_val, dict) or isinstance(data_val, list):
                        logger.info('Data: %s %s %s %s %s', name, fidx, iidx, label, type(data_val))
                        try:
                            with open(os.path.join(save_path, f'{name}.{iidx}.{label}.json'), 'w', encoding="utf-8") as fp:
                                fp.write(json.dumps(data_val, indent=4, cls=NumpyArrayEncoder))
                        except Exception as ex:
                            logger.error("EX: %s: %s => %s", fidx, name, ex)
                    elif isinstance(data_val, nx.Graph):
                        with open(os.path.join(save_path, f'{name}.{iidx}.{label}.json'), 'w', encoding="utf-8") as fp:
                            fp.write(json.dumps(data_val, default=nx.node_link_data)) #json_graph.dumps(data_val))
                    elif isinstance(data_val, pd.DataFrame):
                        data_val.to_excel(os.path.join(save_path, f'{name}.{iidx}.{label}.xlsx'))

            for err in data.get("errors", []):
                logger.error("Notes: %s", err)

def consolidate_excel(path: str, excel_path: str) -> None:
    """Will scan the supplied folder for excel file matching the
    regex, and will then combine these files into a single
    dataframe and then export to excel

    parameters:
    -----------
    path: str
        the folder path to scan for .xlsx files
    excel_path: str
        the xlsx filename to export the data to
    """
    dataframes = {}

    for f in fast_scan(uri=path):
        name, ext = os.path.splitext(f.name)
        if ext.lower() == ".xlsx":
            parts = name.split('.')
            if len(parts) < 4:
                continue
            logger.info("Parts: %s", parts)

            # [basepath.].[filename.].[iidx].[src].[data]
            # load the dataframe...
            df = pd.read_excel(f.path).iloc[:,1:]
            parent_directory = os.path.dirname(f.path)
            parent_folder_name = os.path.basename(parent_directory)
            df['name'] = '.'.join(parts[:-3])
            df['iidx'] = parts[-3]
            df['scanner'] = parts[-2]
            df['parent_folder'] = parent_folder_name

            # check if there is a dataframe for the section
            if parts[-1] not in dataframes:
                dataframes[parts[-1]] = df.copy()
            else:
                # now to concat the data frame
                frames = [dataframes[parts[-1]], df]
                dataframes[parts[-1]] = pd.concat(frames)

    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        for label, df in dataframes.items():
            logger.info("DF: %s -> %s", label, df.shape)
            df.to_excel(writer, sheet_name=label)

def main(config: dict):
    """This will run a core sample of files"""
    logger.warning("Start: %s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    handlers = {}
    # map the parsers to the file extensions:
    for name, obj in getmembers(sys.modules[__name__]):
        if isclass(obj) and obj.__name__.endswith("Parser"):
            avail_config = obj.avail_config()
            for src_config in avail_config.get("source", []):
                if src_config.get("key", "") == "ext":
                    for ext in src_config.get("values", []):
                        if ext not in handlers:
                            handlers[ext] = []
                        handlers[ext].append(obj)
    logger.info("handers: %s", handlers)

    try:
        dest_path = get_filename(file_dict=config.get("paths", []).get("destination", {}))
    except TypeError:
        dest_path = os.path.expandvars(os.path.join("data", "twseu"))
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # get the file to scan...
    files = []
    base_paths = []
    for p in config.get("paths", []).get("sources", []):
        src_path = get_filename(p)
        base_paths.append(src_path)

        if config.get('paths',{}).get('flags',{}).get('subs', False):
            glob_path = os.path.join(src_path, *["**", "*"])
        else:
            glob_path = os.path.join(src_path, "*")
        logger.info("scanning: %s", glob_path)
        print(f"Scan: {glob_path}")
        files.extend(glob.glob(glob_path))

    # load the files
    process_filelist(files=files, config=config, handlers=handlers, base_paths=base_paths)

    # consolidate the outputs into a single file
    try:
        excel_path = get_filename(file_dict=config.get("paths", []).get("excel", {}))
    except TypeError:
        excel_path = os.path.expandvars(os.path.join(dest_path, "twseu_output.xlsx"))

    consolidate_excel(path=dest_path, excel_path=excel_path)
    logger.warning("End: %s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    import argparse

    nb_name = "EngImgV2"
    if not os.path.exists("logs"):
        os.mkdir("logs")

    _logname = "{}.{}".format(nb_name, datetime.now().strftime("%Y%m%d"))
    logpath = os.path.join("logs", f"{_logname}.log")
    if os.path.exists(logpath):
        os.remove(logpath)

    parser = argparse.ArgumentParser(
                        prog='TWS Extraction Util V1',
                        description='Scans a set of engineering diagram and will extract metadata',
                        epilog='for help please email support@thoughtswinsystems.com')

    parser.add_argument('--config', '-c',
                        dest='config_path',
                        help='sets the config path to use, otherwise uses default location.',
                        default=os.path.expandvars(os.path.join(".", *["config", "lci_config.json"])))

    parser.add_argument('-d', '--debug',
                        help="Print lots of debugging statements",
                        action="store_const", dest="loglevel", const=logging.DEBUG,
                        default=logging.WARNING)

    args = parser.parse_args()

    logging.basicConfig(filename=logpath, level=args.loglevel)

    if not os.path.exists("config"):
        os.mkdir("config")
    config_data = None

    if os.path.exists(args.config_path):
        # load the config
        with open(args.config_path, mode="r", encoding="utf-8") as fpointer:
            config_data = json.load(fpointer)

    if config_data is None:
        config_data = {
            "paths":{
                "sources":[
                    {
                        "root": '.',
                        "folders": ["data"]
                    }
                ],
                "ignore": [],
                "flags": {
                    "subs": False
                },
                "rules": [
                    {
                        "root": ".",
                        "folders": ["config"],
                        "name": "imgrules",
                        "ext": ".json"
                    }
                ]
            },
            "exports": {
                "data": [
                    "tx.raw",
                    "tx.texts",
                    "rr.detail",
                    "rr.ellipses"
                ],
                "images": [
                    "tx.markup",
                ]
            },
            "process":[
                "segmentation",
                "text",
                "grayscale",
                "threshold",
                "contours",
                "ellipses",
                "boxes",
                "grids",
                "tables",
                "rules"
            ],
            "caches":[
                "tx.texts"
            ],
            "segemtation":{
                "ranges": [
                    {"min":{"h": 20, "s": 0, "v": 200}, "max":{"h": 80, "s": 100, "v": 255}}
                ]
            },
            "denoise": {
                "mode": "bilateral",
                "diameter": 9,
                "sigmacolor": 75,
                "sigmaspace": 75
            },
            "grayscale": {
                "sourcetype": "BGR"
            },
            "contours": {
                "mode": 3,
                "method": 3
            },
            "ellipse": {
                "text_box_scale_ratio":1.1,
                "edge_detection_threshold":{
                    "threshold1":50,
                    "threshold2":150
                },
                "contours":{
                    "mode": 0,
                    "method": 2
                    },
                "filters":{
                    "min_contour_length":10,
                    "min_inertia_ratio":0.5,
                    "min_area": 3000,
                    "min_adjacent_distance":13
                }
            },
            "boxes": {
                "engine": "contour",
                "threshold": 0.4,
                "minsize": 25
            },
            "template": {},
            "text": {
                "engines": "azure"
            },
            "grids": {
                "minpath": 4,
                "band": 25
            },
            "count": -1
        }
        # save this config file
        logger.warning("New config file created!")
        with open(os.path.join("config", f"default_config.json"), 'w', encoding="utf-8") as fp:
            fp.write(json.dumps(config_data, indent=4))

    main(config=config_data)
