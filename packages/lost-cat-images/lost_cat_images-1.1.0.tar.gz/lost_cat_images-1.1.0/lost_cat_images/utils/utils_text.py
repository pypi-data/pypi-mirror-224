import cv2 as cv

def load_words(text_objs: list) -> list:
    """Will load a words

    parameters
    ----------
    text_objs: list of dict
        word_cluster: str
        word_cluster_box: list for lists
            [[x,y], [x,y], [...]]
        words: list
            bounding_box: list of lists
                [[x,y], [x,y], [...]]
            text: str
            confidence: float 0-1

    return
    ------
    dict:
        words: list of dict
            idx: int
            word: str
            bbox: tuple x,y,w,h
            contour: [[x,y], [x,y], [...]]
            conf: float 0-1
        phrases:
            idx: int
            phrase: str
            bbox: tuple x,y,w,h
            contours: [[x,y], [x,y], [...]]
            conf: float 0-1
            widx: list of int []
    """
    phrases = []
    words = []
    widx = -1

    # iterate the words...
    for pidx, t_obj in enumerate(text_objs):
        widxes = []
        p_conf = 0
        for w_obj in t_obj.get('words',[]):
            widx += 1
            widxes.append(widx)

            # process the bouding box to get the bbox of the
            # contour
            x,y,w,h = cv.boundingRect(w_obj.get('bounding_box'))
            p_conf += w_obj.get('confidence',0.0)
            words.append({
                'idx': widx,
                'word': w_obj.get('text'),
                'conf': w_obj.get('confidence',0.0),
                'contour': w_obj.get('bounding_box'),
                'bbox': (x,y,w,h)
            })

        # now to process the phrase details
        x,y,w,h = cv.boundingRect(t_obj.get('word_cluster_box'))
        phrases.append({
            'idx': pidx,
            'phrase': t_obj.get('word_cluster'),
            'bbox': (x,y,w,h),
            'contour': t_obj.get('word_cluster_box'),
            'conf': p_conf/len(widxes) if len(widxes) > 0 else 0.0,
            'widxes': widxes
        })

    return {
        'phrases': phrases,
        'words': words
    }
