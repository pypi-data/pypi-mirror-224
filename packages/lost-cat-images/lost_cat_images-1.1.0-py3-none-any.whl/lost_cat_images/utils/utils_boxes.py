import logging
import numpy as np
import cv2 as cv
from scipy.sparse import csr_matrix
from lost_cat_images.utils.image_templates import create_targets

from lost_cat_images.utils.utils_nodepaths import PathNode, PathNodeTree

logger = logging.getLogger(__name__)

def build_colors(size: int = 4, step: int = 50):
    """
    build a color pallette for the image uses
    parameters
    ----------
    size : int default = 4
        the number of colors to generate
    step: int default = 509
        the step for each color reduction

    """
    r, g, b = 255, 0, 175
    colors = []
    if size == 4:
        colors.append((255, 0  , 0  ))
        colors.append((0  , 255, 0  ))
        colors.append((255, 0  , 255))
        colors.append((255, 255, 0  ))
    else:
        for i in range(size):
            colors.append((b,g,r))
            r -= step
            if i > 0 and i % 2 == 0:
                g -= step
            if i > 0 and i % 3 == 0:
                b -= step

            if r <= 0:
                r = 255
            if b <= 0:
                r = 255
            if g <= 0:
                r = 255

    return colors

def find_targets(image: object, config: dict) -> dict:
    """
    will use the opencv match template function to
    find the targets located in the image.
    A sparsematrix is returned, using the target idx +1
    as the point

    parameters
    ----------
    image
        the image to pass to be processed, single channel
    config
        targets: list or np.arrays
            a list of arrays to match to the image
        offsets: list of points
            offset (x,y) for each target
        threshold: double
            the threshold to use for the match

    return:
    ------
    dict
        images: dict set of images
            "processed"
        data:
            "matrix": np.array
                sparse
        errors: list of error messages if any
    """
    # process the config and set default values...
    targets = config.get("targets", [])
    offsets = config.get('offsets', [])
    threshold = config.get("threshold", 0.8)
    markup_image = config.get("image")
    if markup_image is not None:
        colors = build_colors(size=len(targets), step=75)

    if len(image.shape) != 2:
        return {
            "images": {},
            "data": {},
            "errors": {
                "Invalid Image, expecting a binary image"
            }
        }

    h, w = image.shape

    # create a sparse matrix the same size as the image...
    sparseMatrix = csr_matrix((h, w), dtype = np.int8)

    # detect the targets..
    for idx, target in enumerate(targets):
        logger.debug("target[%s]: %s", idx+1, target)
        #
        res = cv.matchTemplate(image,target, cv.TM_CCOEFF_NORMED)
        loc = np.where( res >= threshold)
        tw,th = target.shape

        for pt in zip(*loc[::-1]):
            x, y = pt
            xo, yo = offsets[idx]
            if markup_image is not None:
                if idx == 0:
                    cv.line(img=markup_image, pt1=(x-15, y), pt2=(x+15, y),
                            color=(0,0,255), thickness=1)
                    cv.line(img=markup_image, pt1=(x, y-15), pt2=(x, y+15),
                            color=(0,0,255), thickness=1)

                cv.circle(img=markup_image, center=(x,y), radius=5,
                          color=colors[idx], thickness=1)
                cv.circle(img=markup_image, center=(x,y), radius=10,
                          color=colors[idx], thickness=1)
                cv.rectangle(markup_image, pt, (x + tw, y + th), (0,255,0), 1)

            logger.info("Point: %s Offset: %s -> %s", (x,y), (xo,yo),idx)
            sparseMatrix[y+yo, x+xo] = idx + 1
    data = {
        "matrix": sparseMatrix,
    }
    if markup_image is not None:
        data['images'] = {}
        data['images']['markup'] = markup_image
    return data

def group_vertices(matrix: csr_matrix, config: dict) -> dict:
    """Will process the matrix and look for pairs on
    the x or y axis
    parameters
    ----------
    matrix: a sparse matrix of points and vertix index
    config:
        vertices: a list in the order of the
            1 ┎    ┐ 3

            2 └    ┘ 4
        expand: bool
            if true will find all possible points
            if false will only return the next target

    return
    ------
    dict:
        images: dict
            a key value set of images, optional
        data: dict
            a key value set of data elements, optional
            rectangles: list of (x,y,w,h)
    """
    vertices = config.get('vertices', [(1,2),(2,3),(4,3),(1,4)]) if config else [(1,2),(2,3),(4,3),(1,4)]
    logger.debug('vertices: %s', vertices)

    # expand is used to det3ermine whether to use next point
    # or fetch all possible points
    # expand = True means get all possible points on x or y axis
    expand = config.get('expand', True) if config else True
    logger.debug('expand: %s', expand)

    # prepare and initialize the memory objects
    # prepare the vertices and load the edges
    check_vertices = set()
    edges = {}
    for v_1, v_2 in vertices:
        if v_1 not in edges:
            edges[v_1] = {}
        if v_2 not in edges[v_1]:
            edges[v_1][v_2] = {}
        if v_1 != 1:
            check_vertices.add((v_1, v_2))

    logger.debug('update check: %s', check_vertices)

    # process the sparsematrix and build
    # a list of shapes, xy and yx points
    xy_points = {}
    yx_points = {}
    shapes = {}
    for row, col in zip(*matrix.nonzero()):
        val = matrix[row, col]
        # organize to help to the lookups....
        if row not in yx_points:
            yx_points[row] = {}

        if col not in xy_points:
            xy_points[col] = {}

        yx_points[row][col] = val
        xy_points[col][row] = val

        # find the top left corner...
        # this assumes 1 is the top left corner
        if val == 1:
            shapes[(col, row)] = {}

        # get the seed idx
        for v_1, v_2 in vertices:
            if val == v_1:
                edges[v_1][v_2][(col, row)] = set()

            # add the vertices
            if val == 1:
                shapes[(col, row)][(v_1, v_2)] = []

        if val == 1:
            logger.debug("INIT: point: %s shapes: %s", (col, row), shapes.get((col, row)))

    logger.debug("edges: %s", edges)

    # get the horizontal and vertically points
    for v_1, v_2 in vertices:
        logger.debug("Vertix: %s", (v_1, v_2))
        for x,y in sorted(edges.get(v_1,{}).get(v_2,{}).keys()):
            y_points = sorted(xy_points.get(x).keys())
            x_points = sorted(yx_points.get(y).keys())

            idx_y = y_points.index(y)
            idx_x = x_points.index(x)

            logger.debug("Start point: %s: idx [%s] idy [%s]\n\tX: %s\n\tY: %s", (x, y), idx_x, idx_y, x_points, y_points)

            # process the vertical
            if idx_y + 1 < len(y_points):
                pt_candidates = []
                if expand:
                    # work down the points and return the matching edges
                    for next_y in y_points[idx_y+1:]:
                        if xy_points.get(x,{}).get(next_y,{}) == v_2:
                            pt_candidates.append(next_y)
                else:
                    next_y = y_points[idx_y+1]
                    if xy_points.get(x,{}).get(next_y,{}) == v_2:
                        pt_candidates.append(next_y)

                if len(pt_candidates) > 0:
                    logger.debug('Point: %s Candidates Y: %s', (x,y), pt_candidates)

                for next_y in pt_candidates:
                    edges[v_1][v_2][(x, y)].add((x,next_y))
                    logger.debug('line_y: %s: %s -> %s', (v_1, v_2), (x,y), (x,next_y))

                    # apply the offsets, if we have the matching side...
                    if (v_1, v_2) in shapes.get((x,y),{}):
                        shapes[(x, y)][(v_1, v_2)].append([(x,y), (x,next_y)])
                        logger.debug("point: %s shapes: %s", (x,y), shapes[(x, y)])

            # process the horizontal
            if idx_x + 1 < len(x_points):
                pt_candidates = []
                if expand:
                    # work down the points and return the matching edges
                    for next_x in x_points[idx_y+1:]:
                        if yx_points.get(y,{}).get(next_x,{}) == v_2:
                            pt_candidates.append(next_x)
                else:
                    next_x = x_points[idx_x+1]
                    if yx_points.get(y,{}).get(next_x,{}) == v_2:
                        pt_candidates.append(next_x)

                if len(pt_candidates) > 0:
                    logger.debug('point: %s candidates X: %s', (x,y), pt_candidates)
                for next_x in pt_candidates:
                    edges[v_1][v_2][(x, y)].add((next_x, y))
                    logger.debug('line_x: %s: %s -> %s', (v_1, v_2), (x,y), (next_x,y))

                    # apply the offsets, if we have the matching side...
                    if (v_1, v_2) in shapes.get((x,y),{}):
                        shapes[(x, y)][(v_1, v_2)].append([(x,y), (next_x,y)])
                        logger.debug("point: %s shapes: %s", (x,y), shapes[(x, y)])

    # run through the shapes and find the missing edges...
    complete = {}
    for (x,y), sides in shapes.items():
        logger.debug('point: %s sides: %s', (x, y), sides)
        # sides
        # <point (x,y)>: {
        #   <edge: (v_1, v_2)>: list [<point: (x1, y1)>, <point: (x2, y2)>]],

        # check which sides are populated...
        # if in check_missing then used the other points to
        points = {}
        for v_1, v_2 in vertices:
            if side := sides.get((v_1, v_2)):
                for s in side:
                    if v_1 not in points:
                        points[v_1] = []
                    if s[0] not in points[v_1]:
                        points[v_1].append(s[0])

                    if v_2 not in points:
                        points[v_2] = []
                    if s[1] not in points[v_2]:
                        points[v_2].append(s[1])

            elif (v_1, v_2) in check_vertices:
                # we need to get this points...
                if v_1 not in points:
                    points[v_1] = []
                if v_2 not in points:
                    points[v_2] = []

        # now we have the known points
        # we can calculate the edges to find
        logger.debug('Points: %s', points)

        for v_1, v_2 in check_vertices:
            logger.debug('Checks: (%s, %s) v1: %s v2: %s', v_1, v_2, points.get(v_1), points.get(v_2))

            # skip if the points are loaded
            if points.get(v_1) and points.get(v_2):
                logger.debug("SKIPPING: [lookup] points: %s sides: %s", points, sides)
                continue

            # get the first points
            for pt_1 in points.get(v_1, []):
                logger.debug("point: %s edge: %s pt_1: %s type: %s", (x,y), (v_1, v_2), pt_1, type(pt_1))
                # remove offset
                if not isinstance(pt_1, tuple):
                    continue

                x_1, y_1 = pt_1
                pt_1 = (x_1, y_1)

                for pt_2 in edges.get(v_1, {}).get(v_2, {}).get(pt_1, {}):
                    # apply offsets, edges is raw data
                    x_2, y_2 = pt_2
                    pt_2 = x_2, y_2

                    logger.debug("pt_1: %s pt_2: %s", (x_1, y_1), pt_2)
                    shapes[(x,y)][(v_1, v_2)] = [pt_1, pt_2]
                    if pt_2 not in points[v_2]:
                        points[v_2].append(pt_2)

        # check all points are populated...
        is_complete = True
        for _, v in points.items():
            if v is None:
                is_complete = False
                break

        if not is_complete:
            logging.info("INVALID Loop check Points: %s", points)
            continue

        if not any(points.values()):
            logging.info("INVALID any Points: %s", points)
            continue

        # add the shape to complete
        if (x,y) not in complete:
            complete[(x,y)] = []
        complete[(x,y)].append(points.copy())

    data = {
        'edges': edges,
        'shapes': complete,
    }
    return data

def extract_shapes(image: object, config: dict) -> dict:
    """
    takes an image and will check the supplied shapes are valid shapes
    i.e. solid border pixels percentage over threshold

    parameters
    ----------
    image
        [binary image] the image to pass to be processed, single channel
    config
        shapes: dict
            <origin>: {
                <template id>: list <point>
                ...
            }
        threshold: double
            the threshold to use for the match
        minh: int
        minw: int

    return:
    ------
    dict
        images: dict set of images
            "markup"
        data:=
            "shapes": dict
    """
    minsize = config.get('minsize', 10) if config else 10
    minw = config.get('minh', minsize) if config else minsize
    minh = config.get('minh', minsize) if config else minsize

    border = config.get('border', 2) if config else 2
    threshold_border = config.get('threshold_border', 0.4) if config else 0.4

    shapes = config.get('shapes')
    markup_image = config.get("image")

    font = cv.FONT_HERSHEY_SIMPLEX

    # check for missing shapes
    if not shapes:
        return {
            "images": {},
            "data": {},
            "errors": {
                "Shapes are missing"
            }
        }

    # process the origins
    sidx = 0
    found = []
    for pidx, (pt, pt_list) in enumerate(shapes.items()):
        # build the paths for this origin...
        for item in pt_list:
            orgin_node = PathNode(pt)
            origin_tree = PathNodeTree()
            origin_tree.head = orgin_node

            if len(item) != 4:
                #logger.warning("skipping: %s %s", len(item), item)
                continue
            #logger.warning("Processing: %s %s %s", pt, len(item), item)

            # add the paths...
            for pt_d in item.get(2,[]):
                logger.info('1 Point: %s', pt_d)
                d_node = PathNode(pt_d)
                origin_tree.head.add_node(ancestor=pt, new_node=d_node)

                for pt_e in item.get(3,[]):
                    logger.info('2\tPoint: %s', pt_e)
                    e_node = PathNode(pt_e)
                    origin_tree.head.add_node(ancestor=pt_d, new_node=e_node)

                    for pt_f in item.get(4,[]):
                        logger.info('3\t\tPoint: %s', pt_f)
                        f_node = PathNode(pt_f)
                        origin_tree.head.add_node(ancestor=pt_e, new_node=f_node)

            # now we have the system loaded
            # get the paths...
            shape_paths = list(filter(lambda x: len(x)==4, origin_tree.contours()))
            logger.info("Candidates: %s", shape_paths)

            if markup_image is not None:
                cv.circle(img=markup_image, center=pt, radius=5,color=(0,255,0), thickness=1)

            for sp in shape_paths:
                logger.info("sp: %s", sp)
                x,y = sp[0]
                x2,y2 = sp[2]
                x3,y3 = sp[3]
                if not (x == x3 or y == y3):
                    logging.warning("This shape doesn't close %s", sp)
                    continue

                w,h = x2-x,y2-y

                if h <= minh or w <= minw:
                    continue

                # Now to test the pixel border
                pixels1 = image[y:y+h, x-border:x]
                pixels2 = image[y:y+h, x+w:x+w+border]
                pixels3 = image[y-border:y, x:x+w]
                pixels4 = image[y+h:y+h+border, x:x+w]
                pixsum = (pixels1.sum() + pixels2.sum() + pixels3.sum() + pixels4.sum())
                pixsize = (pixels1.size + pixels2.size + pixels3.size + pixels4.size)

                border_ratio =  pixsum / pixsize if pixsize > 0 else 255
                if border_ratio < (255 * threshold_border):
                    cv.putText(img=markup_image, text=str(sidx),
                        org=(x+10, y+10), fontFace=font, fontScale=0.5, color=(0, 0, 255),
                        thickness=1)
                    logger.info("ES: Added: %s:%s BR: %s Rectangle: x: %s y: %s w: %s h: %s", pidx, sidx, border_ratio, x,y,w,h)
                    shape = {
                        'idx': sidx,
                        'origin': (x, y),
                        'bbox': (x,y,w,h),
                        'confidence': border_ratio/255,
                    }
                    found.append(shape)
                    sidx += 1
                    if markup_image is not None:
                        cv.rectangle(markup_image, (x, y), (x + w, y + h), (255, 255, 0), 1)
                else:
                    logger.info("ES: Dropped: S: %s  BR: %s Rectangle: coord: %s", pidx, border_ratio, (x,y,w,h))
                    if markup_image is not None:
                        cv.rectangle(markup_image, (x-border, y-border), (x + w + border, y + h + border), (255, 0, 255), 1)
                        cv.rectangle(markup_image, (x, y), (x + w, y + h), (0, 255, 255), 1)
                        cv.putText(img=markup_image, text=str(sidx),
                            org=(x+10, y+10), fontFace=font, fontScale=0.5, color=(0, 255, 255),
                            thickness=1)

    return {
        "images": {
            "markup": markup_image,
        },
        "data": {
            "shapes": found,
        }
    }

def process_box_templates(image: object, config: dict) -> dict:
    """
    the main runner for the template box processor, this weil be used for
    the selection of small key areas of the drawing, and then boxes are resonctructed.

    # Caveat:
    the detector should accomodate the misalignment of the key points, namely
    coreners not on the same h or v axis.  fThe point will be mapped to a internal grid,
    teh same size as the template

                    [2]                         [1]     [2]
    Point . [1]                 rather than
                        [3]                     [4]     [3]
                [4]

    parameters
    ----------
    image
        an BW image to be processed, single channel
    config
        threshold: (optional) double
            the threshold to use for the match
        threshold_border: (optional) double
            the border threshold to use for the match
        minsize : (optional) int the min size the return
        minh    : (optional) int the min height the return
        minw    : (optional) int the min width the return
        image   : (optional) an image for markup

    return:
    ------
    dict
        images: dict set of images
            "templates" the template markers
            "rectangles" the rectangle markers
        data:=
            "shapes": dict
    """

    targets, offsets = create_targets(size=10, bleed=1)
    vertices = [(1,2),(2,3),(4,3),(1,4)]
    threshold = config.get('threshold', 0.8) if config else 0.8
    border = config.get('border', 2) if config else 2
    threshold_border = config.get('threshold_border', 0.4) if config else 0.4
    minsize = config.get('minsize', 10) if config else 10
    minw = config.get('minh', minsize) if config else minsize
    minh = config.get('minh', minsize) if config else minsize
    markup_image = config.get("image")

    data = {
        "images": {},
        "data": {
            'shapes': []
        },
    }

    ft_config = {
        "targets": targets,
        "offsets": offsets,
        "threshold": threshold,
    }
    if markup_image is not None:
        ft_config['image'] = markup_image.copy()

    # find the target locations
    ft = find_targets(image=image, config=ft_config)
    for label, img_res in ft.get("images",{}).items():
        data['images'][f'FT.{label}'] = img_res

    # process the targets found into a set of rectangles
    gv_config = {
        'vertices': vertices,
        'expand': True,
    }

    gv = group_vertices(matrix=ft.get("matrix"), config=gv_config)

    es_config = {
        'threshold_border': threshold_border,
        'border': border,
        'shapes': gv.get('shapes'),
        'minw': minw,
        'minh': minh,
    }
    if markup_image is not None:
        es_config['image'] = markup_image.copy()

    es = extract_shapes(image=image, config=es_config)

    # save the images...
    for label, img_res in es.get("images",{}).items():
        data['images'][f'ES.{label}'] = img_res

    # save the shapes
    data['data']['shapes'] = es.get('data', {}).get('shapes',[])[:]

    return data

def process_box_contours(image: object, config: dict) -> dict:
    """
    the main runner for the contour box processor

    parameters
    ----------
    image
        a BW image to be processed, single channel
    config
        threshold   : (optional) double
            the threshold to use for the match
        minsize     : (optional) int the min size the return
        kernelsize  : (optional) int the min height the return
        step        : (optional) int the min width the return
        image       : (optional) an image for markup

    return:
    ------
    dict
        images: dict set of images
            "templates" the template markers
            "rectangles" the rectangle markers
        data:=
            "shapes": dict
                'origin': (x.y)
                'bbox': (x,y,w,h)
                'contours': list of contours contained
                'confidence': the confidence is is bounded rectangle
    """

    border = config.get('border', 2) if config else 2
    threshold_border = config.get('threshold_border', 0.4) if config else 0.4

    minsize =  config.get('minsize', 10) if config else 10
    minw = config.get('minh', minsize) if config else minsize
    minh = config.get('minh', minsize) if config else minsize
    markup_image = config.get("image")

    font = cv.FONT_HERSHEY_SIMPLEX

    data = {
        "images": {},
        "data": {
            'shapes': []
        },
    }

    # get the contours
    contours, _ = cv.findContours(image=image, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
    # draw the contours
    if markup_image is not None:
        # draw the contours
        contour_image = markup_image.copy()
        cv.drawContours(image=contour_image, contours=contours, contourIdx=-1, color=(0,0,255), thickness=1)
        data['images']['contours'] = contour_image

    found = []
    # quick segementation, too small and to large :)
    sidx = 0
    for cidx, c in enumerate(contours):
        # update the markup image
        (x,y,w,h) = cv.boundingRect(c)
        if h <= minh or w <= minw:
            continue

        # Now to test the pixel border
        pixels1 = image[y:y+h, x-border:x]
        pixels2 = image[y:y+h, x+w:x+w+border]
        pixels3 = image[y-border:y, x:x+w]
        pixels4 = image[y+h:y+h+border, x:x+w]
        pixsum = (pixels1.sum() + pixels2.sum() + pixels3.sum() + pixels4.sum())
        pixsize = (pixels1.size + pixels2.size + pixels3.size + pixels4.size)

        border_ratio =  pixsum / pixsize if pixsize > 0 else 255

        if border_ratio < (255 * threshold_border):
            if markup_image is not None:
                cv.circle(img=markup_image, center=(x, y), radius=5,color=(0,255,0), thickness=1)
                cv.putText(img=markup_image, text=str(sidx),
                    org=(x+10, y+10), fontFace=font, fontScale=0.5, color=(0, 0, 255),
                    thickness=1)

            logger.debug("PT: Added: %s BR:%s Rectangle: x: %s y: %s w: %s h: %s", cidx, border_ratio, x,y,w,h)
            shape = {
                'idx': sidx,
                'origin': (x, y),
                'bbox': (x,y,w,h),
                'contours': c,
                'confidence': border_ratio/255,
            }
            found.append(shape)
            sidx += 1
            if markup_image is not None:
                cv.rectangle(markup_image, (x, y), (x + w, y + h), (255, 255, 0), 1)
        else:
            logger.debug("PT: Dropped: %s BR: %s Rectangle: x: %s y: %s w: %s h: %s", cidx, border_ratio, x,y,w,h)
            if markup_image is not None:
                cv.circle(img=markup_image, center=(x, y), radius=5,color=(255, 0,255), thickness=1)
                cv.putText(img=markup_image, text=f'C:{cidx}',
                    org=(x+10, y+10), fontFace=font, fontScale=0.5, color=(255, 0, 255),
                    thickness=1)
                cv.rectangle(markup_image, (x-border, y-border), (x + w + border, y + h + border), (255, 0, 0), 1)
                cv.rectangle(markup_image, (x, y), (x + w, y + h), (0, 255, 0), 1)

    data['data']['shapes'] = found[:]


    # save the markup_image
    if markup_image is not None:
        data['images']['markup'] = markup_image

    return data
