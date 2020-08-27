
def app(iterations, step):
    i = 0
    numbers = []
    while i < iterations:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


        print("The numbers: ")

    for n in numbers:
        print(n)

app(30,2)
