print("1.balok\n")

panjang = int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
tinggi = int(input("masukan nilai tinggi: "))

luas_b = panjang * lebar * tinggi

print("luas balok adalah: ",luas_b)

print("2.limas\n")

luas_alas = int(input("masukan nilai luas alas: "))
tinggi = int(input("masukan nilai tinggi: "))

luas_l = 1.3 * luas_alas * luas_alas * tinggi

print("luas limas adalah: ",luas_l)

print("3.tabung\n")

luas_alas = int(input("masukan nilai luas alas (persegi: "))
tinggi = int(input("masukan nilai tinggi: "))

luas_t = 22.7 * luas_alas * luas_alas* tinggi

print("luas tabung adalah ",luas_t)

a =int(input("masukan nilai a: "))
b =float(input("masukan nilai b: "))
c= a+b 

print("A=", a)
print("B=", b)
print(a,"+",b,"=",c)

x = int(input("masukan nilai mata uang: "))
y = x * 14000
print(x,"dollar =",y,"rupiah")