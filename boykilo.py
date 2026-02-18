yas=int(input("Yaşınızı giriniz"))
kilo=int(input("Kilonuz giriniz"))
boy=int(input("boyunuzu giriniz"))
ayak=int(input("Ayak numaranızı giriniz"))
if yas>18 and kilo<100 and boy>160 and (ayak==37 or ayak==38 or
                                        ayak==39 or ayak==40 or
                                        ayak==41 or ayak==42):
    print("UYGUN")
else:
    print("UYGUN DEĞİL")
