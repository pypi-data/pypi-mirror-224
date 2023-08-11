""""""
from datetime import datetime
import logging
import re
import cv2 as cv
import pandas as pd
import numpy as np

from lost_cat.utils.rules_utils import Rule, RuleEngine, RuleState, RulesTool

logger = logging.getLogger(__name__)


def clean_text(text: str, operations: dict = None) -> str:
    """This will clean a text block and return
    a list of phrases"""

    logger.debug("CT: Before: %s", text)
    for _opk, _opv in operations.items():
        if _opv.get("stage","") == "pre":
            if _reg := _opv.get("regex"):
                text = re.sub(pattern=_reg, repl=_opv.get("replace",""), string=text, flags=re.IGNORECASE)
            else:
                _fnd = _opv.get("find", "")
                text = text.replace(_fnd, _opv.get("replace",""))

    logger.debug("CT: After: %s", text)
    return text

def process_shapes(shapes: list, words: dict, mappings: dict,
                   section: str = 'phrases') -> dict:
    """This will map the words to the shapes, and return a shape
    lookup with the phrase, sorted using a radial sort from top-left

    parameters
    ----------
    shapes: list
        a list of shapes
        idx
        origin
        bbox
        contours

    returns
    -------
    dict
        shape_idx: int
            shape: dict
                idx: int
                origin: tuple (x,y)
                bbox: tuple (x,y,w,h)
                contours: np.array
                phrase: str
    """
    if not mappings:
        mappings = {}

    shape_lookup = {}
    for shape in shapes:
        idx = shape.get('idx')
        shape_lookup[idx] = shape

        # now to get the phrasef wihtin this shape...
        sub_list = mappings.get(idx, {}).get(section,[])


        if len(sub_list) == 1:
            logger.debug("LIDX: %s", sub_list)
            shape['phrase'] = words.get(section, {}).get(sub_list[0]).get('text')
            logger.debug("ShapeL idx: %s phrase %s", idx, shape['phrase'])

        elif len(sub_list) > 1 :
            logger.debug("LIDX: %s", sub_list)
            items = [v for k, v in words.get(section, {}).items() if k in sub_list]
            arr = np.array([v['bbox'] for k, v in words.get(section, {}).items() if k in sub_list])
            r = (arr[:, 1]**2 + arr[:, 0]**2)
            parts = []
            for iidx in np.argsort(r):
                parts.append(items[iidx].get('text'))
            phrase = ' '.join(parts)

            shape['phrase'] = phrase
            logger.debug("ShapeL idx: %s phrase %s", idx, phrase)

    return shape_lookup

def process_shaperules(shape_lookup: dict, rules_data:list)-> dict:
    """ will process the shape_lookup and add the rules results to the
    shape object

    parameters
    ----------

    returns
    -------
    dict
        results: dataframe
        shape_idx: int
            shape: dict
                idx: int
                origin: tuple (x,y)
                bbox: tuple (x,y,w,h)
                contours: np.array
                phrase: str
                results: list
    """

    # load the rules
    rules = RulesTool()
    ops = {}
    for rule_defs in rules_data:
        for r in rule_defs.get("rules"):
            ruledict = {}

            for fld in ["name", "idx", "engine", "expr", "stop", "tags", "state", "options"]:
                if value := r.get(fld):
                    ruledict[fld] = value

            rule = Rule(**ruledict)
            rules.add_rule(rule)
            logger.info("Rules: Load: %s", rule)

        # now load the operations as well
        for op_label, op_rule in rule_defs.get("operations",{}).items():
            ops[op_label] = op_rule

    # now to process the shape data
    fields =  ['idx', 'origin', 'bbox', 'phrase']
    tags = set()
    rows = []
    for _, shape in shape_lookup.items():
        row = {}
        for fld in fields:
            row[fld] = shape.get(fld)

        if not shape.get('phrase'):
            continue

        phrase_clean = clean_text(text=shape.get('phrase',""), operations=ops)
        logger.info('Rules: Phrase: %s Clean: %s', shape.get('phrase',""), phrase_clean)
        # "rule": rule,
        # "phrase": phrase,
        # "result": {
        #    "passed": passed,
        #    "stop": stop,
        #    "tags": result.get("tags")
        for result in rules.run(phrases=[phrase_clean]):
            logger.info("Rules: %s -> %s", phrase_clean, result)
            for tag_key, tag_value in result.get('result',{}).get('tags',{}).items():
                tags.add(tag_key)
                if tag_key in fields:
                    row[f'tag.{tag_key}'] = tag_value
                else:
                    row[tag_key] = tag_value

        rows.append(row)

    # pivot to a csv, use pandas dataframe
    df = pd.DataFrame(rows)

    return {
        "rule_run":df,
        "shapes": shape_lookup
    }

def process_ellipses(ellipses: list, maxlength: int = 10) -> dict:
    """ Will process the ellipses and return a dataframe of the
    ellipse id, text id, text in the ellipse

    parameters
    ----------
    ellipses: dict
        'ellipse_idx': int
        'center': array x,y
        'size': array r, a
        'angle': float
        'texts': list
            'text_idx': int
            'text': str
            'bounding box': array
            'center': tuple x,y

    maxlength: int
        the cutoff for the word count in the ellipse

    returns
    -------
    dataframe
    """
    rows = []
    for ellipse in ellipses:
        if texts := ellipse.get('texts'):
            # we have a set of text elements
            if len(texts) > maxlength:
                logger.warning("Skipping ellipse idx: %s max: %s len: %s", ellipse.get('ellipse_idx'), maxlength, len(texts))
                continue

            # now to collect the center points and arrange from top elft corner
            tidxes = []
            if len(texts) == 1:
                phrase = texts[0].get('text')
                tidxes = texts[0].get('text_idx')
            elif len(texts) > 1:
                items = [t['text'] for t in texts]
                logger.debug("Ellipses: text: %s", items)
                tidxes = ', '.join([t['text_idx'] for t in texts])

                arr = np.array([t['center'] for t in texts])
                logger.debug("Ellipses: bbox: %s", arr)

                r = (arr[:, 1]**2 + arr[:, 0]**2)
                logger.debug("Ellipses: r: %s", r)
                logger.debug("Ellipses: sort: %s", np.argsort(r))

                parts = []
                for iidx in np.argsort(r):
                    parts.append(items[iidx])
                phrase = ' '.join(parts)
            else:
                continue

            # now add to the table
            rows.append({
                'idx': ellipse.get('ellipse_idx'),
                'phrase': phrase,
                'center': str(ellipse.get('center')),
                'tidxes': tidxes
            })

    # convert to dataframe
    df = pd.DataFrame(rows)
    logger.debug("Ellipses: Rows: %s DF: %s", len(rows), df.shape)

    return df
