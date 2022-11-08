# Program mencari bilangan terbesar dari 2 buah bilangan
# Meminta inputan dari user dengan menggunakan fitur destruksi
a, b = (
    int(input('Masukkan nilai a : ')),
    int(input('Masukkan nilai b : '))
)

if b > a:
    print(b, "adalah bilangan terbesar dari ", a)
print("ini diluar pernyataan if")
