# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_2026
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2026 = int(input("Input angka-1: "))
angka2_2026 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_2026 = angka1_2026 > angka2_2026
print("\nOperator lebih besar dari")
print("anka1_2026 > angka2_2026 =", hasil_2026)

# Lebih kecil dari
hasil_2026 = angka1_2026 < angka2_2026
print("\nOperator lebih kecil dari")
print("angka1_2026 < angka2_2026 =", hasil_2026)

# Lebih besar dari atau sama dengan
hasil_2026 = angka1_2026 >= angka2_2026
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_2026 >= angka2_2026 =", hasil_2026)

# Lebih kecil dari atau sama dengan
hasil_2026 = angka1_2026 <= angka2_2026
print("\nOperator lebih kecil atau sama dengan")
print("angka1_2026 <= angka2_2026 =", hasil_2026)

# Sama dengan
hasil_2026 = angka1_2026 == angka2_2026
print("\nOperator sama dengan")
print("angka1_2026 == angka2_2026 =", hasil_2026)

# Tidak sama dengan
hasil_2026 = angka1_2026 != angka1_2026
print("\nOperator tidak sama dengan")
print("angka1_2026 != angka2-2026 =", hasil_2026)

# Tambahan: perbandingan berantai dalam Python
hasil_2026 = 0 < angka1_2026 < 100
print("\n Perbandingan berantai")
print("0 < angka1_2026 , 100 =", hasil_2026)

hasil_2026 = 0 < angka2_2026
print("0 < angka2_2026 < 100 =", hasil_2026)