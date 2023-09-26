import random
import string

amount = 4

for _ in range(amount):
    random_letter = random.choice(string.ascii_uppercase)
    print(random_letter)