# Buat file dengan nama if2_NIM.py
# Buat program untuk kondisional if
# Nama variabel diatmbah 4 digit nim terakhir contoh: ipk_1234
# Program ini mengguanakan fungsi input()

ipk_2026 = float(input("Input IPK Anda = "))

if ipk_2026 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str(ipk_2026))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")