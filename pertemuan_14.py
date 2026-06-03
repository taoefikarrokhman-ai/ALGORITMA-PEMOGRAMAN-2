# Exceptions in Python - Pertemuan 14
# Gabungan contoh kode dari materi

print("=== CONTOH 1: Menangani Exception Sederhana ===")

while True:
    try:
        bilangan = int(input("Masukkan bilangan natural: "))
        print("Kebalikan dari", bilangan, "adalah", 1 / bilangan)
        break
    except:
        print("Peringatan: bilangan yang dimasukkan bukan bilangan bulat!")


print("\n=== CONTOH 2: Menangani Multiple Exception ===")

while True:
    try:
        bilangan = int(input("Masukkan bilangan natural: "))
        print("Kebalikan dari", bilangan, "adalah", 1 / bilangan)
        break

    except ValueError:
        print("Peringatan: bilangan yang dimasukkan bukan bilangan bulat!")

    except ZeroDivisionError:
        print("Peringatan! Tidak bisa membagi dengan 0")

    except Exception:
        print("Maaf sepertinya ada yang salah... :(")


print("\n=== CONTOH JENIS-JENIS EXCEPTION ===")

# ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# ValueError
try:
    angka = int("abc")
except ValueError as e:
    print("ValueError:", e)

# TypeError
try:
    my_list = [1, 2, 3]
    print(my_list[0.5])
except TypeError as e:
    print("TypeError:", e)

# AttributeError
try:
    my_list = [1, 2, 3]
    my_list.depend(4)
except AttributeError as e:
    print("AttributeError:", e)

print("\nProgram selesai.")
