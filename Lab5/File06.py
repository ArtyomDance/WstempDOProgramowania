x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = -3
for i in range(len(x)):
    print(x[b], end=" ")
    b += 1
print()
y = x
print(x)
y.insert(0, 100)
print(y)
