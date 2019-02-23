class Features:
    def __init__(self):
        self.__dict = {}

    def set(self, name, value):
        self.__dict[name] = value

    def get(self, key):
        if key not in self.__dict:
            raise Exception('Feature `%s` does not exist' % key)

        return self.__dict[key]

    def remove(self, key):
        del self.__dict[key]

    @property
    def features(self):
        return self.__dict.keys()


class Node:
    def __init__(self, id=0):
        self.__features = Features()
        self.__id = id

    def set_id(self, id):
        self.__id = id

    def get_feature(self, feature_name):
        return self.__features.get(feature_name)

    def set_feature(self, feature_name, value):
        self.__features.set(feature_name, value)

    def delete_feature(self, feature_name):
        self.__features.remove(feature_name)

    @property
    def id(self):
        return self.__id
