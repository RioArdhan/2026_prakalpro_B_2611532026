height = int(input("Masukkan tinggi: "))

for row in range(1, height + 1):
    for coloumn in range(1, row + 1):
        print(coloumn, end=" ")
    print()