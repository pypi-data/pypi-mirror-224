from typing import List

MAX_ARRAY_DIMS = 10
MAX_MAP_DIMS = 21


class NodeVocabulary:
    def __init__(self):
        self._dtypes = [
            "float",
            "double",
            "bool",
            "char",
            "short",
            "int",
            "long",
            "long long",
            "unsigned char",
            "unsigned short",
            "unsigned int",
        ]
        self._reduction_types = [
            "Custom",
            "Min",
            "Max",
            "Sum",
            "Product",
            "Sub",
            "Div",
            "Logical_And",
            "Bitwise_And",
            "Logical_Or",
            "Bitwise_Or",
            "Logical_Xor",
            "Bitwise_Xor",
            "Min_Location",
            "Max_Location",
            "Exchange",
        ]

        self._vocab = ["ACCESS_NODE", "MAP_ENTRY", "MAP_EXIT", "MAP_BODY", "MEMLET"]

        self._features = {
            "ACCESS_NODE": 7 + len(self._dtypes) + 2 * MAX_ARRAY_DIMS,
            "MAP_ENTRY": 3 + 2 * MAX_MAP_DIMS,
            "MAP_EXIT": 1,
            "MAP_BODY": 1,
            "MEMLET": 3
            + (len(self._reduction_types) + 1)
            + 2 * (MAX_ARRAY_DIMS * (MAX_MAP_DIMS + 1))
            + MAX_ARRAY_DIMS,
        }

        index = 0
        self._ranges = {}
        for word in self._vocab:
            feature_size = self._features[word]
            self._ranges[word] = range(index, index + feature_size, 1)

            index += feature_size

    def __len__(self):
        return len(self._vocab)

    def __contains__(self, word):
        return word in self._ranges

    def __getitem__(self, word):
        return self._ranges[word]

    def __iter__(self):
        return self._vocab.__iter__()

    @property
    def dtypes(self) -> List[str]:
        return self._dtypes

    @property
    def reduction_types(self) -> List[str]:
        return self._reduction_types

    @property
    def dims(self) -> int:
        return sum(self._features.values())
