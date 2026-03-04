#girilen bir metinde "t" harfine kadar olan kısmını ekrana yazdıran program
metin=input("Bir metin giriniz")
for i in metin:
    if i=='t':
        break
    print(i)
print("------------------------")
