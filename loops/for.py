# --------- for --------- 

for x in "hey":
    print(x)

toplam=0
for x in range(101):   # range metodu içine aldığı parametre ile 0 dan başlayıp parametrenin 1 eksiği kadar iterasyon oluşturur
    toplam +=x
print(toplam)

usalma =1
for _ in range(5):   # for daki degiskeni kullanmaya gerek yoksa underscore (_) ile degisken ismi girebiliriz
    usalma *=5
print(usalma)

#break ve continue mantığı

for i in range(10):
    if i ==3:
        break    #break komutu eğer şart sağlanırsa if bloğundan çıkar
    print(i)


for i in range(6):
    if i ==3:
        continue    #continue komutu eğer şart sağlanırsa diğer iterasyona geçer
    print(i)
