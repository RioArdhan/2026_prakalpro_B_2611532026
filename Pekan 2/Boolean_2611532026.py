# Buat file dengan nama Booleean_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan type data Boolean
is_lulus_2026 = True
is_cumlaude_2026 = True

# Menggunakan Boolean
nilai_2026 = 85
batal_lulus_2026 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_2026 = nilai_2026 >= batal_lulus_2026 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai_2026:", nilai_2026)
print("Apakah Lulus?:", status_kelulusan_2026)
if is_lulus_2026 and is_cumlaude_2026:
    print("Selamat, Anda lulus dengan predikat cumlaude!")