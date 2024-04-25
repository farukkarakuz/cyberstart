#-------- while -----------
x = int(input("Bir sayi giriniz : "))

while (x<0):
    print("Sayiniz negatif lütfen pozitif sayi giriniz!!")
    x = int(input("Pozitif sayi giriniz : "))
print("Sayiniz pozitif ve sayiniz :",x)

toplam = 0
x =0

while x<=100:
    toplam += x
    x +=1

print("Toplam : ",toplam)

