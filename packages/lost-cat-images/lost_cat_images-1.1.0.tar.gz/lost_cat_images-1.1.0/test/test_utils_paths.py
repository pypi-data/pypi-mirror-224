"""A test case for the path utils module"""
import logging
import unittest

from lost_cat_images.utils.utils_nodepaths import PathNode, PathNodeTree

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler("logs/test_pathnode.log")
logger.addHandler(file_handler)

class TestPathNode(unittest.TestCase):
    """A container class for the node path module test cases"""

    def test_pathnode(self):
        """test the node path elements"""
        points = [
            (1,1),
            (1,2),
            (2,2),
            (2,1)
        ]

        node = PathNode(point=points[0])

        self.assertEqual(node.point, points[0], 'Ppints are not equal')

    def test_pathnodetree(self):
        """Test the path tree"""
        pt = (306, 255)
        d_1 = [(1504, 255), (2704, 255), (3904, 255), (6304, 255), (7504, 255), (8704, 255), (9904, 255)]
        d_2 = [(1504, 481), (1504, 6253), (2704, 481), (2704, 6253), (3904, 481), (3904, 6253), (6304, 481), (6304, 6253), (7504, 481), (7504, 6253), (8704, 481), (8704, 6253), (9904, 6253), (9904, 5253), (9904, 4253), (9904, 2253), (9904, 1253)]
        d_3 = [(306, 1253), (306, 2253), (306, 4253), (306, 5253), (306, 6253)]

        tree = PathNodeTree()
        a_node = PathNode(pt)
        tree.head = a_node

        for pt_d in d_1:
            logger.info('1 Point: %s', pt_d)
            d_node = PathNode(pt_d)
            tree.head.add_node(ancestor=pt, new_node=d_node)

            for pt_e in d_2:
                logger.info('2\tPoint: %s', pt_e)
                e_node = PathNode(pt_e)
                tree.head.add_node(ancestor=pt_d, new_node=e_node)

                for pt_f in d_3:
                    logger.info('3\t\tPoint: %s', pt_f)
                    f_node = PathNode(pt_f)
                    tree.head.add_node(ancestor=pt_e, new_node=f_node)

        # check the paths
        mypaths = tree.contours()
        logger.info("paths: all paths")
        for myp in mypaths:
            logger.info(myp)
        self.assertEqual(len(mypaths), 17, 'should have 16 paths')

        # check the paths with are len(4)
        logger.info("Paths: length 4")
        myrects = list(filter(lambda x: len(x)==4, mypaths))
        for myr in myrects:
            logger.info(myr)

        self.assertEqual(len(myrects), 11, 'should have 6 paths')
