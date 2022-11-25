from math import floor


class Integer:
    something = 1
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, num):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(num):
            # test_1 = roman_numerals[num[i + 1]]
            # test_2 = roman_numerals[c]
            if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        error = "wrong type"
        if isinstance(value, float):
            return error

        try:
            number = int(value)
            return cls(number)

        except:
            return error


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

