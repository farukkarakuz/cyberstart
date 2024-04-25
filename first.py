#değişken atama
a = 2

b= a+2

#degisken uygulama
limon_fiyati = 10
s1 = limon_fiyati *10
s2 = limon_fiyati *20
s3 = limon_fiyati*30

print(s1)
print(s2)
print(s3)

#type fonksiyonu
#değişkenin hangi tip veri olduğunu gösterir.
type(s3)

# int-division --> //
# division --> /
# power --> **
# mod --> %

#string veri
#escape sequences \",\',\n
print("Merhaba"+"Dünya")
#string functions --> concat,len,
print("hey"*4) #-->succssive concat
isim= "Faruk"
print(isim[-1]) #indexleme
#slicing
print(isim[0:3]) # [baslangic:bitis] bitis degeri alınmaz
print(isim[2:]) # sonuna kadar alır
print(isim[:10:2]) # 3 tane girersek son parametre adım sayısını belirtir. bitisi string len inden fazla girsekte son değere kadar alır
print(isim[10:0:-1]) #geri geri yazar. Son değeri almaz dikkat!!


x = input("Bir sayı giriniz : ") #inputtan alınan değer string değer olur !!!
# x ile sayılar ile işlem yapmak için casting işlemleri uygula


