import re
import string

import UniqeExeptions


def check_input(username, password):
    try:

        # match the string to the pattern from beginning to end, if there is a letter that do not match raise exeption
        if re.match("^[A-Za-z0-9_]*$", username) is None:
            not_valid_char = re.sub("[a-zA-Z0-9_]", "", username)
            index = username.index(not_valid_char)
            raise UniqeExeptions.UsernameContainsIllegalCharacter(not_valid_char, index)

        if len(username) < 3:
            raise UniqeExeptions.UsernameTooShort

        if len(username) > 16:
            raise UniqeExeptions.UsernameTooLong

        if not any(c.isupper() for c in password):
            raise UniqeExeptions.PassUpperCase

        if not any(c.islower() for c in password):
            raise UniqeExeptions.PassLowercase

        if not any(c.isdigit() for c in password):
            raise UniqeExeptions.PassDigit

        if not any(c in string.punctuation for c in password):
            raise UniqeExeptions.PassSpecial

        if len(password) < 8:
            raise UniqeExeptions.PasswordTooShort

        if len(password) > 40:
            raise UniqeExeptions.PasswordTooLong

    except Exception as e:
        print(e)
        return False

    else:
        print("OK")
        return True


def main():
    username = input("enter user name ")
    password = input("enter password, password must contain:\nuppercase and lower case letter\ndigit and a "
                     "punctuation")

    while not check_input(username, password):
        username = input("enter user name ")
        password = input("enter password, password must contain:\nuppercase and lower case letter\ndigit and a "
                         "punctuation")


if __name__ == "__main__":
    main()
