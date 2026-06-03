# ==========================================
# ALGORITMA DAN PEMROGRAMAN II
# PERTEMUAN 5 - MAKING DECISIONS IN PYTHON
# ==========================================

# ==========================================
# CONTOH 1 - COMPARISON OPERATOR
# ==========================================

print("===== COMPARISON OPERATOR =====")

x = 0
y = 1
z = 0

print("x == z :", x == z)
print("x == y :", x == y)
print("x != y :", x != y)
print("y > x  :", y > x)
print("x < y  :", x < y)
print("x >= z :", x >= z)
print("x <= y :", x <= y)


# ==========================================
# KUIS 11
# ==========================================

print("\n===== KUIS 11 =====")

n = int(input("Masukkan nilai n: "))

print(n > 100)


# ==========================================
# CONTOH IF TUNGGAL
# ==========================================

print("\n===== IF TUNGGAL =====")

nilai = 85

if nilai >= 75:
    print("Lulus")


# ==========================================
# CONTOH IF ELSE
# ==========================================

print("\n===== IF ELSE =====")

nilai = int(input("Masukkan nilai: "))

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")


# ==========================================
# CONTOH IF ELIF ELSE
# ==========================================

print("\n===== IF ELIF ELSE =====")

nilai = int(input("Masukkan nilai: "))

if nilai >= 85:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
elif nilai >= 60:
    print("Grade C")
else:
    print("Grade D")


# ==========================================
# CONTOH 1
# ==========================================

print("\n===== CONTOH 1 =====")

umur = int(input("Masukkan umur: "))

if umur >= 17:
    print("Boleh membuat SIM")
else:
    print("Belum boleh membuat SIM")


# ==========================================
# CONTOH 2
# ==========================================

print("\n===== CONTOH 2 =====")

angka = int(input("Masukkan angka: "))

if angka > 0:
    print("Positif")
elif angka < 0:
    print("Negatif")
else:
    print("Nol")


# ==========================================
# KUIS 12
# ==========================================

print("\n===== KUIS 12 =====")

a = int(input("Angka pertama : "))
b = int(input("Angka kedua   : "))
c = int(input("Angka ketiga  : "))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

print("Angka terbesar =", terbesar)


# ==========================================
# FUNGSI MAX()
# ==========================================

print("\n===== FUNGSI MAX() =====")

a = 10
b = 25
c = 15

print("Nilai terbesar =", max(a, b, c))


# ==========================================
# KUIS 13
# PROGRAM PAJAK PENGHASILAN
# ==========================================

print("\n===== KUIS 13 =====")

penghasilan = float(input("Masukkan penghasilan tahunan: Rp "))

if penghasilan <= 60000000:
    pajak = penghasilan * 0.05
elif penghasilan <= 250000000:
    pajak = penghasilan * 0.15
elif penghasilan <= 500000000:
    pajak = penghasilan * 0.25
else:
    pajak = penghasilan * 0.30

print("Pajak yang harus dibayar = Rp", format(pajak, ",.0f"))

# ==========================================
print("\n===== PROGRAM SELESAI =====")