# Dört işlem yapan program elif ile.
sonuc=0
sayi1=int(input("Birinci sayıyı giriniz"))
sayi2=int(input("İkinci sayıyı giriniz"))
islem=input("Yapmak istediğiniz işlemi seciniz(+,-,*,/)")
if islem=="+":
    sonuc=sayi1+sayi2
elif islem=="-":
    sonuc=sayi1-sayi2
elif islem=="*":
    sonuc=sayi1*Sayi2
elif islem=="/":
    sonuc=sayi1/sayi2
else:
    print("YANLIŞ İŞLEM SEÇTİNiZ")
if sonuc!=0:
    print("Seçtiğiniz işlemin sonucu=",sonuc)

