# mantık oparatörü or veya demek
# mantık oparatörü and ve demek
# or ile sorguda 1 tanesi doğru olsa sonuç doğrudur
# and ile sorguda 1 tanesi doğru olsa sonuç yanlıştır.
# subay secimi için kriterler
# almanca,ingilizce,fransızca veya japonca bilmek
# bayanlar için 160 erkekler için 170 boy olması
cinsiyet=input("bayan için : b erkek için e yazınız")
dil=input("bilgiginiz yabancı dili küçük harfle yazınız")
boy=int(input("boyunuzu giriniz"))

if cinsiyet=="b" and boy>160 and (dil=="almanca" or dil=="ingilizce"or
                                  dil=="fransızca" or dil=="japonca"):
    print(" bayan aday için Subaylığa uygun")
else:
    print(" bayan aday için Subaylığa uygun değil")
if cinsiyet=="e" and boy>170 and (dil=="almanca" or dil=="ingilizce"or
                                  dil=="fransızca" or dil=="japonca"):
    print(" erkek aday için Subaylığa uygun")
else:
    print(" erkek aday için Subaylığa uygun değil")

