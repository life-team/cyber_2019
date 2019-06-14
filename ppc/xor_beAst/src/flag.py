import string
import random

sl = string.ascii_lowercase + string.ascii_uppercase
with open('code.txt', 'w') as f:
    for i in range(2000000):
        f.write(random.choice(sl))
with open('flag.txt', 'w') as f:
    for i in range(2000000):
        f.write(random.choice(sl))
