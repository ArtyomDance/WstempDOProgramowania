a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
D1 = {}
for i in range(len(a)):
    D1[a[i]] = str(a[i] * a[i])
print(D1)