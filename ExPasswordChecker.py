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


### Andrei's method (he adds the specific characters and the length of the password in regex and creates it like that)
pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
password2 = "hjdgas"
check = pattern2.fullmatch(password2)
print(check)