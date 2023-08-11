import logging
import collections
import cv2 as cv
import networkx as nx
import numpy as np
from math import gcd
import pandas as pd

from lost_cat_images.utils.utils_shapes import Rectangle, ShapeGrouper
from lost_cat_images.utils.utils_words import map_shape_text

logger = logging.getLogger(__name__)

def closest_node(node, nodes):
    """Closest node calculates the distance from
    point

    parameters
    ----------
    node: the current node point
    nodes: a list of points

    returns
    -------
    list: the node coords and the distance squared
    """
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node)**2, axis=1)
    return zip(nodes, dist_2)

def solve(nums):
    """ Will determine the gcd for a list of numbers
    https://www.tutorialspoint.com/program-to-find-highest-common-factor-of-a-list-of-elements-in-python

    paramters
    ---------
    nums: list of numbers
        the list of number to calculate the gcd from

    returns
    -------
    number: the gcd
    """

    if len(nums) == 1:
        return nums[0]

    div = gcd(nums[0], nums[1])

    if len(nums) == 2:
        return div

    for i in range(1, len(nums) - 1):
        div = gcd(div, nums[i + 1])
        if div == 1:
            return div

    return div

def load_dataframe(shapes: list) -> pd.DataFrame:
    """ take a list of shapes, a shape must have:

    parameters
    ----------
    shapes: list of shapes
        'idx'   : index for the shape
        'origin': (x,y)
        'bbox'  : (x,y,w,h)

    returns
    -------
    Dataframe
        cols: idx, x,y,w,h,ybr,xbr
    """
    cols = ['x', 'y', 'w', 'h']
    rows = []
    for shape in shapes:
        x,y,w,h = shape.get('bbox')
        row = {
            'idx': shape.get('idx'),
            'x': x,
            'y': y,
            'w': w,
            'h': h,
        }
        rows.append(row)

    df_rect = pd.DataFrame(rows)

    # fix the col types
    for col in cols:
        df_rect[col] = df_rect[col].astype(int)

    # add the br corner x, y
    df_rect['x_br'] = df_rect['x'] + df_rect['w']
    df_rect['y_br'] = df_rect['y'] + df_rect['h']

    return df_rect

def parse_grid_df(shapes: list) -> dict:
    """ will generate a a grid that matches the
    provided shapes.

    parameters:
    -----------
    shapes: list of shapes
        'idx'   : index for the shape
        'origin': (x,y)
        'bbox'  : (x,y,w,h)

    returns
    -------
    dict:
        'gcd': dict
            'x': the gcd for the x axis
            'y': the gcd for the y axis
        'grid': dict
            (c1,r1):
                'bbox': (x,y,w,h)
                'r1c1'  : (i,j) the grid coordinates
                'width' : int  the merge width
                'height': int the merge height
                'type'  :string of  [column, row, cell, table]
                'right' : list of connecting gridref to the right
                'bottom': list of connecting gridref to the bottom
        'shapes': list
            a grid structure withe text embened
            'origin': (x.y)
            'bbox': (x,y,w,h)
            'contours': list of contours contained
            'text': the text in the cell
            'confidence': the confidence of the text
            'gridref': (c1,r1) the grid reference for the shape
    """
    df_rect = load_dataframe(shapes=shapes)

    # get teh w and h gcd
    w_sizes = pd.unique(df_rect[['w']].values.ravel('K'))
    w_gcd = solve(w_sizes)
    h_sizes = pd.unique(df_rect[['h']].values.ravel('K'))
    h_gcd = solve(h_sizes)

    data = {
        'gcd': {
            'x': w_gcd,
            'y': h_gcd
        },
        'grid': {},
        'shapes': [],
    }

    # find connecting rects
    # look in both x and y directions...conty
    # we have the list sorted by
    for index, row in df_rect.iterrows():
        logger.debug('----\n%s %s', index, row.values)
        # look for contained rectangles
        df_cont = df_rect[
            (df_rect['x'] >= row['x']) &
            (df_rect['x'] <= row['x']+row['w']) &
            (df_rect['x_br'] >= row['x']) &
            (df_rect['x_br'] <= row['x']+row['w']) &
            (df_rect['y'] >= row['y']) &
            (df_rect['y'] <= row['y']+row['h']) &
            (df_rect['y_br'] >= row['y']) &
            (df_rect['y_br'] <= row['y']+row['h']) &
            (df_rect['idx'] != row['idx'])
        ]
        if not df_cont.empty:
            logger.debug('=>\tCont: %s', df_cont.values)

        # is there a rectangle that start on the same x+w or y+h
        df_xc = df_rect[(df_rect['x'] >= row['x']) &
                    (df_rect['x'] <= row['x_br']) &
                    (df_rect['y'] == row['y_br']) &
                    (df_rect['idx'] != row['idx'])]
        if not df_xc.empty:
            logger.debug('=>\tX tl: %s', df_xc.values)

        df_yc = df_rect[(df_rect['y'] >= row['y']) &
                    (df_rect['y'] <= row['y_br']) &
                    (df_rect['x'] == row['x_br']) &
                    (df_rect['idx'] != row['idx'])]
        if not df_yc.empty:
            logger.debug('=>\tY tl: %s', df_yc.values)

        df_xbr = df_rect[(df_rect['x_br'] >= row['x']) &
                        (df_rect['x_br'] <= row['x_br']) &
                        (df_rect['y_br'] == row['y_br']) &
                        (df_rect['idx'] != row['idx'])]
        if not df_xbr.empty:
            logger.debug('=>\tX br %s:', df_xbr.values)

        df_ybr = df_rect[(df_rect['y_br'] >= row['y']) &
                        (df_rect['y_br'] <= row['y_br']) &
                        (df_rect['x_br'] == row['x_br']) &
                        (df_rect['idx'] != row['idx'])]
        if not df_ybr.empty:
            logger.debug('=>\tY br: %s', df_ybr.values)

        # process look for containers that are either the same width as there containing cells
        # and x,y coordinates align correctly...


    # return and close
    return data

def find_cells(shape: dict, shapes:list, pts_topleft:dict, band:int = 10):
    """ using the provided shape this will scn the pts-topleft for close
    boxes.  for Each close box it'll cehck for sonnecting edges.

    parameters
    ----------
    shape: dict

    shapes: list of shapes
    pts_topleft: dict
        key: (x,y)
        value: list of shapes at this point
    band: int
        the boundary to include points candidates

    returns:

    """
    # pts_close, a set of x,y ppints to find matching shapes
    pts_close = []
    idx = shape.get('idx')
    x,y,w,h = shape.get('bbox')

    for xi in range(int(x-band), int(x+w)):
        for yi in range(int(y+h-band), int(y+h+band)):
            if (xi,yi) == (x,y):
                continue

            if (xi,yi) in pts_topleft:
                pts_close.append((xi, yi, 'bottom'))

        # right aligned
    for yi in range(int(y-band), int(y+h)):
        for xi in range(int(x+w-band), int(x+w+band)):
            if (xi,yi) == (x,y):
                continue

            if (xi,yi) in pts_topleft:
                pts_close.append((xi, yi, 'right'))

        # now to look for connected edges...
    for test_shp in shapes:
        tidx = test_shp.get("idx")
        if idx == tidx:
            continue

        tx, ty, tw, th = test_shp.get("bbox")
        if (tx, ty) in pts_close:
            continue

            # break if connected by corner only...
            # TL: X,Y
            # TR: x+w, y
            # BL: x, y+h
            # BR: x+w, y+h

        #logger.debug('S:   %s => %s', idx, shape.get('bbox'))
        #logger.debug('  T: %s => %s', tidx, test_shp.get('bbox'))

        # TL <=> BR: x,     y     ~= tx + tw, ty + th
        # TR <=> BL: x,     y + h ~= tx,      ty + th
        # BL <=> TR: x + w, y     ~= tx + tw, ty
        # BR <=> TL: X + W, y + h ~= tx     , ty
        dis_matrix = [
                [ x      - (tx + tw),  y      - (ty + th)],
                [(x + w) -  tx,        y      - (ty + th)],
                [ x      - (tx + tw), (y + h) -  ty],
                [(x + w) -  tx,       (y + h) -  ty],
            ]
        in_zone = False
        for pt_x, pt_y in dis_matrix:
            if (-band <= pt_x <= band) and (-band <= pt_y <= band):
                in_zone = True
                break
        if in_zone:
            continue

            # perform the tests...
            # check bottom to top side...
        if (y + h - band) < ty <  (y + h + band) and (
                    (x + w - band) < tx        <  (x + w + band) or # top edge is within range
                    (x + w - band) < (tx + tw) <  (x + w + band) or
                    (tx - band)    < x         <  (tx + tw + band) or # top edge is within range
                    (tx - band)    < (x + w)   <  (tx + tw + band)
                ):
            pts_close.append((tx, ty, 'bottom'))
            continue

            # check the left to right side...
        if (x + w - band) < tx <  (x + w + band) and (
                    (y + h - band) < ty        <  (y + h + band) or # top edge is within range
                    (y + h - band) < (ty + th) <  (y + h + band) or
                    (ty - band)    < y         <  (ty + th + band) or # top edge is within range
                    (ty - band)    < (y + h)   <  (ty + th + band)
                ):
            pts_close.append((tx, ty, 'right'))
            continue

            # check for above...
        if (ty + th - band) < y <  (ty + th + band) and (
                    (tx + tw - band) < x       <  (tx + tw + band) or # top edge is within range
                    (tx + tw - band) < (x + w) <  (tx + tw + band) or
                    (x - band)    < tx         <  (x + w + band) or # top edge is within range
                    (x - band)    < (tx + tw)  <  (x + w + band)
                ):
            pts_close.append((tx, ty, 'top'))
            continue

            # check to the left...
        if (tx + tw - band) < x <  (tx + tw + band) and (
                    (ty + th - band) < y       <  (ty + th + band) or # top edge is within range
                    (ty + th - band) < (y + h) <  (ty + th + band) or
                    (y - band)    < ty         <  (y + h + band) or # top edge is within range
                    (y - band)    < (ty + th)  <  (y + h + band)
                ):
            pts_close.append((tx, ty, 'left'))
            continue

    return pts_close

def produce_grids(image: np.array = None, graph: nx.Graph = None, minpath: int = 0) -> dict:
    """break the graph in seperate connected graphs

    parameters
    ----------
        image: np.array
            an image to use to generate the markup
        graph: nx.Graph
            the graph of the boxes and shapes
        minpath: int
            the filter for the graph paths

    returns
    -------
    dict:
        images: dict
            markup: np.array
                image iwth markup
        data
            subgraphs: nx.Graph
                the graph starting fomr the top left cell
    """
    center_graphs = {}

    img_res = image.copy()
    conn_subs = [graph.subgraph(c).copy() for c in nx.strongly_connected_components(graph) if len(c) > minpath] #

    for gsidx, g_sub in enumerate(conn_subs):
        sg = ShapeGrouper()

        for nidx, bbox in nx.get_node_attributes(g_sub, 'bbox').items():
            x,y,w,h = bbox

            rect = Rectangle(x=x, y=y, w=w, h=h)
            rect.add_tags(**{
                'idx': nidx
            })
            sg.add_rectangle(rect=rect)

            cv.rectangle(img=img_res, rec=(x,y,w,h), color=(255, 0 ,0), thickness=1)
            cv.circle(img=img_res, center=(x,y), radius=5,
                            color=(255,0,0), thickness=1)

        cg = nx.MultiDiGraph()
        root_rect = sg.shapes.get('shape')
        bbx, bby, bbw, bbh = root_rect.bbox()
        for shape in sg.shapes.get("children",[]):
            # create a center point graph...
            rect = shape.get('shape')
            rx, ry, rw, rh = rect.bbox()
            c_pt = (rx + int(rw/2), ry + int(rh/2))
            cloc_pt = (rx - bbx + int(rw/2), ry - bby + int(rh/2))
            cg.add_node(nidx, pos=cloc_pt, bbox=rect.bbox())

            cv.circle(img=img_res, center=c_pt, radius=5,
                            color=(255,0,0), thickness=1)

            cv.putText(img=img_res, text=f'{gsidx}.{rect.idx}',
                    org=(rx + int(rw/2)+10, ry + int(rh/2)),
                    fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5, color=(255,0,0), thickness=1)

            # plot to grid...
            cv.rectangle(img=img_res, rec=rect.bbox(), color=(0, 255, 0), thickness=2)

        # add the grouping rectangle
        cv.rectangle(img=img_res, rec=(bbx, bby, bbw, bbh), color=(0, 0, 255), thickness=2)

        # add the edges from the original graph
        cg.add_edges_from(g_sub.edges.data())

        center_graphs[gsidx] = cg.copy()

    return {
        "images": {
            "markup": img_res
        },
        "data": {
            "subgraphs":center_graphs
        }
    }

def process_grids(image: object, config: dict) -> dict:
    """Will process the shape objects and
    try to determine the following information:

    parameters
    ----------

    returns
    -------
    dict:
        'images': dict
            'candidates':
                image markuped with groups and shapes
            'groups':
                image markuped with graph joins
        'data': dict
            'shapes':
                list of shapes
            'graph':
                the graph of the shapes
            'grids':
                the found grids
            'tables':
                the table details
            'mapping':
                the mapping of shapes to text
    """
    rev_dir = {'top': 'bottom', 'bottom': 'top', 'left': 'right', 'right': 'left'}

    minpath = config.get('minpath', 4) if config else 4
    band = config.get('band', 10) if config else 10
    shapes = config.get('shapes', []) if config else []
    word_data = config.get('texts', {}) if config else {}

    img_blnk = np.zeros(image.shape, np.uint8)
    img_blnk.fill(255)

    full_graph = nx.MultiDiGraph()

    pts_topleft = {}

    logger.debug("WD: Type: %s Len: %s", type(word_data),len(word_data))
    for label, data_value in word_data.items():
        logger.debug('%s Type: %s, Len: %s', label, type(data_value), len(data_value))
    shape_mapping = map_shape_text(shapes=shapes, word_data=word_data)

    # get the top left corner for the shape
    logger.debug("=== Shapes:")
    for shape in shapes:
        x,y,w,h = shape.get("bbox")
        if (x,y) not in pts_topleft:
            pts_topleft[(x,y)] = []
        pts_topleft[(x,y)].append(shape)

        logger.debug("I: %s", shape.get("idx"))
        logger.debug("O: %s", shape.get("bbox"))

    # process the shapes to prepare for the
    # build lookup based on top left point
    shape_dict = {}
    for shape in shapes:
        idx = shape.get('idx')
        x,y,w,h = shape.get("bbox")
        cpt = (int(w/2)+x, int(h/2)+y)

        # build the phrase and add to the shape list
        phrase = ""
        if p_list := shape_mapping.get(idx,{}).get('phrases',[]):
            if len(p_list) == 0:
                phrase = word_data.get('phrases', {}).get(p_list[-1])
            else:
                items = [v for k, v in word_data.get('phrases', {}).items() if k in p_list]
                bboxes = [v['bbox'] for k, v in word_data.get('phrases', {}).items() if k in p_list]
                arr = np.array([(x+int(w/2), y+int(h/2)) for x,y,w,h in bboxes])
                r = (arr[:, 1]**2 + arr[:, 0]**2)
                parts = []
                for iidx in np.argsort(r):
                    parts.append(items[iidx].get('text'))
                phrase = ' '.join(parts)

        shape['phrase'] = phrase

        shape_dict[idx] = {
            "bbox": shape.get("bbox"),
            "phrase": phrase
        }

        # a list of linked components...
        # tuple = {x, y, s} s: side top|bottom|left|right
        pts_close = find_cells(shape=shape, shapes=shapes, pts_topleft=pts_topleft, band=band)

        # add the vericies and edges
        if len(pts_close) > 0:
            #logger.debug("Close: %s", pts_close)
            full_graph.add_node(shape.get('idx'), pos=(x,y),
                                bbox=shape.get("bbox"),
                                top_left=(x,y), bot_right=(x+w, y+h),
                                phrase=phrase)

            logger.debug("I: %s", shape.get("idx"))
            logger.debug("O: %s", shape.get("bbox"))
            logger.debug("C: %s", set(pts_close))

            # print Shape
            cv.rectangle(img=img_blnk, rec=(x,y,w,h), color=(255, 0 ,0), thickness=1)
            cv.circle(img=img_blnk, center=(int(x + w/2), int(y+h/2)), radius=5, color=(0,0,255), thickness=1)
            for (pt_x, pt_y, pt_dir) in pts_close:
                for link_shape in pts_topleft.get((pt_x, pt_y),[]):
                    # add the child nodes and edges between them
                    lidx = link_shape.get("idx")
                    lx ,ly, lw, lh = link_shape.get("bbox")

                    # check for bottom right and topleft cases...
                    if (-band < (x + w - lx) < band) and (-band < (y + h - ly) < band):
                        logger.debug('idx: %s br: %s => lidx: %s tl: %s D: %s SKIPPING',
                                    idx, (x+w, y+h), lidx, (lx, ly), [(x + w - lx), (y + h - ly)])
                        continue

                    if not full_graph.has_node(lidx):
                        logger.debug("Node: IDX: %s BB: %s", lidx, link_shape.get("bbox"))
                        full_graph.add_node(lidx, pos=(pt_x, pt_y), bbox=link_shape.get("bbox"),
                                            top_left=(lx,ly), link_shape=(lx+lw, ly+lh))

                    # check for edge exists...
                    if not full_graph.has_edge(idx, lidx):
                        logger.debug("Edge: IDX: %s <-> LIDX: %s (%s)", idx, lidx, pt_dir)
                        full_graph.add_edge(idx, lidx, direction=pt_dir)
                        full_graph.add_edge(lidx, idx, direction=rev_dir.get(pt_dir))

                    cv.rectangle(img=img_blnk, rec=(lx ,ly, lw, lh), color=(255, 0, 255), thickness=1)
                    cv.line(img=img_blnk, pt1=cpt, pt2=(int(lw/2)+lx, int(lh/2)+ly), color=(0,255,0), thickness=1)

                cv.rectangle(img=img_blnk, rec=(pt_x, pt_y, 5 , 5), color=(0, 0, 255), thickness=1)

    # propcess the sub graphs
    img_netx = np.zeros(image.shape, np.uint8)
    img_netx.fill(255)
    grid_data = produce_grids(image=img_netx, graph=full_graph)
    tables = {}

    # now we need to take the grids and work out tables and grids from them
    for gidx, sub_graph in grid_data.get("data", {}).get("subgraphs", {}).items():
        # have a graph...
        candidates = find_table_candidates(graph=sub_graph)
        for tidx, t_data in sort_table_candidates(table_candidates=candidates).items():
            # map the found shapes to the table...
            rows = t_data.get("rows", [])
            ex_rows = []
            for row in rows:
                row_nodes = []
                for nidx in row:
                    row_nodes.append({
                        "idx": nidx,
                        "phrase": shape_dict.get(nidx,{}).get("phrase"),
                        "bbox": shape_dict.get(nidx,{}).get("bbox")
                    })
                ex_rows.append(row_nodes)

            tables[tidx] = {
                "seq": t_data.get("seq", []),
                "rows": ex_rows
            }

    return {
        'images': {
            'candidates': img_blnk,
            'groups': grid_data.get("images", {}).get("markup"),
        },
        'data': {
            'shapes': shapes,
            'graph': full_graph,
            'grids': grid_data.get("data", {}).get("subgraphs", {}),
            'tables': tables,
            'mapping': shape_mapping,
        }
    }

def find_table_candidates(graph: nx.Graph) -> list:
    """Will scan the graph and return a list of nodes
    that have one edge in the right or bottom direction,
    remove cells that are connected to multiple cells...

    parameters
    ----------
    graph: nx.graph

    returns
    -------
    list: tuple
        a list of tuples
        (node, right node, bottom node)
    """
    # find cells that have only one right or left connection
    table_candidates = []
    nodes = {}
    enc = [] # the nodeidx encountered, each node should only be seen once...

    for node, degree in graph.degree():
        node_dir = {}
        for (nodi, nodc, attribs) in  graph.edges(node, data=True):
            for attr_key, attr_val in attribs.items():
                if attr_key == 'direction':
                    if attr_val not in node_dir:
                        node_dir[attr_val] = []
                    node_dir[attr_val].append((nodc))

        nodes_r = node_dir.get('right',[])
        nodes_b = node_dir.get('bottom',[])
        nodes[node] = {
            "degree": degree,
            "right": nodes_r,
            "bottom": nodes_b
        }
        enc.append(node)
        enc.extend(nodes_r)
        enc.extend(nodes_b)

    logger.debug("Nodes: %s", nodes)
    logger.debug("Enc: %s", sorted(enc))
    counter = collections.Counter(enc)
    exclude = [node for node, count in counter.items() if count > 3]
    logger.debug("EX: %s", exclude)

    for node, data in nodes.items():
        if node in exclude:
            continue

        nodes_r = [node for node in data.get("right",[]) if node not in exclude]
        nodes_b = [node for node in data.get("bottom",[]) if node not in exclude]

        logger.debug("FTC: C: %s R: %s B: %s", node, nodes_r, nodes_b)
        if (len(nodes_r) == 1 or len(nodes_b) == 1) and (len(nodes_r) <= 1 and len(nodes_b) <= 1):
            node_r = nodes_r[0] if len(nodes_r) == 1 else None
            node_b = nodes_b[0] if len(nodes_b) == 1 else None
            table_candidates.append((node, node_r, node_b))

    logger.info('FTC: %s', table_candidates)
    return table_candidates

def sort_table_candidates(table_candidates: list) -> list:
    """Will scan the graph and return a list of nodes
    that have one edge in the right or bottom direction

    parameters
    ----------
    graph: nx.graph

    returns
    -------
    list: tuple
        a list of tuples
        (node, right node, bottom node)
    """
    row_set = []
    col_set = []
    for (node, node_r, node_b) in table_candidates:
        # make this greedy, if the cell is also connected to
        # another single cell to the right or bottom, add it
        logger.debug("Cell: N: %s R: %s B: %s", node, node_r, node_b)
        if node_r:
            is_row = False
            for row in row_set:
                #logger.debug("ROW: %s", row)
                if node_r == row[0]:
                    row[:0] = [node]
                    is_row = True
                    logger.debug("R: -- %s %s %s %s", node, node_r, is_row, row)
                    break
                elif node == row[-1]:
                    row.append(node_r)
                    is_row = True
                    logger.debug("R: ++ %s %s %s %s", node, node_r, is_row, row)
                    break
                elif node in row or node_r in row:
                    is_row = True
                    logger.debug("R: == %s %s %s %s", node, node_r, is_row, row)
                    break
                #else:
                #    logger.warning("R: ## %s == %s | %s == %s", node_r, row[0], node, row[-1])

            if not is_row:
                row_set.append([node, node_r])
                logger.debug("R: >> %s %s %s %s", node, node_r, is_row, [node, node_r])
        else:
            row_set.append([node])
            logger.debug("R: ~~ %s %s %s", node, node_r, [node])

        if node_b:
            is_col = False
            for col in col_set:
                if len(col) == 0:
                    continue

                if node_b == col[0]:
                    col[:0] = [node]
                    is_col = True
                    logger.debug("C: -- %s %s %s %s", node, node_b, is_col, col)
                    break

                elif node == col[-1]:
                    col.append(node_b)
                    is_col = True
                    logger.debug("C: ++ %s %s %s %s", node, node_b, is_col, col)
                    break
                elif node in col or node_b in col:
                    is_col = True
                    logger.debug("C: == %s %s %s %s", node, node_b, is_col, col)
                    break

            if not is_col:
                col_set.append([node, node_b])
                logger.debug("C: >> %s %s %s %s", node, node_b, is_col, [node, node_b])
        else:
            col_set.append([node])
            logger.debug("C: ~~ %s %s %s", node, node_b, [node])

        logger.debug("-\tRS: %s", row_set)
        logger.debug("-\tCS: %s", col_set)

    # now we have row_set and col_set...
    # operations:
    #   match top left row and cols
    #   merge orphan rows / cols
    # we now need to consolidate the rows and columns...
    ex_rows = {}
    for row in row_set:
        curr_row = row[:]
        node_f = row[0]
        node_l = row[-1]
        for test in row_set:
            if node_l == test[0]:
                # we have a matching ling
                if len(test) > 1:
                    curr_row.extend(test[1:])
                    node_l = curr_row[-1]
                test = []
            elif node_f == test[-1]:
                if len(test) > 1:
                    curr_row[:0] = test[:-1]
                test = []
        row = []
        if curr_row[0] not in ex_rows:
            ex_rows[curr_row[0]] = curr_row

    for ridx, row in ex_rows.items():
        logger.debug("ER: %s -> %s", ridx, row)

    ex_cols = {}
    for col in col_set:
        curr_col = col[:]
        node_f = col[0]
        node_l = col[-1]
        for test in col_set:
            if node_l == test[0]:
                # we have a matching ling
                if len(test) > 1:
                    curr_col.extend(test[1:])
                    node_l = curr_col[-1]
                test = []
            elif node_f == test[-1]:
                if len(test) > 1:
                    curr_col[:0] = test[:-1]
                test = []
        col = []
        if curr_col[0] not in ex_cols:
            ex_cols[curr_col[0]] = curr_col

    for cidx, col in ex_cols.items():
        logger.debug("EC: %s -> %s", cidx, col)

    tables = {}

    for cidx, col in ex_cols.items():
        if cidx in ex_rows:
            # we have a table candidate...
            row_len = len(ex_rows.get(cidx, []))
            seq = []
            tbl = []
            for ridx in col:
                if len(ex_rows.get(ridx, [])) == row_len:
                    seq.append(ridx)
                    tbl.append(ex_rows.get(ridx, []))
            tables[cidx] = {
                "rows": tbl,
                "seq": seq
            }

    for idx, value in tables.items():
        logger.info("TL: %s", idx)
        logger.debug("\tSeq: %s", value.get("seq", []))
        for ridx, row in enumerate(value.get("rows",[])):
            logger.debug("%s\t: %s", ridx, row)

    return tables


def fetch_cells(cells: list, dir: str, graph: nx.Graph) -> list:
    """Returns the cells specified by the cidexes and dir from the
    graph, will only return it the cell dimensions match

    parameters
    ----------
    cells: list
        idx: int
        phrase: str
        bbox: tuple x,y,w,h
    dir: str b,t,l,r
    graph: nx.graph

    returns
    -------
    list:
        idx: int
        phrase: str
        bbox: tuple x,y,w,h

        src_cols: list of str
    """
    header_nodes = []
    idxes = [key['idx'] for key in cells]
    if dir.lower() == "t":
        dims = [key['bbox'][2] for key in cells]
        attrib = "top"
    elif dir.lower() == "l":
        dims = [key['bbox'][3] for key in cells]
        attrib = "right"
    elif dir.lower() == "r":
        dims = [key['bbox'][3] for key in cells]
        attrib = "left"
    else: # assume 'b'
        dims = [key['bbox'][2] for key in cells]
        attrib = "bottom"

    logger.info("FC: IDX: %s", idxes)
    logger.info("FC: Dir: %s Att: %s Dims: %s", dir, attrib, dims)

    # get the edges from the graph...
    nodes = [(u,v) for u,v,e in graph.edges(data=True) if e['direction'] == attrib]
    links = {l:r for l,r in nodes if l in idxes}
    h_graph = graph.subgraph([r for l,r in nodes if l in idxes])
    logger.info("Re: %s", nodes)
    logger.info("Lk: %s", links)
    logger.info("HG: %s", h_graph)

    if len(links) == len(idxes) and len(h_graph) == len(idxes):
        bboxes = {x:{"bbox":y.get('bbox'), "phrase": y.get('phrase', '')} for x,y in h_graph.nodes(data=True)}
        logger.info("BB: %s", bboxes)

        for idx in idxes:
            logger.debug("HN: IDX: %s Link: %s Key: %s", idx,  links.get(idx,'-'), bboxes.get(links.get(idx,'-'),{}).get('phrase',str(idx)))
            header_nodes.append(bboxes.get(links.get(idx,'-'),{}).get('phrase',str(idx)).lower())

    return header_nodes


def extract_tables(image: object, config: dict = None) -> dict:
    """Will take the table information and export the data,
    it will check for the header row, and if present will convert
    to a dataframe.
    If the header row is missing, it will use the table_rules data
    to determine the way to process.

    config:
        tables:
            top left idx
            seq: sequence of rows
            rows: list of list
                idx: int
                phrase: str
                bbox: x,y,w,h
        graph: networkx graph
            used to expand the table if the header row is
            missing
        rules:
            cols: list of column names
            dir: str the direction the table is
                B bottom to top
                T top to bottom
                L left to right
                R right to left
            mapping: dict
                a set of rules to convert the data
                to metadata tags
                    i.e. date = col[Y] & col[M] & col[D]
                    {
                        'operation': 'concat'
                        'cols': ['Y', 'M', 'D']
                        'tag': date
                    }
            export: str the row to export
                TOP, BOTTOM, LEFT, RIGHT
            header: graph | contained
    """

    # INFO:lost_cat_images.utils.utils_grids:TL: 84
    #   Seq: [int, int, ...]
    #   Rows: list of list
    #       [{}, {}, ...]
    #       [{}, {}, ...]
    #       [...]
    #       each cell is
    #           idx: int
    #           bbox: tuple x,y,w,h
    #           phrase: str
    data = {
        "exports": {},
        "tables": []
    }
    graph = config.get("graph")

    for tidx, tb_data in config.get("tables",{}).items():
        # find if a rule matches
        width = len(tb_data.get("seq", []))
        depth = len(tb_data.get("rows", [])[0]) if len(tb_data.get("rows", [])) > 0 else 0

        logger.info("T: %s W: %s D: %s Data: %s", tidx, width, depth, tb_data)

        # skip small tables:
        if width <= 2 and depth <= 1:
            continue

        matching_rules = []
        for rule in config.get("rules", []):
            logger.debug("RH: %s", rule.get("cols"))
            if len(rule.get("cols", [])) == depth:
                matching_rules.append(rule)

        df = None
        # do we have a rule set to apply...
        if len(matching_rules) > 0:
            # can the rule be applied?
            for rule in matching_rules:
                logger.debug("Rule: %s", rule)
                skip_first = False
                dir = rule.get("dir","B").lower()
                header = rule.get("header","graph")
                labels = {}
                cells = []
                if dir == "b":
                    cells = tb_data.get("rows", [])[-1][:]
                elif dir == "t":
                    cells = tb_data.get("rows", [])[1][:]
                elif dir == "l":
                    cells = [i[0] for i in tb_data.get("rows", [])]
                elif dir == "r":
                    cells = [i[-1] for i in tb_data.get("rows", [])]
                else:
                    # default
                    cells = tb_data.get("rows", [])[-1][:]

                # get the header if external
                if header.lower() == "graph":
                    # get the connected cells from the hidxes
                    src_cols = fetch_cells(cells=cells, dir=dir, graph=graph)
                    if len(src_cols) == 0:
                        skip_first = True
                        src_cols = [key['phrase'].lower() for key in cells]

                    labels = {k:{"tag":k,"cols":[k]} for k in src_cols}
                else:
                    # header should be in the table...
                    # get the mapping for the columns...
                    src_cols = [key['phrase'].lower() for key in cells.items()]
                    # apply the mapping if any...
                    for map in rule.get("mapping", []):
                        # cols: list
                        # tag: str
                        # [operation: str]
                        # [format: str]
                        tag = map.get("tag")
                        labels[tag] = map

                # check the cols match..
                if rule.get("cols",[]) != src_cols:
                    # mismathc
                    logger.warning("Not matching...%s -> %s", rule.get("cols",[]), src_cols)
                    continue

                # now build the dataframe...
                rows = []
                for row in tb_data.get("rows", []):
                    record = {}
                    for idx, tag in enumerate(list(labels.keys())):
                        record[tag] = row[idx].get("phrase")
                    rows.append(record)

                # we have a
                logger.info("MR: %s Rows: %s", rule, rows)
                df = pd.DataFrame(rows)
                if df.shape[0] >= 2 and skip_first is True:
                    df.drop(index=df.index[0])

                if df.shape[0] >= 2:
                    data["tables"].append(df.copy())

                # get the top populated row...
                if len(rows) > 0:
                    for k,v in rows[-1].items():
                        data['exports'][k] = v
                break

        if not isinstance(df, pd.DataFrame):
            # export the table to a dataframe...
            # check to see if the surrounding cells are
            # the same width (top , bottom) or height (left, right)
            # use these cell if any as the columns for the table
            skip_first = False
            cells = tb_data.get("rows", [])[-1][:]
            src_cols = fetch_cells(cells=cells, dir='b', graph=graph)
            if len(src_cols) == 0:
                skip_first = True
                src_cols = [key['phrase'].lower() for key in cells]

            # fix missing values here if any
            for idx, value in enumerate(src_cols[:]):
                if value == '':
                    src_cols[idx] = str(idx)

            labels = {k:{"tag":k,"cols":[k]} for k in src_cols}
            rows = []
            src_rows = reversed(tb_data.get("rows", []))
            logger.info("SR: %s", src_rows)
            for row in src_rows:
                if all('' == s or s.isspace() for s in [key['phrase'] for key in row]):
                    continue

                record = {}
                for idx, tag in enumerate(list(labels.keys())):
                    record[tag] = row[idx].get("phrase")
                logger.debug("RR: %s", record)
                rows.append(record)

            # we have a
            logger.info("DF: Rows: %s", rows)
            df = pd.DataFrame(rows)
            if df.shape[0] >= 2 and skip_first is True:
                df.drop(index=df.index[0])

            if df.shape[0] >= 1:
                data["tables"].append(df.copy())

            # get the top populated row...
            if len(rows) > 0:
                for k,v in rows[-1].items():
                    data['exports'][k] = v

    return {
        "images": {},
        "data": data
    }
