import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']
symbols = ['@', '!', '#', '$', '%', '&', '*', '-', '_']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def generate(lenght):
    chars = alphabet + symbols + numbers
    pwd = ''
    while len(pwd) < lenght:
        pwd += random.choice(chars)
    return pwd

lenght = 13
newPwd = generate(lenght)
print("Nova senha:", newPwd)