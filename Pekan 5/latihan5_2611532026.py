# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2026 = int(input("Masukkan tinggi segitiga: "))

for i_2026 in range(1, tinggi_2026 + 1):
    print(" " * (tinggi_2026 - i_2026), end="")

    for j_2026 in range(i_2026):
        print("*", end=" ")
    
    print()