# ==========================================
# ALGORITMA DAN PEMROGRAMAN II
# PERTEMUAN 4 - INTERACTION WITH THE USER
# ==========================================

# ==========================================
# CONTOH 1 - INPUT SEDERHANA
# ==========================================
print("===== CONTOH 1 =====")

nama = input("Masukkan nama Anda: ")
print("Halo", nama)


# ==========================================
# CONTOH 2 - INPUT DAN KONVERSI INTEGER
# ==========================================
print("\n===== CONTOH 2 =====")

umur = int(input("Masukkan umur Anda: "))
print("Umur Anda adalah", umur, "tahun")


# ==========================================
# CONTOH 3 - INPUT DAN KONVERSI FLOAT
# ==========================================
print("\n===== CONTOH 3 =====")

tinggi = float(input("Masukkan tinggi badan (cm): "))
print("Tinggi badan =", tinggi, "cm")


# ==========================================
# CONTOH 4 - PITAGORAS
# ==========================================
print("\n===== CONTOH 4 =====")

a = float(input("Masukkan sisi a: "))
b = float(input("Masukkan sisi b: "))

c = (a**2 + b**2) ** 0.5

print("Sisi miring =", c)


# ==========================================
# CONTOH 5 - OPERATOR STRING
# ==========================================
print("\n===== CONTOH 5 =====")

kata1 = "Algoritma "
kata2 = "Python"

print(kata1 + kata2)
print("Python " * 3)


# ==========================================
# CONTOH 6 - TYPE CONVERSION
# ==========================================
print("\n===== CONTOH 6 =====")

angka = 100
teks = str(angka)

print(teks)
print(type(teks))

nilai = "25"
nilai_int = int(nilai)

print(nilai_int)
print(type(nilai_int))


# ==========================================
# KUIS 7
# ==========================================
print("\n===== KUIS 7 =====")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

print("Penjumlahan =", a + b)
print("Pengurangan =", a - b)
print("Perkalian =", a * b)
print("Pembagian =", a / b)

print("Selamat kamu sudah pintar matematika")


# ==========================================
# KUIS 8
# ==========================================
print("\n===== KUIS 8 =====")

x = float(input("Masukkan nilai x: "))

# Rumus pada PDF tidak terbaca,
# contoh menggunakan:
y = (3 * x) + 5

print("Nilai y =", y)


# ==========================================
# KUIS 9
# ==========================================
print("\n===== KUIS 9 =====")

jam_mulai = int(input("Jam mulai: "))
menit_mulai = int(input("Menit mulai: "))
durasi = int(input("Durasi acara (menit): "))

total_menit = jam_mulai * 60 + menit_mulai + durasi

jam_selesai = (total_menit // 60) % 24
menit_selesai = total_menit % 60

print(
    "Acara selesai pukul",
    str(jam_selesai).zfill(2) + ":" +
    str(menit_selesai).zfill(2)
)


# ==========================================
# KUIS 10
# ==========================================
print("\n===== KUIS 10 =====")

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
prodi = input("Masukkan Program Studi: ")

print("\n===== DATA MAHASISWA =====")
print("Nama :", nama)
print("NIM  :", nim)
print("Prodi:", prodi)

print("\nProgram selesai.")