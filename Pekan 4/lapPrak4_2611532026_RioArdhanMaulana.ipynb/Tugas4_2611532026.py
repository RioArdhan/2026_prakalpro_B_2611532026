# Tugas4_2611532026.py

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# Input Data Pengunjung
nama_2026 = input("Masukkan Nama Pengunjung        : ")
umur_2026 = int(input("Input umur anda                 : "))
sim_2026 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].lower()

# Pilihan Paket Wahana
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_2026 = int(input("Masukkan nomor paket (1-5)      : "))

# Pemilihan Wahana dengan match-case
match paket_2026:
    case 1:
        nama_wahana_2026 = "Wahana Safari Rimba"
        harga_satuan_2026 = 50000
    case 2:
        nama_wahana_2026 = "Wahana Arung Jeram"
        harga_satuan_2026 = 75000
    case 3:
        nama_wahana_2026 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2026 = 120000
    case 4:
        nama_wahana_2026 = "Wahana Roller Coaster Kilat"
        harga_satuan_2026 = 100000
    case 5:
        nama_wahana_2026 = "Wahana All-Access VIP"
        harga_satuan_2026 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

# Input jumlah tiket
jumlah_tiket_2026 = int(input("Masukkan jumlah tiket           : "))

# If tunggal untuk validasi jumlah tiket
if jumlah_tiket_2026 <= 0:
    print("Peringatan: kuota tiket tidak valid.")

# Validasi kelayakan pengunjung
print("\n--- KELAYAKAN PENGUNJUNG ---")

if paket_2026 == 3 and umur_2026 >= 17 and sim_2026 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif paket_2026 == 3 and umur_2026 >= 17 and sim_2026 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif paket_2026 == 3 and umur_2026 < 17 and sim_2026 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif paket_2026 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif umur_2026 >= 10:
    print("Status Akses: Anda memenuhi syarat usia wahana.")
else:
    print("Status Akses: Anda belum cukup umur untuk wahana ini.")

# Input data diskon
is_member_2026 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_2026 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# Perhitungan subtotal
subtotal_2026 = harga_satuan_2026 * jumlah_tiket_2026

# Multi-if terpisah untuk diskon akumulatif
total_diskon_persen_2026 = 0

if subtotal_2026 >= 200000:
    total_diskon_persen_2026 += 10

if is_member_2026 in ['y', 'ya']:
    total_diskon_persen_2026 += 5

if kode_promo_valid_2026 in ['y', 'ya']:
    total_diskon_persen_2026 += 15

if jumlah_tiket_2026 >= 5:
    total_diskon_persen_2026 += 5

# Perhitungan nominal diskon dan total bayar
nominal_diskon_2026 = subtotal_2026 * (total_diskon_persen_2026 / 100)
total_bayar_2026 = subtotal_2026 - nominal_diskon_2026

# Evaluasi audit transaksi
if total_bayar_2026 > 300000:
    catatan_layanan_2026 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_2026 = "Terima kasih telah berkunjung."

# Rincian pembayaran
print("\n--- Rincian Pembayaran ---")
print(f"Nama Pengunjung   : {nama_2026}")
print(f"Wahana            : {nama_wahana_2026}")
print(f"Harga Satuan      : Rp {harga_satuan_2026:,.0f}")
print(f"Jumlah Tiket      : {jumlah_tiket_2026}")
print(f"Subtotal Belanja  : Rp {subtotal_2026:,.0f}")
print(f"Total Diskon      : {total_diskon_persen_2026}% (Rp {nominal_diskon_2026:,.0f})")
print(f"Total Bayar       : Rp {total_bayar_2026:,.0f}")
print(f"Catatan Layanan   : {catatan_layanan_2026}")
print("Program Selesai")