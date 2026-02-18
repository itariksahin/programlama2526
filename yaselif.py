#doğum Tarihine göre çıktı veren program
dogum_tarihi=int(input("Doğum yılınızı girin: "))
yas=2026-dogum_tarihi
if yas>=0 and yas<=3:
    print("BEBEK")
elif yas>=3 and yas<=17:
    print("Çocuk")
elif yas>=18 and yas<=50:
    print("Genç")
elif yas>=51 and yas<=65:
    print("ORTA YAŞLI")
elif yas>=66 and yas<=79:
    print("YAŞLI")
elif yas>=80:
    print("ÇOK YAŞLI")
else:
    print("Yanlış değer girdiniz")
