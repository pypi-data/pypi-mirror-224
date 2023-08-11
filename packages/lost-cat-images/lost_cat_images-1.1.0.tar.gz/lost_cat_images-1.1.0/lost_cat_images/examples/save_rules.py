from datetime import datetime
import logging
import glob
import json
import re
import os

from lost_cat.utils.rules_utils import Rule, RuleEngine, RuleState, RulesTool
from lost_cat_images.parsers.engimg_parser import EngImgParser

logger = logging.getLogger(__name__)

def get_ops() -> dict:
    """operations to run against the text to clean
    up artifacts of ocr"""
    return {
        "ocrpre01":{
            "stage": "pre",
            "find": "-�",
            "replace": "-",
        },
        "ocrpost01":{
            "stage": "pre",
            "find": "�-",
            "replace": "-",
        },
        "ocre01":{
            "stage": "pre",
            "find": "�",
            "replace": "-",
        },
        "ocrpre02":{
            "stage": "pre",
            "find": "-\u2014",
            "replace": "-",
        },
        "ocrpost02":{
            "stage": "pre",
            "find": "\u2014-",
            "replace": "-",
        },
        "ocre02":{
            "stage": "pre",
            "find": "\u2014",
            "replace": "-",
        },
        "m01":{
            "stage": "pre",
            "find": "\u201c",
            "replace": " ",
        },
        "m02":{
            "stage": "pre",
            "find": "\u00b0",
            "replace": " ",
        },
        "unit":{
            "stage": "pre",
            "find": "UNT",
            "replace": "UNIT",
        },
        "plant":{
            "stage": "pre",
            "find": "PUT",
            "replace": "PLANT",
        },
        "facility":{
            "stage": "pre",
            "find": "FACIUTY",
            "replace": "FACILITY",
        },

    }

def get_tags():
    """returns a dict of tags
        <tag>
    """
    return {
        "joins": [" ", "-", "_", "�"],
        "P-001": ["P", "001"],
        "M-001": ["M", "001"],
        "MOV-002": ["MOV", "002"]
    }

def get_rules() -> RulesTool:
    """Returns the rules as RulesTool object"""
    rules = RulesTool()
    ridx = 0

    #  DRAWING NO. 5-2.235-001

    numstr = r"[0-9DOSB]+[\-\.]+[0-9DOSB\-\.]+[0-9DOSB]+"
    # tags
    ridx += 1
    rules.add_rule(Rule(
        name="tags",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"(?P<tag>[A-Z0851]{2,5}[ \-]{1,2}[0-9SBDO]{3,10})",
        tags=[{"key":"tag", "group":"tag"}],
        stop=False,
        state=RuleState.SINGLE,
        options={"findall":True}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="DNUM Simple",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"[D|O]RAWING[ NO\.]{1,4}(?P<number>[0-9\-\.]+)$",
        tags=[{"key": "drawingnum", "group": "number"}],
        stop=True,
        state=RuleState.SINGLE,
        options={} #{"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="DNUM Simple",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"[D|O]RAWING NUM[B|8]ER[ \.]{1,4}(?P<number>[0-9\-\.]+)$",
        tags=[{"key": "drawingnum", "group": "number"}],
        stop=True,
        state=RuleState.SINGLE,
        options={} #{"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="DNUM Simple",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"[O|D]W[R|G][ NO\.]{1,4}(?P<number>[0-9\-\.]+)$",
        tags=[{"key": "drawingnum", "group": "number"}],
        stop=True,
        state=RuleState.SINGLE,
        options={} #{"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="drawing",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"NO[ \.]{1,2}(?P<number>[0-9\-\.]+)$",
        tags=[{"key": "drawingnum", "group": "number"}],
        stop=True,
        state=RuleState.SINGLE,
        options={"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="drawing",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"(?P<number>[0-9DOSB]+[\-\.]+[0-9DOSB\-\.]+[0-9DOSB]+)",
        tags=[{"key": "number", "group": "number"}],
        stop=True,
        state=RuleState.SINGLE,
        options={"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="revision",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"Rev[\. \-](?P<number>[0-9OBDS]+)",
        tags=[{"key":"revision", "group":"number"}],
        stop=False,
        state=RuleState.SINGLE,
        options={"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="title",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"title[ \.\-](?P<text>.*)",
        tags=[{"key":"title", "group":"text"}],
        stop=False,
        state=RuleState.SINGLE,
        options={"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="plant",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"plant[ \.\-](?P<text>.*)",
        tags=[{"key":"plant", "group":"text"}],
        stop=False,
        state=RuleState.SINGLE,
        options={"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="issue",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"issue[ \.\-](?P<text>.*)",
        tags=[{"key":"issue", "group":"text"}],
        stop=False,
        state=RuleState.SINGLE,
        options={"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="unit",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"unit[ \.\-](?P<text>.*)",
        tags=[{"key":"unit", "group":"text"}],
        stop=False,
        state=RuleState.SINGLE,
        options={"flags": re.IGNORECASE}
    ))

    ridx += 1
    rules.add_rule(Rule(
        name="facility",
        idx=ridx,
        engine=RuleEngine.REGEX,
        expr=r"facility[ \.\-](?P<text>.*)",
        tags=[{"key":"facility", "group":"text"}],
        stop=False,
        state=RuleState.SINGLE,
        options={"flags": re.IGNORECASE}
    ))

    return rules

def get_phraseblocks(filepath: str):
    """Return a set of phrase to process"""
    phraseblocks = {}
    # INFO:__main__:	{0}: Phrases: [' <...> ']
    reg = re.compile(r".*\{(?P<fidx>[\d]+)\}:\sPhrases:\s\['(?P<phrase>.*)'\].*") #

    with open(filepath) as f:
        for line in f:
            if m:= reg.match(line.rstrip()):
                fidx = int(m.group("fidx"))
                phrase = m.group("phrase")
                phrase =  clean_text(text=phrase, operations=get_ops())
                logger.info("{%s}: %s", fidx,  phrase)

                if fidx not in phraseblocks:
                    phraseblocks[fidx] = []
                phraseblocks[fidx].append(phrase)

    return phraseblocks

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

def main():
    """Run the main thread"""
    rules = get_rules()

    process_ops = {
        "rules": rules.export(),
        "operations": get_ops(),
        "tags": get_tags(),
        "sources":[
            "data\\*"
        ],
        "export":{
            "filename": "export.json"
        },
        "lookups":{
            "tags": {"file":"tag.tsv","type":"tsv"},
            "facility":{"file":"facility.csv", "type": "csv"},
            "plant": {"file":"plant.csv", "type": "csv"},
            "unit": {"file":"unit.csv", "type": "csv"}
        }
    }
    logger.info("Rules:")
    for rule in rules.rules:
        logger.info("R: %s", rule.export())
        #process_ops["rules"].append(rule.export())
    # save to a text file...

    with open(r"config\imgrules.json", "w") as fp:
        json.dump(process_ops, fp, indent=4)
    return

    data = {}
    phraseblocks = get_phraseblocks()
    
    for fidx, phrases in phraseblocks.items():
        logger.info("fidx: %s", fidx)
        logger.debug("{%s}: Phrases: %s", fidx, phrases)
        metadata = {}

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

        # extract the tags if found:
        found_tags = set()
        tag_lookup = get_tags()
        joins = tag_lookup.get("joins")
        for phrase in phrases:
            for tag, tagparts in tag_lookup.items():
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

        # show the results
        for tag,value in metadata.items():
            logger.info("{%s}: Tag: %s => %s", fidx, tag, value)

        data[fidx] = {
            "phrases": phrases,
            "metadata": metadata,
            "tags": list(found_tags)
        }
        logger.info("Data: %s", data)

    # save the dump to json
    with open(r"data\imgexport.json", "w") as fp:
        json.dump(data, fp, indent=4)

if __name__ == "__main__":
    nb_name = "TestRules"
    if not os.path.exists("logs"):
        os.mkdir("logs")

    _logname = "{}.{}".format(nb_name, datetime.now().strftime("%Y%m%d"))
    filename=f'logs\\log.{_logname}.log'
    if os.path.exists(filename):
        os.remove(filename)

    logging.basicConfig(filename=filename, level=logging.INFO)
    main()