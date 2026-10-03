# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2026 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2026 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2026 = tinggi_2026
    c_2026 = a_2026
    lebar_2026 = (2 * tinggi_2026) - 2

    for i in range(1, tinggi_2026 + 1):
        b_2026 = c_2026 + 1

        for j in range(1, lebar_2026 + 1):

            # Baris atas dan bawah
            if i == 1 or i == tinggi_2026:
                if j == 1 or j == lebar_2026:
                    print("#", end="")
                else:
                    print("=", end="")

                    # Baris isi
            else:
                if j == 1 or j == lebar_2026:
                    print("|", end="")
                else:
                    if j == c_2026:
                        print("<", end="")
                    elif j == b_2026:
                        print(">", end="")
                    elif j == (lebar_2026 - c_2026):
                        print("<", end="")
                    elif j == (lebar_2026 - c_2026 + 1):
                        print(">", end="")
                    elif j > b_2026 and j < (lebar_2026 - c_2026):
                        print(".", end="")
                    else:
                        print(" ", end="")

            print()

            #Logika asli java
            a_2026 -= 1
            if a_2026 <= 0:
                c_2026 =(-a_2026) + 2
            else:
                c_2026 = a_2026   