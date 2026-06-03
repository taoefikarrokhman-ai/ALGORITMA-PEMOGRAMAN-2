# =====================================================
# PERTEMUAN 11 - RETURNING A RESULT FROM A FUNCTION
# =====================================================

print("=" * 50)
print("1. RETURN TANPA EKSPRESI")
print("=" * 50)

def fungsi_harapan(harapan):
    if harapan == False:
        return

    print("Harapan masih ada!")

fungsi_harapan(True)
fungsi_harapan(False)


print("\n" + "=" * 50)
print("2. RETURN DENGAN EKSPRESI")
print("=" * 50)

def fungsi_malas():
    return 123

x = fungsi_malas()

print("Nilai x =", x)


print("\n" + "=" * 50)
print("3. HASIL RETURN DIABAIKAN")
print("=" * 50)

def fungsi_malas():
    print("Fungsi dipanggil")
    return 123

fungsi_malas()


print("\n" + "=" * 50)
print("4. NILAI NONE")
print("=" * 50)

def tanpa_return():
    print("Fungsi tanpa return")

hasil = tanpa_return()

print("Nilai hasil =", hasil)
print("Apakah None?", hasil is None)


print("\n" + "=" * 50)
print("5. RETURN NONE SECARA EKSPLISIT")
print("=" * 50)

def contoh_none():
    return None

nilai = contoh_none()

if nilai is None:
    print("Nilai berisi None")


print("\n" + "=" * 50)
print("6. LIST SEBAGAI ARGUMEN FUNGSI")
print("=" * 50)

def tampilkan_list(data):
    for item in data:
        print(item)

angka = [10, 20, 30, 40, 50]

tampilkan_list(angka)


print("\n" + "=" * 50)
print("7. LIST SEBAGAI HASIL FUNGSI")
print("=" * 50)

def buat_list():
    return [1, 2, 3, 4, 5]

hasil_list = buat_list()

print(hasil_list)


print("\n" + "=" * 50)
print("8. MENJUMLAHKAN ELEMEN LIST")
print("=" * 50)

def jumlahkan(data):
    total = 0

    for item in data:
        total += item

    return total

angka = [5, 10, 15, 20]

print("Jumlah =", jumlahkan(angka))


print("\n" + "=" * 50)
print("9. MENCARI NILAI TERBESAR")
print("=" * 50)

def nilai_maksimum(data):
    terbesar = data[0]

    for item in data:
        if item > terbesar:
            terbesar = item

    return terbesar

data = [45, 78, 23, 99, 12]

print("Nilai terbesar =", nilai_maksimum(data))


print("\n" + "=" * 50)
print("10. MENCARI NILAI TERKECIL")
print("=" * 50)

def nilai_minimum(data):
    terkecil = data[0]

    for item in data:
        if item < terkecil:
            terkecil = item

    return terkecil

data = [45, 78, 23, 99, 12]

print("Nilai terkecil =", nilai_minimum(data))


print("\n" + "=" * 50)
print("11. MENGEMBALIKAN DUA NILAI")
print("=" * 50)

def hitung(a, b):
    jumlah = a + b
    kali = a * b

    return jumlah, kali

jml, kl = hitung(5, 3)

print("Jumlah =", jml)
print("Perkalian =", kl)


print("\n" + "=" * 50)
print("12. RETURN DENGAN KONDISI")
print("=" * 50)

def cek_genap(angka):
    if angka % 2 == 0:
        return True
    else:
        return False

print("10 genap?", cek_genap(10))
print("15 genap?", cek_genap(15))


print("\n" + "=" * 50)
print("13. RETURN STRING")
print("=" * 50)

def salam(nama):
    return f"Halo {nama}"

pesan = salam("Taufik")

print(pesan)


print("\n" + "=" * 50)
print("14. RETURN LIST BARU")
print("=" * 50)

def kuadrat_list(data):
    hasil = []

    for item in data:
        hasil.append(item ** 2)

    return hasil

angka = [1, 2, 3, 4, 5]

print(kuadrat_list(angka))


print("\n" + "=" * 50)
print("PROGRAM SELESAI")
print("=" * 50)