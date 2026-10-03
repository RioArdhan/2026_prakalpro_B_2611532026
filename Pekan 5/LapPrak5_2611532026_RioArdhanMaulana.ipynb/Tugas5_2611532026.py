print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_2026 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Border atas
for pagar_2026 in range(1):
    print("#", end="")
    for garis_2026 in range(4 * n_2026 + 5):
        print("=", end="")
    print("#")

# Fase 1: Jam pasir atas
for baris_2026 in range(n_2026, 0, -1):
    print("|", end="")
    print(" ", end="")

    # Spasi penyeimbang kiri
    for spasi_2026 in range(2 * (n_2026 - baris_2026)):
        print(" ", end="")

    # Deret angka mundur
    for angka_2026 in range(baris_2026, 0, -1):
        print(angka_2026, end=" ")
    
    # Poros kristal
    print("<*>", end="")

    # Deret angka maju
    for angka_2026 in range(1, baris_2026 + 1):
        print(" ", end="")
        print(angka_2026, end="")

    # Spasi penyeimbang kanan
    for spasi_2026 in range(2 * (n_2026 - baris_2026)):
        print(" ", end="")

    print(" |")

# Fase 2: Poros titik pusat
print("|", end="")
for spasi_2026 in range(2 * n_2026 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_2026 in range(2 * n_2026 + 1):
    print(" ", end="")
print("|")

# Fase 3: Jam pasir bawah
for baris_2026 in range(1, n_2026 + 1):
    print("|", end="")
    print(" ", end="")

    # Spasi penyeimbang kiri
    for spasi_2026 in range(2 * (n_2026 - baris_2026)):
        print(" ", end="")

    # Deret angka mundur
    for angka_2026 in range(baris_2026, 0, -1):
        print(angka_2026, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Deret angka maju
    for angka_2026 in range(1, baris_2026 + 1):
        print(" ", end="")
        print(angka_2026, end="")

    # Spasi penyeimbang kanan
    for spasi_2026 in range(2 * (n_2026 - baris_2026)):
        print(" ", end="")

    print(" |")

# Border bawah
for pagar_2026 in range(1):
    print("#", end="")
    for garis_2026 in range(4 * n_2026 + 5):
        print("=", end="")
    print("#")