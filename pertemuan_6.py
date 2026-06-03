# ==========================================
# ALGORITMA DAN PEMROGRAMAN II
# PERTEMUAN 6 - LOOPS IN PYTHON
# ==========================================

# ==========================================
# CONTOH 1 - WHILE
# ==========================================
print("===== CONTOH WHILE =====")

i = 1

while i <= 5:
    print("Perulangan ke-", i)
    i += 1


# ==========================================
# KUIS 15
# GAME TEBAK ANGKA RAHASIA
# ==========================================
print("\n===== KUIS 15 =====")

secret_number = 777

tebakan = int(input("Masukkan angka rahasia: "))

while tebakan != secret_number:
    print("hahaha! kamu nyangkut deh di Loop saya")
    tebakan = int(input("Masukkan angka lagi: "))

print("Selamat, Muggle! kamu bebas sekarang!")


# ==========================================
# CONTOH FOR
# ==========================================
print("\n===== CONTOH FOR =====")

for i in range(1, 11):
    print(i)


# ==========================================
# CONTOH RANGE()
# ==========================================
print("\n===== CONTOH RANGE =====")

for i in range(5):
    print(i)

print()

for i in range(2, 11, 2):
    print(i)


# ==========================================
# BREAK
# ==========================================
print("\n===== BREAK =====")

for i in range(1, 11):

    if i == 6:
        break

    print(i)


# ==========================================
# CONTINUE
# ==========================================
print("\n===== CONTINUE =====")

for i in range(1, 11):

    if i == 6:
        continue

    print(i)


# ==========================================
# KUIS 16
# TEBAK ANGKA DENGAN BREAK
# ==========================================
print("\n===== KUIS 16 =====")

secret_number = 777

while True:

    tebakan = int(input("Masukkan angka rahasia: "))

    if tebakan == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang!")
        break

    print("hahaha! kamu nyangkut deh di Loop saya")


# ==========================================
# KUIS 17
# HAPUS HURUF VOKAL
# ==========================================
print("\n===== KUIS 17 =====")

kata = input("Masukkan kata: ").upper()

for huruf in kata:

    if huruf in ["A", "I", "U", "E", "O"]:
        continue

    print(huruf)


# ==========================================
# WHILE ELSE
# ==========================================
print("\n===== WHILE ELSE =====")

x = 1

while x <= 5:
    print(x)
    x += 1
else:
    print("Perulangan selesai")


# ==========================================
# FOR ELSE
# ==========================================
print("\n===== FOR ELSE =====")

for i in range(1, 6):
    print(i)
else:
    print("Loop selesai")


# ==========================================
# LOGICAL OPERATOR
# ==========================================
print("\n===== LOGICAL OPERATOR =====")

a = True
b = False

print("a and b =", a and b)
print("a or b  =", a or b)
print("not a   =", not a)


# ==========================================
# BITWISE OPERATOR
# ==========================================
print("\n===== BITWISE OPERATOR =====")

x = 10
y = 4

print("x & y =", x & y)
print("x | y =", x | y)
print("x ^ y =", x ^ y)
print("~x =", ~x)


# ==========================================
# BINARY SHIFT
# ==========================================
print("\n===== BINARY SHIFT =====")

angka = 8

print("Angka awal =", angka)

print("Geser kiri 1 bit =", angka << 1)
print("Geser kiri 2 bit =", angka << 2)

print("Geser kanan 1 bit =", angka >> 1)
print("Geser kanan 2 bit =", angka >> 2)


# ==========================================
# KUIS 18
# CONTOH SHIFTING
# ==========================================
print("\n===== KUIS 18 =====")

nilai = 16

print("Nilai awal :", nilai)
print("nilai << 1 :", nilai << 1)
print("nilai << 2 :", nilai << 2)

print("nilai >> 1 :", nilai >> 1)
print("nilai >> 2 :", nilai >> 2)

print("\nPenjelasan:")
print("<< menggeser bit ke kiri (perkalian 2^n)")
print(">> menggeser bit ke kanan (pembagian 2^n)")


# ==========================================
print("\n===== PROGRAM SELESAI =====")