import random

with open("random.txt", 'w+') as file:
    for i in range(500):
        file.write(str(random.randint(1, 100)))
        file.write("\n")
    file.seek(0)