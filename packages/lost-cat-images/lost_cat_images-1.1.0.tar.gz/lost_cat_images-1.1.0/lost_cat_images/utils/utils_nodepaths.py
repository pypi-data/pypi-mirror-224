from datetime import datetime
import io
import logging
import os
import re
import sys
import numpy as np
import cv2 as cv
from scipy.sparse import csr_matrix

logger = logging.getLogger(__name__)

class PathNode:
    """A class to sotre the point, is a single direction linked
    list."""

    def __init__(self, point: tuple = None, constraints: list = ['horizontal']):
        """create a new instance using the single point
        parameters
        ----------
        point: tuple : a point (x,y)
        constraints: list of strings : horizontal | ...
        """
        self.point = point
        self.constraints = constraints
        self.descendants = []
    
    def add_node(self, ancestor: tuple, new_node: object):
        """Adds a node based on the origin point and the 
        next pathNode point
        
        parameters
        ----------
        ancestor: tuple : a point (x,y)
        new_node: PathNode: the node to link to if
            matching criteria match
        """
        logger.debug("NODE: Add %s -> %s", ancestor, new_node)
        if self.point == ancestor:
            # this is the ancestor of the new node
            add_node = True
            for node in self.descendants:
                if node.point == new_node.point:
                    add_node = False
                    return
                
            if add_node:
                xa, ya = self.point
                xd, yd = new_node.point
                if 'horizontal' in self.constraints:
                    if xa == xd or ya == yd:
                        self.descendants.append(new_node)    
                else:
                    self.descendants.append(new_node)
        else:
            # walk the tree and add as descendant
            for node in self.descendants:
                node.add_node(ancestor=ancestor, new_node=new_node)

    def __repr__(self) -> str:
        """Returns a string representation of the class
        
        returns
        -------
        string : the class point and the number of immediate descendants
        """
        return f'Node Class<{self.point}> Descendants:{len(self.descendants)}'

    def dump(self):
        """ build a dictonary of the points
        
        returns
        -------
        dict : {point : dict of points : descendants}
        """
        data = {}
        if len(self.descendants) > 0:
            for node in self.descendants:
                data[node.point] = node.dump()

            return data
        return

class PathNodeTree:
    """The head node for the PathNode"""

    def __init__(self):
        """a linked list header for points"""
        self.head = None
        self._data = {}
        self._paths = []

    def _hierarchy(self, dictionary, prefix=None):
        """Internal function to return the paths as a list"""
        prefix = prefix if prefix is not None else []
        for key, value in dictionary.items():
            if isinstance(value, dict) and value:
                self._hierarchy(value, [*prefix, key])
            else:
                self._paths.append([*prefix, key])

    def dump(self):
        """Head function to return the dictonary of descendants and linked nodes

        returns
        -------
        dict : {point : dict of points : descendants}
        """
        self._data[self.head.point] = self.head.dump()
        logger.debug("Head: %s", self._data)
        return self._data

    def contours(self):
        """Returns the possible paths in the object
        
        returns
        -------
        list:
            type: str [rectangle, square, circle, etc.]
            path: list of points 
        """
        data = self.dump()
        self._paths = []
        self._hierarchy(dictionary=data, prefix=None)
        return self._paths
