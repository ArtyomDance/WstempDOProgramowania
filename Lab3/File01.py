a = int(input("Prosze podac:"))
b = int(input("Prosze podac:"))
if a < b:
    a, b = b, a
while b <= a:
    print(b, end=" ")
    b += 1
