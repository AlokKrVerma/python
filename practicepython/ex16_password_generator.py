import string
import random

def generate_password(pass_strength = "strong"):
    if pass_strength == "strong":
        return ''.join(random.SystemRandom().choice(string.printable) for i in range(8))
    else:
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(8))

print(generate_password(str(input("Do you want a strong password or with normal strength(Strong/Normal): ")).lower()))

