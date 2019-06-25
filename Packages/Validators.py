
import re

def phonenumbervalidator(num):
    pattern = "^[6-9][0-9]{9}$|[0][[6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$"
    if re.match(pattern,str(num)):
        return True
    else:
        return False

phonenumbervalidator(7045672354)

def emailvalidator(email):
    pattern = "  ^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][0-9a-z]{3,15}[.][a-z]{2,4}$"
    if re.match(pattern,email):
        return True
    else:
        return False
    
emailvalidator("name1@domain.ext")