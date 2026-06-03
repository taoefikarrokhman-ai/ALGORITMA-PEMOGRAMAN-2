# =====================================================
# PERTEMUAN 12 - SCOPE & MULTI PARAMETER FUNCTION
# =====================================================

print("=" * 50)
print("1. SCOPE LOKAL")
print("=" * 50)

def contoh_scope():
    angka = 10
    print("Di dalam fungsi =", angka)

contoh_scope()

# print(angka)  # ERROR karena scope lokal


print("\n" + "=" * 50)
print("2. SCOPE GLOBAL")
print("=" * 50)

angka = 100

def tampil():
    print("Di dalam fungsi =", angka)

tampil()
print("Di luar fungsi =", angka)


print("\n" + "=" * 50)
print("3. SHADOWING")
print("=" * 50)

nilai = 50

def contoh_shadowing():
    nilai = 20
    print("Dalam fungsi =", nilai)

contoh_shadowing()
print("Luar fungsi =", nilai)


print("\n" + "=" * 50)
print("4. GLOBAL KEYWORD")
print("=" * 50)

counter = 0

def tambah_counter():
    global counter
    counter += 1

tambah_counter()
tambah_counter()
tambah_counter()

print("Counter =", counter)


print("\n" + "=" * 50)
print("5. MULTI PARAMETER FUNCTION")
print("=" * 50)

def tambah(a, b):
    return a + b

hasil = tambah(10, 20)

print("Hasil =", hasil)


print("\n" + "=" * 50)
print("6. FUNGSI DENGAN 3 PARAMETER")
print("=" * 50)

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

print("Volume =", volume_balok(5, 4, 3))


print("\n" + "=" * 50)
print("7. FUNGSI CEK SEGITIGA")
print("=" * 50)

def segitiga(a, b, c):
    if a + b <= c:
        return False

    if a + c <= b:
        return False

    if b + c <= a:
        return False

    return True

print(segitiga(3, 4, 5))
print(segitiga(1, 2, 5))


print("\n" + "=" * 50)
print("8. VERSI SINGKAT SEGITIGA")
print("=" * 50)

def segitiga_singkat(a, b, c):
    return (
        a + b > c and
        a + c > b and
        b + c > a
    )

print(segitiga_singkat(5, 5, 5))
print(segitiga_singkat(2, 3, 10))


print("\n" + "=" * 50)
print("9. FAKTORIAL ITERATIF")
print("=" * 50)

def faktorial(n):
    hasil = 1

    for i in range(1, n + 1):
        hasil *= i

    return hasil

print("5! =", faktorial(5))
print("7! =", faktorial(7))


print("\n" + "=" * 50)
print("10. FIBONACCI ITERATIF")
print("=" * 50)

def fibonacci(n):
    if n <= 0:
        return None

    if n == 1 or n == 2:
        return 1

    fib1 = 1
    fib2 = 1

    for i in range(3, n + 1):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib

    return fib2

for i in range(1, 11):
    print(fibonacci(i), end=" ")

print()


print("\n" + "=" * 50)
print("11. REKURSIF FAKTORIAL")
print("=" * 50)

def faktorial_rekursif(n):
    if n == 0 or n == 1:
        return 1

    return n * faktorial_rekursif(n - 1)

print("5! =", faktorial_rekursif(5))
print("6! =", faktorial_rekursif(6))


print("\n" + "=" * 50)
print("12. REKURSIF FIBONACCI")
print("=" * 50)

def fibonacci_rekursif(n):
    if n <= 0:
        return None

    if n == 1 or n == 2:
        return 1

    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)

for i in range(1, 11):
    print(fibonacci_rekursif(i), end=" ")

print()


print("\n" + "=" * 50)
print("PROGRAM SELESAI")
print("=" * 50)