#faktöriyel hesaplayan program
i=1
faktor=1
sayi=int(input("Faktöriyeli hesaplacak sayıyı giriniz"))
while i<=sayi:
    faktor=faktor*i
    i=i+1
print("sonuç=",faktor)
