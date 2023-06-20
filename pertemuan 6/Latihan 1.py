#Menggunakan Function
print('-------')
def keliling_persegi(sisi):
    keliling = 4 * sisi
    return keliling

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

s = int(input("Masukkan sisi :"))
print("Keliling : %d" % keliling_persegi(s))
print("Luas : %d" % luas_persegi(s))

# Menggunakan Prosedur
def keliling_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    print("Keliling : %d" %keliling)
    print("Luas : %d" %luas)
    

s = int(input("Masukkan panjang sisi :"))
keliling_persegi(s)