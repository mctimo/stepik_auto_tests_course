# "6 7 8 7 8 2 7"
# "2 2 2 10"

def pairs():
    x = input("Введите строку: ").split()
    counter = 0

    for i in range(len(x)):
        for j in x[i + 1:]:
            if x[i] == j:
                counter += 1

    print(f"Пар в строке: {counter}")


pairs()




