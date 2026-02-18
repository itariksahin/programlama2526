ad=["Ali","Ayşe","Zeki","Zeki","Zeki","Sibel","Merve","Yalçın","Zümra"]
il=["Van","Muş","Samsun","Adana"]
#Append listenin sonuna eleman ekleme
print("**************************************")
ad.append("Hayri")
il.append("İstanbul")
print(ad)
print(il)
#extend listre birleştirici
print("**************************************")
ad.extend(il)
print(ad)
print(il)
#İnsert istenilen indis noktasına deger ekleme
print("**************************************")
ad.insert(3,"Tamer")
print(ad)
ad.insert(3,"Mert")
print(ad)
#remove ilgili degeri listeden siler
print("**************************************")
ad.remove("Tamer")
ad.remove("Mert")
print(ad)
#pop listeden indis degerine göre veri siler
print("**************************************")
ad.pop(3)
print(ad)
ad.pop(5)
print(ad)
#index bir degerin indis degerini bulur
print("**************************************")
print(ad.index("Yalçın"))
#count elaman sayar kaç tane varsa verir
print("**************************************")
print(ad.count("Zeki"))
#listeyi ters yazdırma Reverse
print("**************************************")
ad.reverse()
print(ad)
# sort listeyi belirli bir kritere göre sıralar
print("**************************************")
ad.sort()
print(ad)
ad.sort(reverse=True)
print(ad)
#listeyi kopyalama
print("**************************************")
yeni_ad=ad.copy();
print(yeni_ad)
#indisi verilen degeri siler
del ad[7]
print(ad)
#listeyi temizleme clear
print("**************************************")
ad.clear()
print(ad)
