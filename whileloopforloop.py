# membangkitkan nilai random()
import random

inputan dari User
n = int(input("masukkan jumlah n : "))
for i in range(n):
    while 1:
        n = random.random()
        if n < 0.5:
            break
    print(n)
print('selesai')
