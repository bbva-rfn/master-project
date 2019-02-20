from typing import List
from bson import ObjectId


class Feature:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Node:
    def __init__(self):
        self.__features = []
        self.__neighbours = []
        self.__probability = []
        self.__id = ObjectId()

    def get_id(self) -> ObjectId:
        return self.__id

    def make_connection(self, node: 'Node'):
        self.__neighbours.append(node.get_id())

    def get_features(self) -> List[Feature]:
        return self.__features

    def get_neighbours(self) -> List[ObjectId]:
        return self.__neighbours

    def add_neighbours(self, neighbours):
        if type(neighbours) != Node:
            raise Exception('Not a Neighbour Node')

        self.__neighbours.append(neighbours.id)

    def add_feature(self, feature):
        if type(feature) != Feature:
            raise Exception('Not a feature')

        self.__features.append(feature)

    def make_connections(self, nodes: List['Node']):
        for node in nodes:
            self.make_connection(node)