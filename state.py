"""
eşitlik --> i==j
eşitsizlik --> i!=j
büyüktür -->  i>j
küçüktür --> i<j
büyük eşittir --> i>=j
küçük eşittir --> i<=j

"""

x = int(input("Bir sayi giriniz : "))
if (x==5):
    print("x 5'e eşit")
elif(x<5):
    print("x 5ten küçük")
else:
    print("x ten büyük")
print("Program bitti ....")

#ternany conditionals
cevap ="n"
x = 5 if cevap=="y" else 0 # cevap y ye eşit ise 5 yap değil ise 0 yap
