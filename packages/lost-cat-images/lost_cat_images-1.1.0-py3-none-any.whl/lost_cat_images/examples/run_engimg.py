from datetime import datetime
import logging
import csv
import glob
import json
import re
import os

from lost_cat.utils.rules_utils import Rule, RuleEngine, RuleState, RulesTool
from lost_cat_images.parsers.engimg_parser import EngImgParser, cv2

logger = logging.getLogger(__name__)

def load_tsv(filepath: str, hasheader:bool = True, skiprows:int = 0) -> list:
    """loads a tab seperated file into a list of dictionary"""
    rows = []
    with open(filepath, "r") as fp:
        reader = csv.DictReader(fp, delimiter='\t')
        for row in reader:
            rows.append(row)
    return rows

def load_csv(filepath: str, hasheader:bool = True, skiprows:int = 0) -> list:
    """loads a tab seperated file into a list of dictionary"""
    rows = []
    with open(filepath, "r") as fp:
        reader = csv.DictReader(fp, delimiter='\t')
        for row in reader:
            rows.append(row)
    return rows

def load_tags(rows: list, fields: list = None):
    """will load the tag table into a match lookup
        Split into parts based on word - number boundary

        tag:
            parts: [[]]        => list of lists
            map: <tag to use>  -> return this value when found

    """
    mappings = {
        0: ["O"],
        "O": [0],
        1: ["I", "l"],
        3: [5]


    }
    tags = {}
    if fields is None:
        fields = rows[0].keys()

    for row in rows:
        tag_old = row.get(fields[0])
        tag_new = row.get(fields[1])
        tag = tag_old if tag_old is not None else tag_new

    return tags

def load_fuzzy(rows: list):
    """This will build up a lookup for the values
        find: replace
    """
    fuzzy = {}

    return fuzzy

def clean_text(text: str, operations: dict = None) -> str:
    """This will clean a text block and return
    a list of phrases"""

    logger.info("CT: Before: %s", text)
    for _opk, _opv in operations.items():
        if _opv.get("stage","") == "pre":
            if _reg := _opv.get("regex"):
                text = re.sub(pattern=_reg, repl=_opv.get("replace",""), string=text, flags=re.IGNORECASE)
            else:
                _fnd = _opv.get("find", "")
                text = text.replace(_fnd, _opv.get("replace",""))
    logger.info("CT: After: %s", text)
    return text

def extract_tags(phrases: list, tags: dict):
    """Looks and load the tags if found"""
    found_tags = set()
    for phrase in phrases:
        for tag, tagparts in tags.items():
            if tag in phrase:
                # direct hit, yay
                found_tags.add(tag)
            else:
                # we need to be smart and find the part of the
                search = "[.]+".join(tagparts)
                if m:= re.search(search, phrase):
                    logger.info("Found %s in %s", search, phrase)
                    if (m.end() - m.start()) < (len(tag) + len(tagparts)):
                        logger.info("Candidate: %s in %s", search, m.span())
                        found_tags.add(tag)

    return list(found_tags)

def run_rules(phrases: list, rules: RulesTool, metadata: dict, fidx: int):
    """run the rules against the phrases"""
    for item in rules.run(phrases=phrases):
        logger.info("{%s}: Item: %s", fidx, item)
        rule = item.get("rule")
        result = item.get("result")

        if result.get("passed", False):
            logger.info("\tRule %s:%s => Tags: %s", rule.idx, rule.name, result.get("tags",{}))

        for tag, value in result.get("tags",{}).items():
            if tag not in metadata:
                metadata[tag] = value
            else:
                if value != metadata.get(tag):
                    if isinstance(metadata.get(tag), list):
                        metadata[tag].append(value)
                    else:
                        # handle converting to list
                        metadata[tag] = [metadata.get(tag), value]

    return metadata

def main():
    """Loop through the found files and process
    save the results to a text file"""

    # load the rules files...
    configdata = {
        "rules": {"file": "imgrules.json", "data":{}},
        "settings": {"file": "imgsettings.json", "data":{}},
    }

    for key, value in configdata.items():
        path = os.path.join("config", value.get("file"))
        if os.path.exists(path):
            with open(path, "r") as fp:
                value["data"] = json.load(fp)

    ruledefs = configdata.get("rules",{}).get("data",{}).get("rules")
    rules = RulesTool()
    for r in ruledefs:
        ruledict = {}

        for fld in ["name", "idx", "engine", "expr", "stop", "tags", "state", "options"]:
            if value := r.get(fld):
                ruledict[fld] = value

        rule = Rule(**ruledict)
        rules.add_rule(rule)

    tagdefs = configdata.get("rules",{}).get("data",{}).get("tags")
    ops = configdata.get("rules",{}).get("data",{}).get("operations")
    exportdefs = configdata.get("rules",{}).get("data",{}).get("export")
    sources = configdata.get("rules",{}).get("data",{}).get("sources",[])
    logger.info("Sources: %s", sources)

    # parser config
    if configEng := configdata.get("settings",{}).get("data",{}):
        logger.info("Config: %s", configEng)
    else:
        logger.info("Config: Loading from class!")
        configEng = EngImgParser.avail_config()

        configEng["parser"] = {
            "file": {
                "id": 0,
            },
            "kernel": {
                "size": 3,
            },
            "operations": {
                "blur": True,
                "heal": True,
            },
            "threshold": {
                "thresh": 75,
                "maxval": 255,
                "type": cv2.THRESH_BINARY | cv2.THRESH_OTSU,
            },
            "contours": {
                "mode": cv2.RETR_TREE,
                "method": cv2.CHAIN_APPROX_TC89_L1
            },
            "extract": {
                "ratio": 3,
                "bleed": 4,
                "mindim": 1000,
                "useblur": False,
                "kernel": 3,
                "dilate": -1,
                "erode": 3,
                "resize": cv2.INTER_CUBIC,  # INTER_AREA, INTER_CUBIC, INTER_LANCZOS4, INTER_NEAREST, INTER_LINEAR
                "shape": "ellipse",
                "tesseract": {
                    "i2d": "--psm 1"
                },
            }
        }

        # save the config to a file
        path = os.path.join("config", configdata.get("settings",{}).get("file"))
        with open(path, "w") as fp:
            json.dump(configEng, fp, indent=4)

    # select the extensions to process
    exts = []
    for src in configEng.get("source",[]):
        if src.get("key") == 'ext':
            exts = src.get("values")
            logger.info("Accept: %s", exts)

    # store the output...
    data = {}
    for folderpath in sources:
        logger.info("Scan: %s", folderpath)
        for fidx, fpath in enumerate(glob.glob(folderpath)):
            _, fname = os.path.split(fpath)
            filename, ext = os.path.splitext(fname)
            if ext.lower() in exts:
                if filename not in data:
                    data[filename] = {
                        "fidx": fidx,
                        "path": fpath
                    }
                start = datetime.now()
                logger.info("TIME: {%s} START: %s", fidx, start.strftime("%Y-%m-%d %H:%M:%S"))
                data[filename]["blocks"] = process_file(uri=fpath, fidx=fidx, config=configEng)
                duration = datetime.now() - start
                logger.info("TIME: {%s} END: %s -> %s", fidx, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), duration.total_seconds())

    lufunc = {
        "tsv": load_tsv,        # simple load of a tsv or csv into a list of dicts
        "csv": load_csv,
        "tags": load_tags,      # load the tags, mulitple columns, and map to the new values
                                # assume 3 cols: old tag, new tag (if any), description
        "fuzzy": load_fuzzy     # prepares a fuzsy lookup table to find values,
                                # assumes single column
    }

    # load up the lookups...
    for lukey, ludata in configdata.get("rules",{}).get("data",{}).get("lookups",{}).items():
        logger.info("Lookups: %s => %s", lukey, ludata.get("file"))


    # now to extract the tags and other information
    for filename, value in data.items():
        fidx = value.get("fidx")
        txtname = f"data\\{filename}_{fidx}.txt"
        blocks = []
        tags = set()
        metadata = {}
        with open(txtname, "w") as fp:
            logger.info("TAGS: {%s}", fidx)
            fp.write(f"File: {filename}\n")
            for bnum, bvalue in value.get("blocks",{}).items():
                fp.write(f"Block: {bnum}\n")
                logger.info("\t{%s}: Blocks: %s => %s\n", fidx, bnum, bvalue)
                phrases = []
                for pnum, text in bvalue.items():
                    phrase = ' '.join(text)
                    phrase = clean_text(text=phrase, operations=ops)
                    fp.write(f"\t{fidx}\t{pnum} => {phrase}\n")
                    phrases.append(phrase)
                #
                logger.info("\t{%s}: Phrases: %s", fidx, phrases)
                results = rules.run(phrases=phrases)
                logger.info("\t{%s}: Results: %s", fidx, results)
                blocks.append(phrases)

                # get the tags...
                found_tags = extract_tags(phrases=phrases, tags=tagdefs)
                tags.update(found_tags)

                # metadata
                metadata = run_rules(phrases=phrases, rules=rules,
                            metadata=metadata, fidx=fidx)

        # save to data object
        data[filename] = {
            "fidx": fidx,
            "blocks": blocks,
            "tags": list(tags),
            "metadata": metadata,
        }

    # save the dump to json
    path = os.path.join("data", exportdefs.get("filename", "export.json"))
    with open(path, "w") as fp:
        json.dump(data, fp, indent=4)

def process_file(uri:str, fidx:int = 0, config:dict = None) -> dict:
    """run the initial parser against"""
    logger.info("process %s", uri)

    engobj = EngImgParser(uri)

    if config is not None:
        conf = config
    else:
        conf = engobj.get_config()

    if "parser" not in conf:
        conf["parser"] = {}
    if "file" not in conf.get("parser"):
        conf["parser"]["file"] = {}
    conf["parser"]["file"]["id"] = fidx
    if "debug" not in conf.get("parser"):
        conf["parser"]["debug"] = {}
    conf["parser"]["debug"]["save"] = True

    engobj.set_config(conf)

    funx = engobj.avail_functions().get("parser")
    data = funx()
    text_blocks = {}
    for key, value in data.items():
        logger.info("\t%s => %s", key, type(value))
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                logger.info("\t%s => %s", subkey, type(subvalue))
                if isinstance(subvalue, list):
                    for item in subvalue:
                        blocknum = item.get("idx")
                        paranum = item.get("par_num")
                        textarr = item.get("text")

                        if blocknum not in text_blocks:
                            text_blocks[blocknum] = {}
                        if paranum not in text_blocks.get(blocknum):
                            text_blocks[blocknum][paranum] = []
                        text_blocks[blocknum][paranum].append(textarr)

    # now to use the contour function
    #funx = engobj.avail_functions().get("contours")
    #cc_data = funx()

    engobj = None
    return text_blocks

if __name__ == "__main__":
    nb_name = "EngImg"
    if not os.path.exists("logs"):
        os.mkdir("logs")
    if not os.path.exists(r"data\eng\crops"):
        os.makedirs(r"data\eng\crops")

    _logname = "{}.{}".format(nb_name, datetime.now().strftime("%Y%m%d"))
    logpath = os.path.join("logs", f"{_logname}.log")
    if os.path.exists(logpath):
        os.remove(logpath)

    logging.basicConfig(filename=logpath, level=logging.INFO)

    if not os.path.exists(r"data\eng\crops"):
        os.makedirs(r"data\eng\crops")

    main()
