#Made by TRAJ
import random
import string
def generatepassword(length, complexity):
    if complexity == 1:
        chars = string.ascii_lowercase
    elif complexity == 2:
        chars = string.ascii_letters
    elif complexity == 3:
        chars = string.ascii_letters + string.digits
    elif complexity == 4:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose between 1 and 4.")
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
length = int(input("Enter the length of the password: "))
complexity = int(input("Enter the complexity level (1 to 4): "))
password = generatepassword(length, complexity)
print(f"Generated password: {password}")
#Made by TRAJ
