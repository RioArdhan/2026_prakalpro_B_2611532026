# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir conto: a1_1234
# Program ini mengguankan fungsi input()
# Prgram operator logika dalam Python

# Memasukkan nilai Boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_2026 = input("Input nilai boolean-1 (true/false): ").strip().lower == "true"
a2_2026 = input("Input nilai boolean-2 (true/false): ").strip().lower == "true"

print("\nA1_2026 =", a1_2026)
print("\nA2_2026 =", a2_2026)

# Konjungsi: bernilai true jika kedunya true
hasil_2026 = a1_2026 and a2_2026
print("\nKonjungsi (AND)")
print("A1_2026 and A2_2026 =", hasil_2026)

# Disjungsi: bernilai true jika salah satunya true
hasil_2026 = a1_2026 or a2_2026
print("\nDisjungsi (OR)")
print("A1_206 or A2_2026 =", hasil_2026)

# Negasi A1_2026: membaik nilai A1
hasil_2026 = not a1_2026
print("\nNegasi A1_2026 (NOT)")
print("not A1_2026 =", hasil_2026)

# Negasi A2: membaik nilai A2
hasil_2026 = not a2_2026
print("\nNegasi A2_2026 (NOT)")
print("not A2_2026 =", hasil_2026)

# XOR: bernilai true jika kedua nilai berbeda
hasil_2026 = a1_2026 != a2_2026
print("\nDisjungsi Eksklusif (XOR)")
print("A1_2026 XOR A2_2026 =", hasil_2026)