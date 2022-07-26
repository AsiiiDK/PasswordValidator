# One line function
def validPass2(password):
    return "Valid" if len(password) >= 8 and any(char.isdigit() for char in password) else "Not valid"


password = input("Type your password to get it validatet: ")


valid = validPass2(password)
print("Your password is " + valid)
