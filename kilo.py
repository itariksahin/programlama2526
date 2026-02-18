#Kullanıcıdan kilosunu soran ve çıktı veren program
kilo=int(input("KAÇ KİLO GELİRSİNİZ"))
if kilo<30:
    print("Aşırı zayıf")
elif kilo<50:
    print("Zayıf")
elif kilo<75:
    print("Normal")
elif kilo<90:
    print("Kilolu")
elif kilo<110:
    print("Şişman")
elif kilo<135:
    print("Obez")
else:
    print("Yok artık NEJLA OLDUN MAŞALLAH")
print("Program tamamlandı!!!!!!!!")
