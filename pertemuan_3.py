# =====================================
# ALGORITMA DAN PEMROGRAMAN II
# PERTEMUAN 3 - VARIABLES
# =====================================

print("===== CONTOH 1 : MEMBUAT VARIABEL =====")

nama = "Taufik"
umur = 20

print("Nama :", nama)
print("Umur :", umur)


# =====================================
print("\n===== CONTOH 2 : MENGUBAH NILAI VARIABEL =====")

nilai = 10
print("Nilai awal =", nilai)

nilai = 20
print("Nilai baru =", nilai)


# =====================================
print("\n===== CONTOH 3 : NAMA VARIABEL YANG BENAR =====")

nama_mahasiswa = "Andi"
umur1 = 19
_IPK = 3.75

print(nama_mahasiswa)
print(umur1)
print(_IPK)


# =====================================
print("\n===== CONTOH 4 : SHORTCUT OPERATOR =====")

angka = 10
print("Nilai awal =", angka)

angka += 5
print("Setelah += 5 =", angka)

angka -= 3
print("Setelah -= 3 =", angka)

angka *= 2
print("Setelah *= 2 =", angka)

angka /= 4
print("Setelah /= 4 =", angka)


# =====================================
print("\n===== CONTOH 5 : TEOREMA PYTHAGORAS =====")

a = 3
b = 4

c = (a**2 + b**2) ** 0.5

print("Sisi a =", a)
print("Sisi b =", b)
print("Hipotenusa =", c)


# =====================================
print("\n===== KUIS 3 =====")

Ayu = 50000
Bagus = 75000
Citra = 100000

print(Ayu, Bagus, Citra, sep=", ")

jumlahTabungan = Ayu + Bagus + Citra

print("Jumlah Tabungan adalah", jumlahTabungan)


# =====================================
print("\n===== KUIS 4 =====")

# Kilometer ke Mil
kilometer = 10
mil = round(kilometer / 1.61, 2)

print(kilometer, "Kilometer =", mil, "Mil")

# Mil ke Kilometer
mil2 = 10
kilometer2 = round(mil2 * 1.61, 2)

print(mil2, "Mil =", kilometer2, "Kilometer")


# =====================================
print("\n===== KUIS 5 =====")

# Karena rumus pada PDF terpotong,
# contoh menggunakan persamaan:
# y = x² + 2x + 1

x = 0
y = x**2 + 2*x + 1
print("x =", x, "-> y =", y)

x = 1
y = x**2 + 2*x + 1
print("x =", x, "-> y =", y)

x = -1
y = x**2 + 2*x + 1
print("x =", x, "-> y =", y)

# =====================================
print("\n===== SELESAI =====")