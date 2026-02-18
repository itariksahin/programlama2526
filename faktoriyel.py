#Girilen sayının faktoriyelini bulan program
faktoriyel=1
sayi=int(input("HAngi sayının faktöriyeni hesaplayayım"))
for sayac in range(1,sayi+1,1):
    faktoriyel=faktoriyel*sayac
print("Sonuc=",faktoriyel)
