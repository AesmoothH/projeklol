import random

angkaBenar = random.randrange(10)
print( angkaBenar )

print("_______________TEBAK JOMOK______________________")
print("Kesempatan anda hanya 7x")
kesempatan = 0
while True:
    angkaJawaban = int( input("Angka Tebakan Anda : ") )
    if angkaJawaban != angkaBenar and kesempatan == 7:
        print("HAAAAAAAAHHAHHAHAHA")
        break
    elif angkaJawaban < angkaBenar:
        print("Angka kamu Benar")
        kesempatan += 1
    elif angkaJawaban > angkaBenar:
        print("Angka kamu Salah")
        kesempatan += 1
    elif angkaJawaban == angkaBenar:
        print("yeayaayay")