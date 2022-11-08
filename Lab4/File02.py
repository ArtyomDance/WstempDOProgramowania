import random


zestaw_1 = []
zestaw_2 = []
a = int(input())
for i in range(a):
    zestaw_1.append(random.randrange(1, 11))
print(zestaw_1)
f = int(input())
for x in range(f):
    zestaw_2.append(random.randrange(1, 16))
print(zestaw_2)
b = int(input())
if b in zestaw_1:
    print("Yes in 1")
elif b in zestaw_2:
    print("Yes in 2")
else:
    print("Niema")
zestaw_1_2 = zestaw_2 + zestaw_1
print(zestaw_1_2)