class Map:
    def __int__(self, iterate):
        self.list = []
        self.__geek(iterate)

    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)

    # private copy of original geek() method
    __geek = geek


# provides new signature for geek() but
# does not break __init__()

# class MapSubClass(Map):
#     def geek(self, keys, value):
#         for i in zip(keys, value):
#             self.list.append(i)


# _Single  UnderScore

# Basically one underline in the beginning of a method, function,
# or data member means you should not access this method because
# it’s not part of the API

def _get_errors(self):
    if self._errors is None:
        self.full_clean()
    return self._errors


errors = property(_get_errors)



