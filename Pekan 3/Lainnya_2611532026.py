# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir conto: angka1_1234
# Program ini mengguanakan fungsi input()
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERTOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2026 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2026 = [int(angka.strip()) for angka in input_data_2026.split(",")]

nilai_dicari_2026 = int(input("Masukkan angka yang ingin dicari: "))

# Operator In
hasil_2026 = nilai_dicari_2026 in data_2026
print("\nOperator keanggotaan IN")
print(nilai_dicari_2026, "in", data_2026, "=", hasil_2026)

# Operator Not In
hasil_2026 = nilai_dicari_2026 not in data_2026
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2026, "not in", data_2026, "=", hasil_2026)


print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_20226 = data_2026

# objek2 menggunakan list dari input pengguna
objek2_2026 = objek1_2026

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2026 = data_2026.copy()

print("objek1_2026 =", objek1_2026)
print("objek2_2026 =", objek2_2026)
print("objek3_2026 =", objek3_2026)

# Operator Is
hasil_2026 = objek1_2026 is objek2_2026
print("\nOperator identitas IS")
print("objek1_2026 is objek2_2026 =", hasil_2026)

# Operator Is Not
hasil_2026 = objek1_2026 is not objek3_2026
print("\nOperator identitas IS NOT")
print("objek1_2026 is not objek3_2026 =", hasil_2026)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai:")
print("objek1_2026 is objek3_2026 =", objek1_2026 is objek3_2026)
print("objek1_2026 == objek3_2026 =", objek1_2026 == objek3_2026)