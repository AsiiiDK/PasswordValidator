# Multiple line function
def validPass(password):
    if len(password) >= 8:
        if any(char.isdigit() for char in password):
            return "Valid"
        else:
            return "not valid"
    else:
        return "Not Valid"


# One line function
def validPass2(password):
    return "Valid" if len(password) >= 8 and any(char.isdigit() for char in password) else "Not valid"


password = input("Type your password to get it validatet: ")


valid = validPass2(password)
print("Your password is " + valid)