# Algo II Pertemuan 2 - Python Literals & Operators
# Gabungan contoh materi dalam satu file

print("=== LITERALS ===")
print("Hello World")      # String literal
print(123)                # Integer literal

print("\n=== INTEGERS ===")
a = 11111111
b = 11_111_111
print(a)
print(b)

print("\nBilangan Oktal dan Hexadesimal")
print(0o123)   # Oktal
print(0x123)   # Hexadesimal

print("\n=== FLOATS ===")
print(0.4)
print(.4)
print(4.0)
print(4.)
print(3e2)     # 3 x 10^2
print(3E2)

print("\n=== STRINGS ===")
print("Python")
print('Algoritma dan Pemrograman')

print("\n=== BOOLEAN ===")
print(True)
print(False)
print(10 > 5)
print(10 < 5)

print("\n=== BASIC OPERATORS ===")
x = 10
y = 3

print("Penjumlahan :", x + y)
print("Pengurangan :", x - y)
print("Perkalian   :", x * y)
print("Pembagian   :", x / y)
print("Floor Div   :", x // y)
print("Modulo      :", x % y)
print("Pangkat     :", x ** y)

print("\n=== UNARY OPERATORS ===")
print(+10)
print(-10)

print("\n=== PRIORITAS OPERATOR ===")
print(2 + 3 * 4)
print((2 + 3) * 4)

print("\n=== RIGHT-SIDED BINDING (EXPONENT) ===")
print(2 ** 3 ** 2)  # 2 ** (3 ** 2)

print("\n=== CONTOH KUIS ===")
hasil = 2 + 3 * 2 ** 2
print("2 + 3 * 2 ** 2 =", hasil)

print("\nProgram selesai.")
