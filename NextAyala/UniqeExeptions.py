class UsernameContainsIllegalCharacter(Exception):

    def __init__(self, not_valid_char, index):
        self._not_valid_char = not_valid_char
        self._index = index

    def __str__(self):
        return 'The user name contains illegal character ' + '"' + self._not_valid_char + '" at index ' + str(
            self._index)


class UsernameTooShort(Exception):
    def __str__(self):
        return "User name too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "User name too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "Password missing a character "


class PasswordTooShort(Exception):
    def __str__(self):
        return "Password too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "Password too long"


class PassUpperCase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Uppercase)"


class PassLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Lowercase)"


class PassDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Digit)"


class PassSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Special)"
