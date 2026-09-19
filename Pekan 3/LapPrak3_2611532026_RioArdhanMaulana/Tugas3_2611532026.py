# TUGAS PEKAN 3
# Sistem Simulasi Transaksi dan Validasi Akses Toko

print("==============================================")
print("   SISTEM SIMULASI TRANSAKSI DAN AKSES TOKO")
print("==============================================")

# Input data pelanggan
nama_2026 = input("Masukkan nama pelanggan            : ")
status_2026 = input("Status pelanggan (member/non-member): ").lower()
umur_2026 = int(input("Masukkan umur pelanggan            : "))

# Input data transaksi
harga_2026 = float(input("Masukkan harga barang              : Rp "))
jumlah_2026 = int(input("Masukkan jumlah barang             : "))

# Input promo
kode_promo_2026 = input("Masukkan kode promo                : ").upper()

print("\n==============================================")
print("             HASIL TRANSAKSI")
print("==============================================")

# Menghitung subtotal
subtotal_2026 = harga_2026 * jumlah_2026

print(f"Nama pelanggan : {nama_2026}")
print(f"Harga barang   : Rp {harga_2026:,.0f}")
print(f"Jumlah barang  : {jumlah_2026}")
print(f"Subtotal       : Rp {subtotal_2026:,.0f}")

# Menentukan diskon
if status_2026 == "member" and subtotal_2026 >= 100000:
    diskon_2026 = subtotal_2026 * 0.10
    status_diskon_2026 = "Member - Diskon 10%"
elif status_2026 == "member":
    diskon_2026 = subtotal_2026 * 0.05
    status_diskon_2026 = "Member - Diskon 5%"
else:
    diskon_2026 = 0
    status_diskon_2026 = "Non-member - Tidak mendapat diskon"

# Menghitung total setelah diskon
total_setelah_diskon_2026 = subtotal_2026 - diskon_2026

# Daftar kode promo
promo_tersedia_2026 = ["HEMAT10", "HEMAT20", "PROMO"]

# Validasi kelayakan promo
layak_promo_2026 = (
    status_2026 == "member"
    and umur_2026 >= 17
    and subtotal_2026 >= 150000
    and kode_promo_2026 in promo_tersedia_2026
)

# Menentukan potongan promo
if layak_promo_2026:
    if kode_promo_2026 == "HEMAT10":
        potongan_promo_2026 = total_setelah_diskon_2026 * 0.10
    elif kode_promo_2026 == "HEMAT20":
        potongan_promo_2026 = total_setelah_diskon_2026 * 0.20
    else:
        potongan_promo_2026 = 10000
else:
    potongan_promo_2026 = 0

# Menghitung total pembayaran
total_bayar_2026 = (
    total_setelah_diskon_2026 - potongan_promo_2026
)

# Validasi hak akses promo
akses_promo_2026 = (
    status_2026 == "member"
    and umur_2026 >= 17
    and kode_promo_2026 in promo_tersedia_2026
)

# Menampilkan hasil
print("----------------------------------------------")
print(f"Status pelanggan    : {status_2026}")
print(f"Status diskon       : {status_diskon_2026}")
print(f"Diskon              : Rp {diskon_2026:,.0f}")
print(
    f"Total setelah diskon: "
    f"Rp {total_setelah_diskon_2026:,.0f}"
)

print("----------------------------------------------")

if akses_promo_2026:
    print("Hak akses promo     : DIBERIKAN")
else:
    print("Hak akses promo     : DITOLAK")

if layak_promo_2026:
    print("Status promo        : PROMO BERHASIL DIGUNAKAN")
    print(f"Potongan promo      : Rp {potongan_promo_2026:,.0f}")
else:
    print("Status promo        : TIDAK MEMENUHI SYARAT")
    print("Potongan promo      : Rp 0")

print("----------------------------------------------")
print(f"TOTAL PEMBAYARAN    : Rp {total_bayar_2026:,.0f}")
print("==============================================")
print("        TERIMA KASIH TELAH BERBELANJA")
print("==============================================")