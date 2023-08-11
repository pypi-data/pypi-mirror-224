from lost_cat_images.utils.tools import convert_image
from lost_cat_images.utils.tools import grayscale
from lost_cat_images.utils.tools import threshold

from lost_cat_images.utils.clean import color_segmentation
from lost_cat_images.utils.clean import denoise
from lost_cat_images.utils.clean import realign
from lost_cat_images.utils.clean import deskew

from lost_cat_images.utils.extract import extract_contours
from lost_cat_images.utils.extract import boxes
from lost_cat_images.utils.extract import grids
from lost_cat_images.utils.extract import analyze
from lost_cat_images.utils.extract import text
from lost_cat_images.utils.extract import ellipse
from lost_cat_images.utils.extract import run_rules

import base64
import json
import numpy as np

class NumpyArrayEncoder(json.JSONEncoder):
    """https://stackoverflow.com/questions/3488934/simplejson-and-numpy-array/24375113#24375113"""

    def default(self, obj):
        """If input object is an ndarray it will be converted into a dict
        holding dtype, shape and the data, base64 encoded.
        """
        if isinstance(obj, np.ndarray):
            if obj.flags['C_CONTIGUOUS']:
                obj_data = obj.data
            else:
                cont_obj = np.ascontiguousarray(obj)
                assert(cont_obj.flags['C_CONTIGUOUS'])
                obj_data = cont_obj.data
            data_b64 = base64.b64encode(obj_data)
            return dict(__ndarray__=data_b64,
                        dtype=str(obj.dtype),
                        shape=obj.shape)
        # Let the base class default method raise the TypeError
        super(NumpyArrayEncoder, self).default(obj)

def json_numpy_obj_hook(dct):
    """Decodes a previously encoded numpy ndarray with proper shape and dtype.

    :param dct: (dict) json encoded ndarray
    :return: (ndarray) if input was an encoded ndarray
    """
    if isinstance(dct, dict) and '__ndarray__' in dct:
        data = base64.b64decode(dct['__ndarray__'])
        return np.frombuffer(data, dct['dtype']).reshape(dct['shape'])
    return dct