import random

def createpassword(name):
    password = ""
    name = name.lower()
    name += name.upper()
    name += "0123456789"
    uzunluk = random.randint(6,10)
    for i in range(uzunluk):
        password += random.choice(name)
    
    return password

name = input("isim giriniz: ")
for i in range(1000):
    print(createpassword(name))

