a = int(input("Wprowadz wiek:"))
if a < 4:
    cena = 0
elif a >= 4 and a < 18:
    cena = 10
else:
    cena = 20
print(f"cena biletu:", {cena}, "zl")