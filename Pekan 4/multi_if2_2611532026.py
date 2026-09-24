# Buat file dengan nama multi_if2_NIM.py
# Buat program untuk kondisional if
# Nama variabel diatmbah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini mengguanakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_2026 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2026 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_2026 = input_member_2026 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2026 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2026 = input_promo_2026 in ["y" "ya"]

total_diskon_persen_2026 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2026 > 1000000:
    total_diskon_persen_2026 += 10  # Diskon belanja besar

if is_member_2026:
    total_diskon_persen_2026 += 5  # Diskon member

if kode_promo_valid_2026:
    total_diskon_persen_2026 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nomina_diskon_2026 = total_belanja_2026 * (total_diskon_persen_2026 / 100)
total_bayar_2026 = total_belanja_2026 - nomina_diskon_2026

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_2026}% (Rp {nomina_diskon_2026:,.0f})")
print(f"Total Bayar   : Rp {total_bayar_2026:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_2026}%")
# Ouput: Total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid