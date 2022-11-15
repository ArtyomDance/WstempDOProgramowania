a = ['Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr',
'Zuzia', 'Bartek', 'Jacek']
a[3] = "Artyom"
a.insert(4,"Lena")
a.insert(0, "Danil")
a.insert(0, "Nikita")
a.insert(0, "Semen")
b = input("Podaj ime:")
a.remove(b)
a[-1] = "Masha"
print(a[:3], a[-3:])
b = input("Podaj ime:")
if b in a:
    print("Yes")
else:
    print("No")
a = sorted(a)
print(a)
print(a.reverse())
print(a)
for i in range(len(a) // 2):
    i -= 1
    a.pop(i)
print(a)
print(len(a))