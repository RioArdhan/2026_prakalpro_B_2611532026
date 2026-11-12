# Name : Rio Ardhan Maulana
# NIM : 2611532026
# Question 7

name = "Rio Ardhan Maulana"
nim = "261153206"
space_index = name.find(" ")
first_name = name[:space_index] if space_index != -1 else name
username = first_name.lower() + nim[-3:]
angkatan = "20" + nim[:2]
print("=" * 30)
print("KARTU MAHASISWA".center(30))
print("=" * 30)
print(f"{'Nama':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Angkatan':<10}: {angkatan}")
print("=" * 30)