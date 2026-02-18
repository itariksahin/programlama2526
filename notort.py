#iki yazılı 2 performans notuna göre dersten geçti veya
#kaldı yazan program geçme notu 50
yazi1=int(input("Birinci yazılı notunu girniz"))
yazi2=int(input("İkinci yazılı notunu girniz"))
per1=int(input("Birinci performans notunu girniz"))
per2=int(input("İkinci performans notunu girniz"))
ort=(yazi1+yazi2+per1+per2)/4
if ort>=50:
    print("Dersten başarılı")
else:
    print("Dersten başarısız")
