# Buat file dengan nama if_elif_else1_NIM.py
# Buat program untuk kondisional if
# Nama variabel diatmbah 4 digit nim terakhir contoh: ipk_1234
# Program ini mengguanakan fungsi input()

umur_2026 = int(input("Input umur anda: "))
sim_2026 = input("Apakah Anda Sudah Punya Sim C: ")[0]

if umur_2026 >= 17 and sim_2026 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_2026 >= 17 and sim_2026 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2026 < 17 and sim_2026 == 'y':
    print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")
print("Program Selesai")