import re


class Client:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        pattern = r"\b0\d+\b"

        result = re.match(pattern, value)

        if result and len(value) == 10:
            self.__phone_number = value

        else:
            raise ValueError("Invalid phone number!")
