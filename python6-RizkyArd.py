print("1.persegi panjang\n")

panjang = int(input("Masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
luas_pp = panjang * lebar

print("luas persegi panjang adalah: ",luas_pp)

print("2.segitiga\n")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))

luas_s = alas * tinggi / 2

print("luas segitiga adalah: ",luas_s)

print("3.jajargenjang\n")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))

luas_jg = alas * tinggi

print("luas jajargenjang adalah: ",luas_jg)

print("4.lingkaran")

ph1 = 22.7
r = int(input("masukan nilai panjang jari-jari: "))

luas_1 = ph1 * r *r

print("luas lingkaran",luas_1)
