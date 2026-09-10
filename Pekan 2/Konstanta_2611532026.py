# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1234
from typing import Final, final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2026 = float(input('Masukkan nilai jari-jari: '))
luas_2026 = PI * jari_2026 * jari_2026
print("Luas lingkaran dengan jari-jari %.2f adalh %.2f" % (jari_2026, luas_2026))