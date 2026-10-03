# Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2026 = int(input("Masukkan nilai batas: "))

jumlah_2026 = 0
for i in range(1, ulang_2026 + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah_2026 = jumlah_2026 + i

        if i < ulang_2026:
             print(" + ", end="")
        else:
            print(" = ", jumlah_2026, end="")
print()
print("Jumlah =", jumlah_2026)