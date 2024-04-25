#list start
notlar = [92,35,23,79,56,84]

# #listler tek bir veri tipi bulundurmayabilir.Farklı veri tiplerini içerebilir
list =[12,"Faruk",[1,23,4]]
print(notlar[:200])

# #listler mutable özelliklidir. İndexleri değiştirebilir
notlar[2]= 10
notlar[1:3] = 20,56,78

print(len(notlar))
print("--------------------")
#bazı fonksiyonlar --> append(),extend(),insert(),remove(),pop(),count(),copy(),+(concat islemi),index(),reverse(),sorted().sort()

"""
remove fonksiyonunu listin içinde olmayan değeri silmek icin kullanirsak hata verir,o degerden 2 tane varsa dusuk indekliyi siler
insert fonksiyonu verilen parametre yerine yeni değer atar eski değeri +1 indekse atar yani list in boyutunu artar
pop fonksiyonu belirtilen indexteki değeri siler ve o değeri döndürür
sorted fonk intleri değerlerini,charlari alfabetik siralamaya göre en küçüktene göre siralar
reverse  ve sort fonksiyonlari inplacedir. listeyi günceller.
siralama islemlerinde farkli int ve str verileri siralarken hata verir. ama "a","c","2","3" de hata vermez ilk intleri sonra strleri siralar

"""
l1 =[1,2,3,4,5]
print(len(l1)) # yazilan 5

l1.insert(1,200)
print(len(l1)) # yazilan 6
print("--------------------")
#------- list aliasing ------
a=2
b = a 
a += 2   #a nın değeri değiştiginde b nin değeri güncellenmez lakin bu durum listlerde farklı

l2= [24,56,78,81,42]
l3 = l2
l2.append(97)
print(l3) # l3 ün değeri güncellendi burdaki eşitleme bir nevi pointer görevi görüyor bu engellenmek isteniyorsa copy fonksiyonu kullanılabilir

l3 = l2.copy()



