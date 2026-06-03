# =====================================================
# PERTEMUAN 13 - TUPLE DAN DICTIONARY
# =====================================================

print("=" * 50)
print("1. TIPE SEQUENCE")
print("=" * 50)

data_list = [10, 20, 30, 40]

for item in data_list:
    print(item)


print("\n" + "=" * 50)
print("2. MUTABILITY - LIST (MUTABLE)")
print("=" * 50)

angka = [1, 2, 3]

print("Sebelum:", angka)

angka[1] = 99

print("Sesudah:", angka)


print("\n" + "=" * 50)
print("3. TUPLE (IMMUTABLE)")
print("=" * 50)

data_tuple = (1, 2, 3, 4)

print(data_tuple)

# data_tuple[0] = 100
# Akan error karena tuple immutable


print("\n" + "=" * 50)
print("4. MEMBUAT TUPLE")
print("=" * 50)

tuple1 = (10, 20, 30)

tuple2 = 100, 200, 300

tuple3 = ("Taufik", 20, True)

print(tuple1)
print(tuple2)
print(tuple3)


print("\n" + "=" * 50)
print("5. TUPLE KOSONG DAN SATU ELEMEN")
print("=" * 50)

kosong = ()

satu_elemen = (100,)

bukan_tuple = (100)

print(type(kosong))
print(type(satu_elemen))
print(type(bukan_tuple))


print("\n" + "=" * 50)
print("6. MENGAKSES ELEMEN TUPLE")
print("=" * 50)

mahasiswa = ("Taufik", "Informatika", 20)

print(mahasiswa[0])
print(mahasiswa[1])
print(mahasiswa[2])


print("\n" + "=" * 50)
print("7. OPERASI PADA TUPLE")
print("=" * 50)

t1 = (1, 2, 3)
t2 = (4, 5, 6)

print("len =", len(t1))

print("Gabung =", t1 + t2)

print("Kali =", t1 * 3)

print("2 ada?", 2 in t1)

print("10 tidak ada?", 10 not in t1)


print("\n" + "=" * 50)
print("8. TUPLE UNPACKING")
print("=" * 50)

a, b, c = (10, 20, 30)

print(a)
print(b)
print(c)


print("\n" + "=" * 50)
print("9. MENUKAR NILAI TANPA VARIABEL BANTU")
print("=" * 50)

x = 5
y = 10

print("Sebelum:", x, y)

x, y = y, x

print("Sesudah:", x, y)


print("\n" + "=" * 50)
print("10. DICTIONARY DASAR")
print("=" * 50)

kamus = {
    "cat": "kucing",
    "dog": "anjing",
    "bird": "burung"
}

print(kamus)


print("\n" + "=" * 50)
print("11. DICTIONARY STRING-INTEGER")
print("=" * 50)

nilai = {
    "Andi": 90,
    "Budi": 85,
    "Siti": 95
}

print(nilai)


print("\n" + "=" * 50)
print("12. MENGAKSES NILAI DICTIONARY")
print("=" * 50)

print(kamus["cat"])
print(kamus["dog"])


print("\n" + "=" * 50)
print("13. LEN DICTIONARY")
print("=" * 50)

print("Jumlah item:", len(kamus))


print("\n" + "=" * 50)
print("14. KEYS()")
print("=" * 50)

for key in kamus.keys():
    print(key)


print("\n" + "=" * 50)
print("15. VALUES()")
print("=" * 50)

for value in kamus.values():
    print(value)


print("\n" + "=" * 50)
print("16. ITEMS()")
print("=" * 50)

for key, value in kamus.items():
    print(key, "=", value)


print("\n" + "=" * 50)
print("17. UPDATE()")
print("=" * 50)

kamus.update({
    "fish": "ikan"
})

print(kamus)


print("\n" + "=" * 50)
print("18. POPITEM()")
print("=" * 50)

data = {
    "A": 1,
    "B": 2,
    "C": 3
}

print("Sebelum:", data)

hapus = data.popitem()

print("Item dihapus:", hapus)
print("Sesudah:", data)


print("\n" + "=" * 50)
print("19. COPY()")
print("=" * 50)

asal = {
    "nama": "Taufik",
    "umur": 20
}

salinan = asal.copy()

print("Asal :", asal)
print("Copy :", salinan)


print("\n" + "=" * 50)
print("20. CLEAR()")
print("=" * 50)

data = {
    "A": 1,
    "B": 2
}

print("Sebelum:", data)

data.clear()

print("Sesudah:", data)


print("\n" + "=" * 50)
print("21. KONVERSI TUPLE KE DICTIONARY")
print("=" * 50)

pasangan = (
    ("nama", "Taufik"),
    ("umur", 20),
    ("prodi", "Informatika")
)

hasil = dict(pasangan)

print(hasil)


print("\n" + "=" * 50)
print("22. MENAMBAH ITEM BARU")
print("=" * 50)

mahasiswa = {}

mahasiswa["nama"] = "Taufik"
mahasiswa["umur"] = 20

print(mahasiswa)


print("\n" + "=" * 50)
print("23. MENGUBAH NILAI ITEM")
print("=" * 50)

mahasiswa["umur"] = 21

print(mahasiswa)


print("\n" + "=" * 50)
print("24. MENGHAPUS ITEM TERTENTU")
print("=" * 50)

del mahasiswa["umur"]

print(mahasiswa)


print("\n" + "=" * 50)
print("25. MENGURUTKAN KEY DICTIONARY")
print("=" * 50)

nilai = {
    "Budi": 80,
    "Andi": 90,
    "Siti": 95
}

for nama in sorted(nilai.keys()):
    print(nama, "=", nilai[nama])


print("\n" + "=" * 50)
print("26. CONTOH DICTIONARY NILAI MAHASISWA")
print("=" * 50)

nilai_mahasiswa = {
    "Andi": [80, 90, 85],
    "Budi": [75, 80, 70],
    "Siti": [90, 95, 88]
}

for nama, daftar_nilai in nilai_mahasiswa.items():
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)

    print(nama, "=", round(rata_rata, 2))


print("\n" + "=" * 50)
print("PROGRAM SELESAI")
print("=" * 50)