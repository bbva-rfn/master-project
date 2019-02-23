import pickle
from pathlib import Path
from typing import List, Union

from nptyping import Array
from scipy.sparse import lil_matrix

from Node import Node


class Graph:
    def __init__(self, nodes: Array[Node]):
        assert isinstance(nodes, Array[Node])

        self.__set_node_ids(nodes)
        self.__nodes = nodes
        num_nodes = len(nodes)
        self.__matrix = lil_matrix((num_nodes, num_nodes))

    def __set_node_ids(self, nodes: Array[Node]):
        for id, node in enumerate(nodes):
            node.set_id(id)

    def set_connections(self, from_node: int, to_nodes: Union[int, List[int]]):
        self.__matrix[from_node, to_nodes] = 1

        if (type(to_nodes) == int and from_node == to_nodes) or (type(to_nodes) == list and from_node in to_nodes):
            self.__matrix[from_node, from_node] = 2

    def remove_connections(self, from_node: int, to_nodes: Union[int, List[int]]):
        self.__matrix[from_node, to_nodes] = 0

    def get_connections(self, node_id: int) -> Array[int]:
        assert isinstance(node_id, int)

        _, cols = self.__matrix.getrow(node_id).nonzero()

        return cols

    def get_connected_nodes(self, node_id: int) -> Array[Node]:
        assert isinstance(node_id, int)

        connected_node_ids = self.get_connections(node_id)

        return self.__nodes[connected_node_ids]

    def get_matrix(self) -> lil_matrix:
        return self.__matrix

    def get_nodes(self, node_ids: Union[int, List[int]]):
        return self.__nodes[node_ids]

    def save(self, file_path: str):
        assert isinstance(file_path, str)

        file_path = Path(file_path)
        pickle.dump(self, file_path.open("wb"))

    @staticmethod
    def load(file_path: str) -> 'Graph':
        assert isinstance(file_path, str)

        file_path = Path(file_path)
        graph = pickle.load(file_path.open("rb"))

        if not isinstance(graph, Graph):
            raise Exception("File not a graph pickle")

        return graph

    @property
    def num_nodes(self):
        return self.__matrix.shape[0]
