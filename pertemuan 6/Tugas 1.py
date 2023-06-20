# Latihan  ganjil genap menggunakan function
def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

# Meminta input bilangan dari pengguna
angka = int(input("Masukkan bilangan: "))

# Memanggil fungsi cek_ganjil_genap() dan menampilkan hasilnya
hasil = cek_ganjil_genap(angka)
print("Bilangan tersebut adalah", hasil)



# Latihan ganjil genap mengunakan procedure
def cek_ganjil_genap():
    bilangan = int(input("Masukkan bilangan: "))
    if bilangan % 2 == 0:
        print("Bilangan tersebut adalah Genap")
    else:
        print("Bilangan tersebut adalah Ganjil")

# Memanggil prosedur cek_ganjil_genap()
cek_ganjil_genap()

