x = int(input())
pares = 0

if x <= 200:
    while True:
        if x%2 == 0:
            pares += 1

        if x == 200:
            break

        x += 1

    print(pares)

else:
    print("0")

