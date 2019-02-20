from typing import List, Union

import numpy as np
from scipy.sparse import lil_matrix

from Node import Node


class Graph:
    def __init__(self, nodes: 'np.ndarray[Node]'):
        assert isinstance(nodes, np.ndarray)
        assert all(isinstance(node, Node) for node in nodes)

        self.__nodes = nodes
        num_nodes = len(nodes)
        self.__matrix = lil_matrix((num_nodes, num_nodes))

    def set_connections(self, from_node: int, to_nodes: Union[int, List[int]]):
        self.__matrix[from_node, to_nodes] = 1

        if (type(to_nodes) == int and from_node == to_nodes) or (type(to_nodes) == list and from_node in to_nodes):
            self.__matrix[from_node, from_node] = 2

    def remove_connections(self, from_node: int, to_nodes: Union[int, List[int]]):
        self.__matrix[from_node, to_nodes] = 0

    def get_connections(self, node_id: int) -> lil_matrix:
        assert isinstance(node_id, int)

        return self.__matrix[node_id]

    def get_connected_nodes(self, node_id: int) -> List[Node]:
        assert isinstance(node_id, int)

        connected_node_ids = self.get_connections(node_id)

        return self.__nodes[connected_node_ids].copy()

    def get_matrix(self) -> lil_matrix:
        return self.__matrix

    def get_node(self, node_id: int):
        assert isinstance(node_id, int)
        if node_id >= self.num_nodes:
            raise Exception("Node with id %d does not exist" % node_id)

        return self.__nodes[node_id]

    @property
    def num_nodes(self):
        return self.__matrix.shape[0]
