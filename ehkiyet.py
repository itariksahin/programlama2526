#Kullanıcıya yaşını soran ve ehliyet alır almaz belirten program
yas=int(input("Yaşınızı giriniz"))
if yas>=18:
    print("Ehliyet ala bilir")
    print("****************")
else:
    print("Ehliyet Alamaz")
    print("!!!!!!!!!!!!!!!!")
# aynı kodu yaş küçük olarak kontrol edelim
if yas<18:
    print("Ehliyet Alamaz")
    print("!!!!!!!!!!!!!!!!")
else:
    print("Ehliyet ala bilir")
    print("****************")
