# ---- dictionary -------
# dictionary mutable da olabilir immutable da olabilir
# dic1 ={ key : value } --> dic tanimlamasi bu sekildedir

notlar ={"Deniz":95, "Ege" : 25,"Samet":44}
print(notlar["Ege"])

#dic valueleri listlerden tupledan dictionaryden de olusabilir
dic2 = {"Deniz":{"not":80,"ogrno":12345},"Ege":{"not":25,"ogrno":23456}}
print(dic2["Deniz"]["ogrno"])

#olmayan key sorgulaması yapilirsa hata alinir
print(dic2["Mert"]) # hata verir

#sorgu yaparken key:value degerine gore sorgu yapar, diziler gibi index sorgusu degil

# value degeri degistirebilir
dic2["Deniz"]["not"]=dic2["Deniz"]["not"]+5

len(dic2) #dictionaryde kac tane key oldugunu yazar

del notlar["Samet"] # Mert key ini siler

# sadece immutable tipindeki veriler key olabilir
dic3={} # bos dictionary

# bir deger keyler arasında var mı sorgusu in ile yapilabilir

print("Deniz" in dic2)