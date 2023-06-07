class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 > len(value) or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        length_condition = len(value) >= 8
        upper_case_condition = False
        digit_condition = False
        for char in value:
            if char.isupper():
                upper_case_condition = True
            if char.isdigit():
                digit_condition = True

        conditions = all([length_condition, upper_case_condition, digit_condition])
        if not conditions:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'



    
