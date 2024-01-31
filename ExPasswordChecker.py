# at least 8 char long
# contains any sort of letters, numbers and $%#@

import re

regex = re.compile(r'(?=.*[a-zA-Z])(?=.*[0-9])')
password = ("f#A0hasdga")


def check_password():
    check_password = regex.match(password)
    if check_password and len(password) > 8:
        print("Thank you for creating the password.")

    else:
        print("That is not a valid password")

check_password()
