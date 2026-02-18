# Girilen sayıya kadar olan sayıları tek mi çift mi
#oldugunu ekrana yazan program
sayi=int(input("Kaça kadar sayayım"))
for sayac in range(sayi+1):
    if sayac%2==0:
        print(sayac,"Sayısı çift sayıdır")
    else:
        print(sayac,"Sayısı tek sayıdır")
print("------ Program Bitti-----")
