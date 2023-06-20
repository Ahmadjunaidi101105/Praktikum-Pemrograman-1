# contoh program menggunakan if-elif-else
T = real

if T <= 0:
    print("T kurang  dari 0")
elif ifx == 0:
    print("x sama dengan 0")
else:
    print("x lebih besar dari 0")



suhu = int(input("masukan Suhu: "))
if suhu <= 0:
    print("pada suhu", suhu , "derajat celcius, air akan berwujud es")  
    
elif suhu > 0 and suhu < 100:
     print("pada suhu", suhu , "derajat celcius, air akan berwujud air")  

else:
    print("pada suhu", suhu , "derajat celcius, air akan berwujud gas")        

gender = input("perempuan atau laki-laki ? (L/P)")

if(gender =='L'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Bapak!") 
    elif(status == 'N'):
        print("Hallo Mas!")
    else:
        print("Tidak ada dalam pilihan") 
elif(gender == 'P'):
    status = input("Anda sudah menikah atau belum? (Y/N): ") 
    if(status == 'Y'): 
        print("Hallo Ibu!")
    elif(status == 'N'):
        print("Hallo Mba!")
    else:
        print("Tidak ada dalam pilihan")
else:
    print("tidak ada dalam pilihan")



print("===========INPUT==========")
nama= input("Nama: ")
jk = input("Jenis Kelamin (L/P): ")
agama = int(input("Agama: "))
#1-Islam, 2-Protestan, 3-Katolik, 4-Hindu, 5=Budha
if(agama==1):
    agama = "Islam"
elif (agama==2):
    agama = "Protestan"
elif(agama==3):
    agama = "Katolik"
elif(agama==4):
    agama = "Hindu"
elif(agama==5):
    agama = "Budha"
else:
    agama = "Agama tidak ditemukan"

print(" =====OUTPUT========")
print("Nama: ",nama)
print("Jenis Kelamin: ",jk)
print("Agama: ",agama)

nama = input('masukan nama salesman = ')
NilaiPenjualan = float(input('masukan nilai penjualan = Rp = '))

Komisi = 0.05 * NilaiPenjualan

print('Komisi', nama, ' =Rp.', Komisi)

# #PERSOALAN PERTUKARAN
# A = 8
# B = 5

# print(A,B)

# C = A
# A = B
# B = C

# print(A,B)


#MENGHITUNG GAJI PAJAK 

gaji = 4000000
print("Gaji :", gaji)
#pajak
pajak = gaji *(15/100)


#if satu kondisi
nilai = int (input("Masukan bilangan bulat: "))
if (nilai > 0):
    print("Bilangan", nilai, "merupakan bilangan positif")
elif (nilai < 0): #if dua kondisi menggunakan 
    print("Bilangan", nilai, "Merupakan bilangan Negatif")
else:
    print("Bilangan nol")        
    
bilangan = int(input("Maasukan Bilangan: "))
if(bilangan % 2 == 0):
    print("Bilangan", bilangan ,"merupakan bilangan genap")
else:
    print("Bilangan", bilangan , "Merupakan bilangan ganjil")    
    
 
bilangan = int(input("masukan bilangan: "))

if(bilangan > 0):
    print(bilangan, "merupakan bilangan positif")
elif(bilangan < 0):
    print(bilangan ,"merupakan bilangan negatif")    
else:
    print(bilangan ,"anda memasukan bilangan nol")    
    
    

 
 
 
 
# hh = int(input("masukan jam saat ini: "))
# mm = int(input("masukan menit saat ini: "))
# ss = int(input("masukan detik saat ini: "))

# total_detik = hh*3600 + mm*60 +ss*60
# print(total_detik)

# huruf = str(input("masukan huruf: "))
# if (huruf == "a" or "A"):
#     print("huruf vokal")
# elif (huruf == "i" or huruf == "I"):
#     print("huruf vokal") 
# elif (huruf == "u" or huruf == "U")   :
#     print("huruf vokal")
# elif(huruf == "e" or huruf == "E"):
#     print("huruf vokal")
# elif (huruf == "o" or huruf == "0"):
#     print("huruf vokal")
# else:
#     print("huruf konsonan")                
    
    
   # mencari angka kevalidan 
nilai = int(input("masukkan nilai : "))
pembagi = int(input("masukkan nilai pembagi : "))

hasil = nilai/pembagi

if (hasil == int(hasil)):
    print("hasil valid")
else : 
    print("hasil tidak valid")
    
#     #menghitung tahun kabisat
# tahun = int(input("masukkan tahun saat ini : "))
# hasil = tahun%4
# if (hasil == 0):
#     print("tahun kabisat")
# else:
#     print("bukan tahun kabisat")