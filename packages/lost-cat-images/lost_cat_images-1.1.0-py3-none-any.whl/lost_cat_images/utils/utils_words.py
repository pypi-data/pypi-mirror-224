import logging

logger = logging.getLogger(__name__)

def pivot_text(words: list) -> dict:
    """ Will process the list of words and pivot into
    a lost of words and phrases with bounding boxes

    parameters:
    ----------
    words: list
        word_cluster: str
        words: list
            boundingBox: list of points
            text: str
            confidence: float

    returns
    -------
    dict
        words: dict key idx
            idx: int
            bbox: tuple (x,y,w,h)
            text: str
            conf: float

        phrases: dict key idx
            idx: int
            bbox: tuple (x,y,w,h)
            text: str

    """
    texts = {}
    phrases = {}
    tidx = -1
    pidx = -1

    for t_obj in words:
        tox, toy, tow, toh = ([], [], [], [])
        for w_obj in t_obj.get('words',[]):
            tidx += 1
            contours = w_obj.get('boundingBox',[])
            x_coordinates, y_coordinates = zip(*contours)
            txn, tyn, txm, tym = (min(x_coordinates), min(y_coordinates), max(x_coordinates), max(y_coordinates))
            tox.append(txn)
            toy.append(tyn)
            tow.append(txm)
            toh.append(tym)
            texts[tidx] = {
                "idx": tidx,
                "bbox": (txn, tyn, txm-txn, tym-tyn),
                "contours": contours,
                "text": w_obj.get('text'),
                "conf": w_obj.get('confidence'),
            }

        # create the phrase object...
        pidx += 1
        phrases[pidx] = {
            'idx': pidx,
            'bbox': (min(tox), min(toy), max(tow) - min(tox), max(toh) - min(toy)),
            'text': t_obj.get('word_cluster'),
        }

    return {
        "words": texts,
        "phrases": phrases,
    }

def map_shape_text(shapes: list, word_data:dict) -> dict:
    """"Will map the shape to the supplied words and phrases

    parameters:
    -----------
    shapes: list
        idx: int
        origin: tuple (x, y)
        bbox: tuple (x, y, w, h)
    word_data: dict
        words: dict key idx
            idx: int
            bbox: tuple (x,y,w,h)
            text: str
            conf: float

        phrases: dict key idx
            idx: int
            bbox: tuple (x,y,w,h)
            text: str

    returns
    -------
    dict
        mapping of shape idx to list
        shape idx
            words: list of idx
            phrases: list of idx
    """
    data = {}

    logger.info("Shapes: %s %s", len(shapes), type(shapes))
    logger.info("Texts: %s %s", len(word_data), type(word_data))

    for label, data_value in word_data.items():
        logger.info('-> %s: Type: %s Len: %s', label, type(data_value), len(data_value))

    for shape in shapes:
        idx = shape.get('idx')
        x,y,w,h = shape.get('bbox')
        cx = x+int(w/2)
        cy = y+int(h/2)

        # now to create the mapping...
        # accept if the centrum of the word is inside the box
        for tidx, tobj in word_data.get('words', {}).items():
            tox, toy, tow, toh = tobj.get('bbox')
            cox = tox + int(tow/2)
            coy = toy + int(toh/2)
            if x < cox and y < coy and cox < x + w and coy < y + h:
                # is contained...
                if idx not in data:
                    data[idx] = {
                        'words': [],
                        'phrases': [],
                    }
                data[idx]['words'].append(tidx)

        for pidx, pobj in word_data.get('phrases', {}).items():
            tox, toy, tow, toh = pobj.get('bbox')
            cox = tox + int(tow/2)
            coy = toy + int(toh/2)
            if x < cox and y < coy and cox < x + w and coy < y + h:
                # is contained...
                if idx not in data:
                    data[idx] = {
                        'words': [],
                        'phrases': [],
                    }
                data[idx]['phrases'].append(pidx)

    return data
