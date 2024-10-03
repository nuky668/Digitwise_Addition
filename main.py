### Digitwise Addition ###

a = 0
n = 6789
k = 4

# hlavní cyklus 
while a != k:
    # 1. čísla zvětšíme o 1 a naházíme do listu
    n = str(n)
    list1 = []
    for digit in n:
        digit = int(digit) + 1
        list1.append(digit)

    del n
    n = ""

    # 2. vybereme čísla z listu a uděláme proměnnou n
    for item in list1:
        n = n + str(item)
    n = int(n)

    print(n)        # kontrolní výpis
    a += 1



