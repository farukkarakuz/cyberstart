# ----- split func ------
# split belirli bir bolme kriterine göre stringin alt parçalarını liste elemanlarina donusturebilir
s1 = "merhaba nasilsin?"
s1splitspace = s1.split(" ") # hic bir sey yazmassak default olarak space karakterine gore boler
print(s1splitspace)

print("---------------")
s2 = "elma,muz,portakal,kayisi"
s2splitcomma = s2.split(",")
print(s2splitcomma)

# join func
# listenin elemanlarini arasina belirtilen yapıyı koyup stringe donusturur
l1 = ["elma","muz",'kayisi']

l1joincomma = ",".join(l1)
print(l1joincomma)

l1joinspace = " ".join(l1)
print(l1joinspace)