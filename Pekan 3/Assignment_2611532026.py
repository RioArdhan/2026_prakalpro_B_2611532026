# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2026 = int(input("Input angka-1: "))
angka2_2026 = int(input("Input angka-2: "))

print("\nNilai awal angka1_2026 =", angka1_2026)
print("Nilai angka2_2026 =", angka2_2026)

# Assignment biasa
hasil_2026 = angka1_2026
print("\nAssignment biasa (=)")
print("Hasil =", hasil_2026)

# Assignment penambahan
hasil_2026 = angka1_2026
hasil_2026 += angka2_2026
print("\nAssignment pnambahan (+=)")
print("Hasil =", hasil_2026)

# Assignment pengurangan
hasil_2026 = angka1_2026
hasil_2026 -= angka2_2026
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_2026)
      
# Assignment perkalian
hasil_2026 = angka1_2026
hasil_2026 *= angka2_2026
print("nAssignment perkalian (*=)")
print("Hasil =", hasil_2026)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2026 != 0:
    hasil_2026 = angka1_2026
    hasil_2026 /= angka2_2026
    print("nAssignment pembagian (/=)")
    print("Hasil =", hasil_2026)
    # Operator tambahan
    hasil_2026 = angka1_2026
    hasil_2026//= angka2_2026
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2026)
    hasil_2026 = angka1_2026
    hasil_2026 %= angka2_2026
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_2026)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

    # Operator tambahan: assignment perpangkatan
    hasil_2026 = angka2_2026
    hasil_2026 **= angka2_2026
    print("\nAssignment perpangkatan (**=)")
    print("Hasil =", hasil_2026)