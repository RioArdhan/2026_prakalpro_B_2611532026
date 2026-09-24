# Buat file dengan nama multi_if1_NIM.py
# Buat program untuk kondisional if
# Nama variabel diatmbah 4 digit nim terakhir contoh: ipk_1234
# Program ini mengguanakan fungsi input()

umur_2026 = int(input("Input umur anda: "))
sim_2026 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_2026 >= 17 and sim_2026 == 'y':
    print("Anda Sudah Dewasa dan boleh bawa motor")

if umur_2026 >= 17 and sim_2026 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_2026 < 17 and sim_2026 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_2026 < 17 and sim_2026 != 'y':
    print("Anda Belum Cukup Umur bawa motor")
