#programda saklı sayıyı bulma oyunu
import random
bulundu=0
sakli_sayi=random.randint(0,1000)
while bulundu==0:
    tahmin=int(input("Tahmininiz"))
    if tahmin<sakli_sayi:
        print("Küçük sayı girdiniz")
    elif tahmin>sakli_sayi:
        print("Büyük sayı girdiniz")
    else:
        print("TEBRİKLER BULDUNUZ")
        bulundu=1
print("Program bitti")
