# ==========================================
# ALGORITMA DAN PEMROGRAMAN II
# PERTEMUAN 7 - LISTS IN PYTHON
# ==========================================

# ==========================================
# CONTOH 1 - MEMBUAT LIST
# ==========================================

print("===== MEMBUAT LIST =====")

angka = [10, 5, 8, 3, 7]

print(angka)


# ==========================================
# CONTOH 2 - INDEXING LIST
# ==========================================

print("\n===== INDEXING LIST =====")

angka = [10, 20, 30, 40, 50]

print("List awal :", angka)

angka[0] = 99
print("Setelah index 0 diubah :", angka)

angka[1] = angka[4]
print("Setelah copy index 4 ke index 1 :", angka)


# ==========================================
# CONTOH 3 - MENGAKSES ISI LIST
# ==========================================

print("\n===== MENGAKSES LIST =====")

buah = ["Apel", "Mangga", "Jeruk"]

print(buah)
print(buah[0])
print(buah[1])
print(buah[2])


# ==========================================
# CONTOH 4 - LEN()
# ==========================================

print("\n===== LEN() =====")

data = [1, 2, 3, 4, 5]

print("Panjang list =", len(data))


# ==========================================
# CONTOH 5 - DEL
# ==========================================

print("\n===== DEL =====")

angka = [10, 20, 30, 40, 50]

print("Sebelum :", angka)

del angka[2]

print("Sesudah :", angka)


# ==========================================
# CONTOH 6 - NEGATIVE INDEX
# ==========================================

print("\n===== NEGATIVE INDEX =====")

number = [10, 20, 30, 40]

print(number[-1])
print(number[-2])
print(number[-4])


# ==========================================
# KUIS 19
# ==========================================

print("\n===== KUIS 19 =====")

nilai = [75, 80, 90, 85, 100]

print("Data nilai :", nilai)

print("Nilai pertama :", nilai[0])
print("Nilai terakhir :", nilai[-1])
print("Jumlah elemen :", len(nilai))


# ==========================================
# APPEND()
# ==========================================

print("\n===== APPEND() =====")

data = [1, 2, 3]

data.append(4)

print(data)


# ==========================================
# INSERT()
# ==========================================

print("\n===== INSERT() =====")

data = [1, 2, 3]

data.insert(1, 99)

print(data)


# ==========================================
# CONTOH 1 APPEND DAN INSERT
# ==========================================

print("\n===== CONTOH APPEND & INSERT =====")

angka = []

angka.append(10)
angka.append(20)
angka.append(30)

angka.insert(1, 15)

print(angka)


# ==========================================
# CONTOH 2 LIST KOSONG
# ==========================================

print("\n===== LIST KOSONG =====")

my_list = []

for i in range(5):
    nilai = int(input(f"Masukkan angka ke-{i+1}: "))
    my_list.append(nilai)

print(my_list)


# ==========================================
# MENJUMLAHKAN ISI LIST
# ==========================================

print("\n===== MENJUMLAHKAN LIST =====")

my_list = [10, 20, 30, 40]

total = 0

for i in my_list:
    total += i

print("Total =", total)


# ==========================================
# LIST IN ACTION 1
# MENUKAR NILAI 2 VARIABEL
# ==========================================

print("\n===== SWAP VARIABEL =====")

a = 10
b = 20

print("Sebelum :", a, b)

temp = a
a = b
b = temp

print("Sesudah :", a, b)


# ==========================================
# LIST IN ACTION 2
# SWAP DENGAN PYTHON
# ==========================================

print("\n===== SWAP PYTHON =====")

a = 100
b = 200

print("Sebelum :", a, b)

a, b = b, a

print("Sesudah :", a, b)


# ==========================================
# MEMBALIK LIST
# ==========================================

print("\n===== MEMBALIK LIST =====")

my_list = [1, 2, 3, 4, 5]

panjang = len(my_list)

for i in range(panjang // 2):
    my_list[i], my_list[panjang - i - 1] = (
        my_list[panjang - i - 1],
        my_list[i]
    )

print(my_list)


# ==========================================
# KUIS 20
# ==========================================

print("\n===== KUIS 20 =====")

exo = []

# langkah 2
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")

# langkah 3
anggota = [
    "DO",
    "Baekhyun",
    "Kris",
    "Lay",
    "Luhan",
    "Tao",
    "Chen"
]

for nama in anggota:
    exo.append(nama)

print("Setelah tambah anggota:")
print(exo)

# langkah 4
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")

print("\nSetelah hapus Kris, Luhan, Tao:")
print(exo)

# langkah 5
exo.insert(len(exo) - 2, "Xiumin")

print("\nHasil akhir:")
print(exo)

# ==========================================
print("\n===== PROGRAM SELESAI =====")