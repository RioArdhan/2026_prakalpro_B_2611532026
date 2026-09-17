# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("\n==================================")
print("3. OPERATOR BITWISE")
print("==================================")

angka1_2026 = int(input("Masukkan angka bitwise-1: "))
angka2_2026 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner:")
print("Angka 1:", angka1_2026, "-| biner", bin(angka1_2026))
print("Angka 2:", angka2_2026, "-| biner", bin(angka2_2026))

# Bitwise AND
hasil_2026 = angka1_2026 & angka2_2026
print("\nBitwise AND (&)")
print(angka1_2026, "&", angka2_2026, "=", hasil_2026)
print("Biner hasil =", bin(hasil_2026))
print("Biner hasil (8 bit) =", format(hasil_2026, '08b'))

# Bitwise OR
hasil_2026 = angka1_2026 | angka2_2026
print("\nBitwise OR (|)")
print(angka1_2026, "|", angka2_2026, "=", hasil_2026)
print("Biner hasil =", bin(hasil_2026))
print("Biner hasil (8 bit) =", format(hasil_2026, "08b"))

# Bitwise XOR
hasil_2026 = angka1_2026 ^ angka2_2026
print("\nBitwise XOR (^)")
print(angka1_2026, "^", angka2_2026, "=", hasil_2026)
print("Biner hasil =", bin(hasil_2026))
print("Biner hasil (8 bit) =", format(hasil_2026, '08b'))

# Bitwise NOT
hasil_2026 = ~angka1_2026
print("\nBitwise NOT (~)")
print("~", angka1_2026, "=", hasil_2026)
print("Biner hasil =", bin(hasil_2026))
print("Biner hasil (8 bit) =", format(hasil_2026, '08b'))

# Bitwise geser kiri
jumlah_geser_2026 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2026 = angka1_2026 << jumlah_geser_2026
print("\nBitwise Geser Kiri (<<)")
print(angka1_2026, "<<", jumlah_geser_2026, "=", hasil_2026)
print("Biner hasil =", bin(hasil_2026))
print("Biner hasil (8 bit) =", format(hasil_2026, '08b'))

# Bitwise geser kanan
hasil_2026 = angka1_2026 >> jumlah_geser_2026
print("\nBitwise Geser Kanan (>>)")
print(angka1_2026, ">>", jumlah_geser_2026, "=", hasil_2026)
print("Biner hasil =", bin(hasil_2026))
print("Biner hasil (8 bit) =", format(hasil_2026, '08b'))