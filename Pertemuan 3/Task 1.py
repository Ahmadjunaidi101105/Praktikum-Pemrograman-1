hh = int(input("masukan jam saat ini: "))
mm = int(input("masukan menit saat ini: "))
ss = int(input("masukan detik saat ini: "))

total_detik = hh*3600 + mm*60 +ss*60
print(total_detik)

huruf = str(input("masukan huruf: "))
if (huruf == "a" or "A"):
    print("huruf vokal")
elif (huruf == "i" or huruf == "I"):
    print("huruf vokal") 
elif (huruf == "u" or huruf == "U")   :
    print("huruf vokal")
elif(huruf == "e" or huruf == "E"):
    print("huruf vokal")
elif (huruf == "o" or huruf == "0"):
    print("huruf vokal")
else:
    print("huruf konsonan")                
    