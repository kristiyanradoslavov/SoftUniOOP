class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0 - self.step
        self.all_nums = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.all_nums) >= self.count:
            raise StopIteration

        self.num += self.step
        self.all_nums.append(self.num)

        return self.num


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

