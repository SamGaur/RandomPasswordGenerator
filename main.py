# Random Password Generator

# Importing Module
import random

password = ""

for f in range(10):
    i = chr(random.randint(65,90))
    password = str(password) + i
print(password)

##

password = ""
for a in range(5):
    u = chr(random.randint(65, 90))
    l = chr(random.randint(65, 90)).lower()
    password = str(password) + u + l
print(password)

# for-> upper then lower (50 characters)

password = ""

for n in range(5):
    x = chr(random.randint(65, 90))
    for m in range(5):
        y = chr(random.randint(65, 90)).lower()
        password = str(password) + x + y

print(len(password), password)
