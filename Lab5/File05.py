import random

a = []
for i in range(15):
    a.append(round(random.uniform(0,50), 2))
a = sorted(a)
print(a)
print(a[0])
print(a[-1])
# print(a.index(float(input("Wpish liczbe:"))))
t = float(input("Wpish liczbe:"))
if t in a:
    print(a.index(t))
else:
    print("None")
b = 0
for i in a:
    b += i
print(b / len(a))

c = []
for f in a:
    if f >=  (b / len(a)):
        c.append(f)
t = []
for v in a:
    if v < (b / len(a)):
        t.append(v)
print(len(c), len(t))
print(t)
print(c)