# --- non scalar veri tiplerinde for kullanimi
notlar= [79,67,35,14]
for e in notlar:
    print(e)    # bu forda liste elemanları teker teker yazılır


#not ortalamasini bulan for dongusu
t=0
for e in notlar:
    t +=e
ortalama = t / len(notlar)
print("Not ortalamasi :",ortalama)

# list degerlerini degistirmek icin range(len(notlar)) kullanilabilir.
print("----------------------------------------")
for i in range(len(notlar)):
    notlar[i]+=5

print(notlar)
print("----------------------------------------")
# sayi bulan for dongusu
l1 = [1,2,3,4,5,6,7,8,9,0]
x = int(input("Hangi sayiyi bulalim ? : "))
for i in l1:
    print(i)
    if(i == x):
        print("İstediginiz sayi bulundu ...")
        break
print("----------------------------------------")
#tuplelarda for kullanimi
t1=(1,2,3,4,5,6)
for i in t1:
    print(i)

print("----------------------------------------")
# dictionarylerde for kullanimi
#dictionarylerde iterasyon keyler üzerinden olur
dic1 = {"samet":44,"faruk":56,"batu":42}
for i in dic1:
    print(i)

#valuelere ulasmak icin ise indexleme kullanilir
for i in dic1:
    val = dic1[i]
    print(i , "'n notu : " ,val) # ogrnin ismi yanindada notu yazan for dongusu

#valuelere ulasmak icin diger bir yontem
for i in dic1.values():
    print(i)

#hem key hem valueler ile iterasyon yapmak icin
for k,v in dic1.items():
    print("key degeri : ",k , "--- value degeri : ",v)
