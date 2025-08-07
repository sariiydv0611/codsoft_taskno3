import string
import random

n=int(input("enter password length:"))

uppercase_letters=string.ascii_uppercase
lowercase_letters=string.ascii_lowercase
other_symbols=string.punctuation
digits=string.digits

if n>=4:

    password=[random.choice(uppercase_letters), random.choice(lowercase_letters), random.choice(other_symbols), random.choice( digits)]
    password+=random.choices(uppercase_letters + lowercase_letters + other_symbols + digits, k=n-4)
    random.shuffle(password)
    r="".join(password)
    print(r)

else:
    print("password should be minimum of length 4!!!")