# =====================================================
# PERTEMUAN 10 - ALGORITMA DAN PEMROGRAMAN II
# LIST MULTIDIMENSI DAN FUNCTION
# =====================================================

print("=" * 50)
print("1. LIST DI DALAM LIST")
print("=" * 50)

pion_putih = "P"

baris_kedua = []
for i in range(8):
    baris_kedua.append(pion_putih)

print(baris_kedua)


print("\n" + "=" * 50)
print("2. LIST COMPREHENSION")
print("=" * 50)

baris_kedua = [pion_putih for i in range(8)]
print(baris_kedua)


print("\n" + "=" * 50)
print("3. LIST COMPREHENSION BILANGAN GENAP")
print("=" * 50)

bilangan_genap = [i for i in range(2, 21, 2)]
print(bilangan_genap)


print("\n" + "=" * 50)
print("4. ARRAY 2 DIMENSI PAPAN CATUR")
print("=" * 50)

KOSONG = "-"

papan_catur = []

for baris in range(8):
    papan_catur.append([KOSONG] * 8)

for baris in papan_catur:
    print(baris)


print("\n" + "=" * 50)
print("5. ARRAY 2 DIMENSI DENGAN LIST COMPREHENSION")
print("=" * 50)

papan_catur = [[KOSONG for kolom in range(8)] for baris in range(8)]

for baris in papan_catur:
    print(baris)


print("\n" + "=" * 50)
print("6. MENEMPATKAN BENTENG")
print("=" * 50)

BENTENG = "R"

papan_catur = [[KOSONG for kolom in range(8)] for baris in range(8)]

papan_catur[0][0] = BENTENG
papan_catur[0][7] = BENTENG
papan_catur[7][0] = BENTENG
papan_catur[7][7] = BENTENG

for baris in papan_catur:
    print(baris)


print("\n" + "=" * 50)
print("7. MENGAKSES ELEMEN ARRAY 2 DIMENSI")
print("=" * 50)

papan_catur[3][4] = "X"

print("Isi baris 3 kolom 4 =", papan_catur[3][4])


print("\n" + "=" * 50)
print("8. TEMPERATUR 31 HARI x 24 JAM")
print("=" * 50)

temperatur = [[0.0 for jam in range(24)] for hari in range(31)]

print("Hari pertama:")
print(temperatur[0])


print("\n" + "=" * 50)
print("9. MENGISI DATA TEMPERATUR")
print("=" * 50)

temperatur[0][0] = 28.5
temperatur[0][1] = 29.0
temperatur[0][2] = 30.2

print(temperatur[0])


print("\n" + "=" * 50)
print("10. LIST 3 DIMENSI HOTEL")
print("=" * 50)

hotel = [[[False for kamar in range(20)]
          for lantai in range(15)]
          for gedung in range(3)]

print("Array hotel berhasil dibuat")


print("\n" + "=" * 50)
print("11. KAMAR TERISI")
print("=" * 50)

# Gedung 2, lantai 10, kamar 14
hotel[1][9][13] = True

print("Status kamar:", hotel[1][9][13])


print("\n" + "=" * 50)
print("12. KAMAR KOSONG KEMBALI")
print("=" * 50)

# Gedung 1, lantai 5, kamar 2
hotel[0][4][1] = False

print("Status kamar:", hotel[0][4][1])


print("\n" + "=" * 50)
print("13. HITUNG KAMAR KOSONG")
print("=" * 50)

jumlah_kosong = 0

for kamar in hotel[2][14]:
    if kamar == False:
        jumlah_kosong += 1

print("Jumlah kamar kosong:", jumlah_kosong)


print("\n" + "=" * 50)
print("14. FUNGSI BERPARAMETER")
print("=" * 50)

def pesan(nama):
    print("Halo", nama)

pesan("Taufik")


print("\n" + "=" * 50)
print("15. PARAMETER DAN ARGUMEN")
print("=" * 50)

def tampil_angka(angka):
    print("Angka =", angka)

tampil_angka(10)


print("\n" + "=" * 50)
print("16. SHADOWING")
print("=" * 50)

angka = 100

def tampil(angka):
    print("Dalam fungsi =", angka)

tampil(10)

print("Di luar fungsi =", angka)


print("\n" + "=" * 50)
print("17. POSITIONAL ARGUMENT")
print("=" * 50)

def perkenalan(nama_depan, nama_belakang):
    print("Nama :", nama_depan, nama_belakang)

perkenalan("Baek", "Hyunwoo")


print("\n" + "=" * 50)
print("18. KEYWORD ARGUMENT")
print("=" * 50)

perkenalan(
    nama_belakang="Hyunwoo",
    nama_depan="Baek"
)


print("\n" + "=" * 50)
print("19. MIXING ARGUMENT")
print("=" * 50)

perkenalan(
    "Baek",
    nama_belakang="Hyunwoo"
)


print("\n" + "=" * 50)
print("20. FUNGSI DENGAN 3 PARAMETER")
print("=" * 50)

def biodata(nama, umur, kota):
    print("Nama :", nama)
    print("Umur :", umur)
    print("Kota :", kota)

biodata("Taufik", 20, "Cirebon")


print("\n" + "=" * 50)
print("21. PRE-DEFINED ARGUMENT")
print("=" * 50)

def sapa(nama, pesan="Selamat Datang"):
    print(pesan, nama)

sapa("Taufik")
sapa("Taufik", "Selamat Pagi")


print("\n" + "=" * 50)
print("PROGRAM SELESAI")
print("=" * 50)