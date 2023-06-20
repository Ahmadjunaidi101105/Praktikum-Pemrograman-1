# Menggunakan Function
print('-------')
def keliling_lingkaran(jari):
    keliling = 2 * 3.14 * jari
    return keliling

def luas_lingkaran(jari):
    luas = 3.14 * (jari*jari)
    return luas

s = int(input("Masukkan jari-jari :"))
print("Keliling : %d" % keliling_lingkaran(s))
print("Luas : %d" % luas_lingkaran(s))


# Menggunakan procedure
import math

def hitung_luas_dan_keliling():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    
    luas = math.pi * jari_jari ** 2
    keliling = 2 * math.pi * jari_jari
    
    print("Luas lingkaran:", luas)
    print("Keliling lingkaran:", keliling)

# Memanggil prosedur hitung_luas_dan_keliling()
hitung_luas_dan_keliling()
