x = input("Wprowadz literu:")
if len(x) > 1 or len(x) == 0:
    print("bland")
    exit()
if "a" <= x <= "z":
    print("mała")
elif "A" <= x <= "Z":
    print("duża")
else:
    print("To nie jest litera")