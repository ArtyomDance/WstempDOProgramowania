def dodawanie(a, b):
    return (a + b)
def odejmowanie(a, b):
    return (a - b)
def mnożenie(a, b):
    return (a * b)
def dzielenie(a, b):
    if b == 0:
        return()
    return (a / b)
kalkulator = {
    "+":dodawanie(),
    "-":odejmowanie,
    "*":mnożenie,
    "/":dzielenie
}

