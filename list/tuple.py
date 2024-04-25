# ------- tuple ------
#tuple list gibidir farkı tuple'lar immutable dır. degiskenleri degistirilemez
# tuple tanımlanırken (veri1,veri2,....) seklinde tanimlanir
x=145
y=42
konum=(x,y)
# indeksleme yapabiliriz
print(konum[0])
print(konum[:])

# farkli veri tipleri barindirabilir

tuple1=("a","b",12,45)

# parantezsiz de kullanılabilr

tuple1 = 1,2,3,4


#tuple ve listlerde içinde eleman var mı kontrolü in keywordü kullanilabilir. iflerde kullanilir
if (2 in tuple1):
    print("tuple1 de 2 var")