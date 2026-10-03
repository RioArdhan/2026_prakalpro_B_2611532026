# Buat file dengan nama perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2026 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_2026 -1)
for i in range(ulang_2026):
    print(i, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_2026)
for i in range(1, ulang_2026 + 1):
    print(i, end=" ")