import sys

name = "p8"
values = [204, 261, 289, 348, 380, 408, 526, 541, 678, 779, 840, 858, 889, 913, 940]

with open(name, "r") as ins:
    counter = 0
    array = []
    for line in ins:
        counter += 1
        if counter in values:
            array.append(line)

f = open("/p8_fix", 'a')
for el in array:
    f.write(str(el) + "\n")
f.close()