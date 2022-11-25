class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.control_num = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.control_num == 0:
            raise StopIteration

        self.control_num -= 1

        return self.control_num


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

