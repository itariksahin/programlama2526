#kullanıcı 0 yazana kadar girdiği sayıları toplayap program
toplam=1
while True:
    sayi=int(input("Bir sayı giriniz bitirmek için 0 giriniz"))
    if sayi==0:
        break
    toplam=toplam+sayi
print("toplam=",toplam)
