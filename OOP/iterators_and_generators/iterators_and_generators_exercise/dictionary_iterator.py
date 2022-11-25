class dictionary_iter:

    def __init__(self, ele_dict):
        self.ele_dict = ele_dict

    def __iter__(self):
        return self

    def __next__(self):
        if not self.ele_dict:
            raise StopIteration

        for key, value in self.ele_dict.items():
            self.ele_dict.pop(key)
            return key, value


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)



