#girilen sayıya kadar olan sayıların ortalaması
i=0#sayma işlemi için değişken
toplam=0#toplamı bulmak için kullanılacak değişken
sayi=int(input("ortalaması hesaplanacak sayıyı giriniz"))
#kullanıcıdan sayı aldık
while i<=sayi:#döngüyü istenilen sayıya kadar kurduk
    toplam=toplam+i#Sayıları 0 dan başlayarak topladık
    i=i+1#sayac değişkenini artırdık
ort=toplam/sayi#ortalama bulmak için toplamı girilen sayıya böldük
print("sonuç=",ort)
