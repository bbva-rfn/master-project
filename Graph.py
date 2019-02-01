class Graph:
    def __init__(self):
        print('asd')


class Node:
    def __init__(self):
        self.__features = []

    def get_features(self):
        return self.__features

    def add_feature(self, feature):
        if type(feature) != Feature:
            raise Exception('Not a feature')

        self.__features.append(feature)


class Feature:
    def __init__(self, name, value):
        self.name = name
        self.value = value


node = Node()
feature = Feature('Ramon', 10)

print(node.get_features())

node.add_feature(feature)
node.add_feature(3)

print(node.get_features())