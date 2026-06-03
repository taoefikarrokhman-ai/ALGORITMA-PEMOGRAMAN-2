# ==========================================
# ALGORITMA DAN PEMROGRAMAN II
# PERTEMUAN 9 - SORTING & OPERATIONS ON LIST
# ==========================================

# ==========================================
# BUBBLE SORT
# ==========================================

print("===== BUBBLE SORT =====")

my_list = [8, 10, 6, 2, 4]

for i in range(len(my_list) - 1):
    for j in range(len(my_list) - 1 - i):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print("Hasil sorting:", my_list)


# ==========================================
# SORTING DENGAN SWAPPED
# ==========================================

print("\n===== SORTING DENGAN SWAPPED =====")

my_list = [8, 10, 6, 2, 4]

swapped = True

while swapped:
    swapped = False

    for i in range(len(my_list) - 1):

        if my_list[i] > my_list[i + 1]:

            my_list[i], my_list[i + 1] = (
                my_list[i + 1],
                my_list[i]
            )

            swapped = True

print(my_list)


# ==========================================
# BUBBLE SORT INTERAKTIF
# ==========================================

print("\n===== BUBBLE SORT INTERAKTIF =====")

data = []

jumlah = int(input("Berapa jumlah data? "))

for i in range(jumlah):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    data.append(angka)

for i in range(len(data) - 1):
    for j in range(len(data) - 1 - i):

        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("Data setelah diurutkan:", data)


# ==========================================
# SORT() DAN REVERSE()
# ==========================================

print("\n===== SORT() DAN REVERSE() =====")

angka = [8, 10, 6, 2, 4]

angka.sort()
print("Sort naik :", angka)

angka.reverse()
print("Dibalik   :", angka)


# ==========================================
# INNER LIFE OF LIST
# ==========================================

print("\n===== INNER LIFE OF LIST =====")

list_1 = [1]
list_2 = list_1

list_1[0] = 2

print("list_1 =", list_1)
print("list_2 =", list_2)


# ==========================================
# COPY LIST DENGAN SLICE
# ==========================================

print("\n===== COPY LIST DENGAN SLICE =====")

list_1 = [1]
list_2 = list_1[:]

list_1[0] = 2

print("list_1 =", list_1)
print("list_2 =", list_2)


# ==========================================
# SLICE
# ==========================================

print("\n===== SLICE =====")

my_list = [10, 20, 30, 40, 50]

print(my_list[1:4])
print(my_list[:3])
print(my_list[2:])
print(my_list[-4:-1])


# ==========================================
# DEL DAN SLICE
# ==========================================

print("\n===== DEL DAN SLICE =====")

angka = [10, 20, 30, 40, 50, 60]

del angka[1:4]

print(angka)

angka.clear()

print(angka)


# ==========================================
# IN DAN NOT IN
# ==========================================

print("\n===== IN DAN NOT IN =====")

data = [10, 20, 30, 40]

print(20 in data)
print(99 in data)

print(20 not in data)
print(99 not in data)


# ==========================================
# SIMPLE PROGRAM LIST 1
# ==========================================

print("\n===== SIMPLE PROGRAM 1 =====")

numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print(i)


# ==========================================
# SIMPLE PROGRAM LIST 2
# ==========================================

print("\n===== SIMPLE PROGRAM 2 =====")

numbers = [1, 2, 3, 4, 5]

total = 0

for i in numbers:
    total += i

print("Jumlah =", total)


# ==========================================
# SIMPLE PROGRAM LIST 3
# ==========================================

print("\n===== SIMPLE PROGRAM 3 =====")

numbers = [1, 2, 3, 4, 5]

maksimum = max(numbers)
minimum = min(numbers)

print("Maksimum =", maksimum)
print("Minimum =", minimum)


# ==========================================
# KUIS 21
# LOTRE
# ==========================================

print("\n===== KUIS 21 =====")

tebakan = [3, 7, 11, 42, 34, 49]
lotre = [5, 9, 11, 42, 3, 49]

benar = 0

for angka in tebakan:

    if angka in lotre:
        benar += 1

print("Jumlah tebakan yang benar =", benar)


# ==========================================
# KUIS 22
# HILANGKAN DUPLIKAT
# ==========================================

print("\n===== KUIS 22 =====")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique = []

for angka in my_list:

    if angka not in unique:
        unique.append(angka)

print("List awal :", my_list)
print("List unik :", unique)


# ==========================================
print("\n===== PROGRAM SELESAI =====")