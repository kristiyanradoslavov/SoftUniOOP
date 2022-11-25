class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value

        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        length = False
        upper_case = False
        digit = False

        for symbol in value:
            if symbol == symbol.upper() and symbol.isalpha():
                upper_case = True

            elif symbol.isdigit():
                digit = True

        if len(value) >= 8:
            length = True

        if length and upper_case and digit:
            self.__password = value

        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {len(self.password) * '*'}"


profile_with_invalid_password = Profile('My_username', 'My-password')