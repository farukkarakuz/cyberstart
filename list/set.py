# ---------- set ---------
"""
kümeler olarak düşünülebilir
setler mutabledir
indexlenemez
dictionarylere göre daha az yer kaplar
"""
# set1 = set() ---> bos set olusturma
set2 = {1,2,3,4,5,1,1,2,3}
print(set2) # set icerisinde her degerden sadece 1 tane bulunur

l1 = [1,2,3,1,1,2,3]
set3 = set(l1) # list elemanlarından set olusturabilir

message = "Merhaba, hosgeldiniz.!"
set4 = set(message)
print(set4)

len(set4) # kac elemani oldugunu yazar
#setler indexlenemez

set4.add(6) # sete eleman ekler
set4.remove(6) # setten eleman siler
# olmayan eleman silinmeye calisilirsa hata verir hata vermemesi icin discard() kullanilabilir

# ---- kume islemleri ------
set5 = {1,2,3,4,5}
set6 = {1,2,4,6,7,8}

difference = set5.difference(set6) #set5 in hangi elemanları set6dan farkli , cevabı set olarak verir , s1 - s2 de kullanilabilir
print(type(difference))
print(difference)

symmetricdif = set5.symmetric_difference(set6) # simetric fark yani (set5 (birlesim) set6) - (set5 (kesisim) set6)
print(type(symmetricdif))
print(symmetricdif)

intersec = set5.intersection(set6) # set5 kesisim set6 verir veya set5&set6 kullanilabilir
print(intersec)

setunion = set5.union(set6) # birlesim
print(setunion)

#disjoint sets --> kesisimi bos kumemi kontrol eder --> isdisjoint()
#subset alt kümemi --> issubset()
#superset --> issuperset( )


