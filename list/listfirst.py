#list start
# notlar = [92,35,23,79,56,84]

# #listler tek bir veri tipi bulundurmayabilir.Farklı veri tiplerini içerebilir
# list =[12,"Faruk",[1,23,4]]
# print(notlar[:200])

# #listler mutable özelliklidir. İndexleri değiştirebilir
# notlar[2]= 10
# notlar[1:3] = 20,56,78

# print(len(notlar))

#bazı fonksiyonlar --> append,extend,insert,remove,pop,count

"""
remove fonksiyonunu listin içinde olmayan değeri silmek icin kullanirsak hata verir,o degerden 2 tane varsa dusuk indekliyi siler
insert fonksiyonu verilen parametre yerine yeni değer atar eski değeri +1 indekse atar yani list in boyutunu artar
pop fonksiyonu belirtilen indexteki değeri siler ve o değeri döndürür
"""
l1 =[1,2,3,4,5]
print(len(l1)) # yazilan 5

l1.insert(1,200)
print(len(l1)) # yazilan 6
