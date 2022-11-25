class vowels:

    def __init__(self, letters):
        self.letters = letters
        self.all_vowels = ["a", "e", "i", "u", "y", "o"]
        self.vowels = [x for x in self.letters if x.lower() in self.all_vowels]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels:
            raise StopIteration

        return self.vowels.pop(0)


my_string = vowels('Abcedifuty0o')

for char in my_string:
    print(char)

