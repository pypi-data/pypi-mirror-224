"""A test case for the path utils module"""
import logging
import unittest

import networkx as nx
from random import randrange, sample

from lost_cat_images.utils.utils_grids import (parse_grid_df, solve,
                    load_dataframe, extract_tables,
                    find_table_candidates, sort_table_candidates)

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler(f"logs/test_grids.log")
logger.addHandler(file_handler)

def build_table_graph(cols: int = 7, rows:int = 3,
                offset: int = 0, bidirection: bool = False
            ):
    """Build a simple fully connect set of coordinates
    for a table, of size cols x rows

    parameters
    ----------
    cols: int default 7
    rows: int default 3

    returns
    -------
    string: digraph
    """

    graph = nx.MultiDiGraph()

    edges = set()
    dirx = {'top': 'bottom', 'bottom': 'top', 'left': 'right', 'right': 'left'}
    n_grid = list(range(0,rows * cols))

    ridx = -1
    cidx = 0
    for i in n_grid:
        idx = i + offset
        # add the row to row connector
        # favour right and bottom :)
        if idx-cols >= 0 and bidirection is True:
            #edges.add(f'{i} -> {i-cols} [direction=top]')
            edges.add((idx,idx-cols,'top'))

        elif i+cols < (rows * cols):
            #edges.add(f'{i} -> {i+cols} [direction=bottom]')
            edges.add((idx,idx+cols,'bottom'))

            if bidirection is True:
                #edges.add(f'{i-cols} -> {i} [direction={dirx["bottom"]}]')
                edges.add((idx+cols,idx,dirx["bottom"]))

        if i % cols == 0:
            ridx += 1
            cidx = 0

            #edges.add(f'{i} -> {i+1} [direction=right]')
            edges.add((idx,idx+1,'right'))
            if bidirection is True:
                #edges.add(f'{i+1} -> {i} [direction={dirx["right"]}]')
                edges.add((idx,idx+1,dirx["right"]))

        elif i % cols == cols-1:
            cidx += 1

            #edges.add(f'{i-1} -> {i} [direction=right]')
            edges.add((idx-1,idx,'right'))
            if bidirection is True:
                #edges.add(f'{i} -> {i-1} [direction={dirx["right"]}]')
                edges.add((idx,idx-1,dirx["right"]))

        elif i % cols != 0:
            cidx += 1
            #edges.add(f'{i-1} -> {i} [direction=right]')
            edges.add((idx-1,idx,"right"))
            if bidirection is True:
                #edges.add(f'{i} -> {i-1} [direction={dirx["right"]}]')
                edges.add((idx,idx-1,dirx["right"]))
        else:
            logger.error("Whoa! INvalid state: Iterator: %s, Rows: %s  Cols: %s", i, rows, cols)

        # add to graph...
        graph.add_node(idx, idx=i, pos=(cidx, ridx))

    for edge in edges:
        nidx, ridx, dirn = edge
        graph.add_edge(nidx, ridx, direction=dirn)

    return graph

def build_samplegraphs() -> dict:
    """Build a set of graphs to test the code out"""
    #nx_graph = nx.nx_pydot.read_dot('source.gv')
    rows = 3
    cols = 3
    graphs = {
        f"Table({cols}, {rows})": build_table_graph(rows=rows, cols=cols)
    }

    # add right cell...
    tmp_gg = graphs.get(f"Table({cols}, {rows})").copy()
    tmp_gg.add_node(rows*cols,idx=rows*cols,pos=(rows,1))
    for ridx in range(rows):
        # for 3x3 => 2,5,8
        tmp_gg.add_edge((((ridx+1) * cols)-1), (rows*cols), direction='right')

    graphs[f"Table({cols}, {rows}+right)"] = tmp_gg

    # add left cell...
    tmp_gg = graphs.get(f"Table({cols}, {rows})").copy()
    tmp_gg.add_node(rows*cols,idx=rows*cols,pos=(0,0))
    for ridx in range(rows):
        # for 3x3 => 0, 3, 6
        tmp_gg.add_edge((ridx*cols), (rows*cols), direction='right')

    graphs[f"Table({cols}, {rows}+left)"] = tmp_gg

    # add a cell below the table...
    tmp_gg = graphs.get(f"Table({cols}, {rows})").copy()
    tmp_gg.add_node(rows*cols,idx=rows*cols,pos=(1,cols))
    for ridx in range(rows*(cols-1),rows*cols):
        # for 3x3 => 2,5,8
        tmp_gg.add_edge(ridx, (rows*cols), direction='bottom')

    graphs[f"Table({cols}, {rows}+bottom)"] = tmp_gg

    # add a cell below the table...
    tmp_gg = graphs.get(f"Table({cols}, {rows})").copy()
    tmp_gg.add_node(rows*cols,idx=rows*cols,pos=(1,cols))
    for ridx in range(rows):
        # for 3x3 => 2,5,8
        tmp_gg.add_edge((rows*cols), ridx, direction='bottom')

    graphs[f"Table({cols}, {rows}+top)"] = tmp_gg

    rows2 = 4
    cols2 = 4
    graph_2 = build_table_graph(rows=rows2,cols=cols2, offset=(rows*cols)+1)
    nx.get_edge_attributes(graph_2, 'direction')
    tmp_gg = nx.compose(graphs.get(f"Table({cols}, {rows}+bottom)"), build_table_graph(rows=4,cols=4, offset=(rows*cols)+1))
    for ridx in range((rows*cols)+1, (rows*cols)+cols2+1):
        tmp_gg.add_edge((rows*cols), ridx, direction='bottom')

    graphs[f"Table({cols}, {rows}+bottom)+Table({rows2}, {cols2})"] = tmp_gg

    return graphs

class TestGrids(unittest.TestCase):
    """A container class for the extract functions"""

    @classmethod
    def setUpClass(cls):
        """ Set up for Trie Unit Tests..."""
        #   0     1     2     3     4     5
        # 0 1-----------------------------.  .
        #   |  .  .  .  .  .  .  .  .  .  |  .
        # 1 |  .  7---------------------- |  .
        #   |  .  |  .  .  .  .  .  .  .  |  .
        # 2 |  .  2-----------3-----------|  .
        #   |  .  |  .  .  .  |  .  .  .  |  .
        # 3 |  .  |  .  .  .  4-----5-----|  .
        #   |  .  |  .  .  .  |  .  |  .  |  .
        # 4 |  .  |  .  .  .  6-----.  .  |
        #   |  .  |  .  .  .  |  .  |  .  |  .
        # 5 .---------------------------- .  .
        #   .  .  .  .  .  .  .  .  .  .  .  .

        cls.boxes = [
            {'idx': 1,   'x': 0, 'y': 0, 'w': 5, 'h': 5},
            {'idx': 2,   'x': 1, 'y': 2, 'w': 2, 'h': 3},
            {'idx': 2.1, 'x': 1, 'y': 2, 'w': 4, 'h': 3},
            {'idx': 3,   'x': 3, 'y': 2, 'w': 2, 'h': 1},
            {'idx': 3.1, 'x': 3, 'y': 2, 'w': 2, 'h': 3},
            {'idx': 4,   'x': 3, 'y': 3, 'w': 1, 'h': 1},
            {'idx': 4.1, 'x': 3, 'y': 3, 'w': 2, 'h': 2},
            {'idx': 4.2, 'x': 3, 'y': 3, 'w': 1, 'h': 2},
            {'idx': 5,   'x': 4, 'y': 3, 'w': 1, 'h': 2},
            {'idx': 6,   'x': 3, 'y': 4, 'w': 1, 'h': 1},
            {'idx': 7,   'x': 1, 'y': 1, 'w': 4, 'h': 1},
            {'idx': 7.1, 'x': 1, 'y': 1, 'w': 4, 'h': 4},
        ]

        cls.shapes = []
        # pivot to shapes
        for box in cls.boxes:
            x = box.get('x')
            y = box.get('y')
            w = box.get('w')
            h = box.get('h')
            shape = {
                'idx': box.get('idx'),
                'origin': (x, y),
                'bbox': (x, y, w, h),
            }
            cls.shapes.append(shape)

        cls.dfcols = ['idx', 'x', 'y', 'w', 'h', 'x_br', 'y_br']
        cls.graphs = build_samplegraphs()
        cls.graphs_asserts = {
            "Table(3, 3)": {
                "--":{
                    "type": "",
                    "value": None,
                    "message": ""
                }
            },
            "Table(3, 3+right)": {},
            "Table(3, 3+left)": {},
            "Table(3, 3+top)": {},
            "Table(3, 3+bottom)+Table(4, 4)": {}
        }

    @classmethod
    def tearDownClass(cls):
        """ Tear down for Trie Unit Tests"""
        pass

    def test_load_dataframe(self):
        """Text the simple case"""
        df = load_dataframe(shapes=self.shapes)

        # check the cols
        dfcols = df.columns
        self.assertCountEqual(dfcols, self.dfcols, 'Columns are incorrect')

        # check the rows are correct
        self.assertEqual(len(self.boxes), len(df.index), 'Inccorect number of rows')

    def test_solve(self):
        """Test teh gcd will return a value"""
        factor = randrange(100, 1000, 3)
        randomlist = sample(range(1, 30), 10)

        randomlist.append(1)

        gcdlist = [x * factor for x in randomlist]
        gcd = solve(gcdlist)

        self.assertEqual(gcd, factor, f'gcd is not working as expected {gcd} {factor} {gcdlist}')

    def test_parse_grid(self):
        """tests the parse grid fucntion works"""

        data = parse_grid_df(shapes=self.shapes)

        for key in ['gcd', 'shapes', 'grid']:
            self.assertIn(key, data, f'missing key {key}')

        # check the gcd
        for ngcd in ['x', 'y']:
            gcd = data.get('gcd',{}).get('x')
            self.assertEqual(gcd, 1, f'GCD is incorrect {gcd} for {ngcd}')

    def test_find_table_candidates(self):
        """ test the finder for a graph"""



    def test_sort_table_candidates(self):
        """ sorts the graph nodes into a table..."""

    def test_extract_tables(self):
        """ test the full graph table and grid extraction"""
        for label, graph in self.graphs.items():
            print(label)
            tables = extract_tables(graph=graph)
            print(tables)