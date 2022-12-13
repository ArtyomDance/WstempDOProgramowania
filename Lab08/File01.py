def find(a, b):
    c = []
    for i in range(len(a)):
        if a[i] == b:
            c.append(i)
    return(c)
print(find([2, 5, 7, 1, 4], 7))