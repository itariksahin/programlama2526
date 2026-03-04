#girilen metindeki sessiz harfleri ekrana yazdıran program
metin=input("Bir metin giriniz")
for i in metin:
    if i=='a' or i=='e'or i=='ı'or i=='i'or i=='o'or i=='ö'or i=='u'or i=='ü':
        continue
    print(i)
print("----------------------------------")
