class Node:
    def __init__(self, id):
        self.__features = []
        self.__neighbours = []
        self.__probability = []
        self.__id = id

    def get_probability(self):
        return self.__probability

    def id_nei(self):
        if type(id) != id:
            raise Exception('Not a correct id')

    def get_features(self):
        return self.__features

    def get_neigbours(self):
        return self.__neighbours

    def add_neighbours(self, neighbours):
        if type(neighbours) != Node:
            raise Exception('Not a Neighbour Node')

        self.__neighbours.append(neighbours.id)

    def add_feature(self, feature):
        if type(feature) != Feature:
            raise Exception('Not a feature')

        self.__features.append(feature)


class Feature:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Probability:
    def __init__(self, value):
        self.value = value


node = Node()
feature = Feature('Ramon', 10)

print(node.get_features())

node.add_feature(feature)

print(node.get_features())
