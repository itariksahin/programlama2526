#Tahmin oyunu
import random
ss=random.randint(-10000,10000)
print("Oyun -10000 ile 10000 arasında rastgele bir sayıyı bulma oyunudur")
while True:
    tahmin=int(input("Bir sayı giriniz"))
    if tahmin>ss:
               print("Büyük sayı girdiniz")
    elif tahmin<ss:
        print("Küçük sayı girdiniz")
    elif tahmin==ss:
        print("Doğru tahmin")
        break
    else:
        print("Yanlış giriş yaptınız")
print("Program bitti")
        
    
