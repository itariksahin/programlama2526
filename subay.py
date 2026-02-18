cinsiyet=input("bayan için : b erkek için e yazınız")
dil=input("bilgiginiz yabancı dili küçük harfle yazınız")
boy=int(input("boyunuzu giriniz"))
if cinsiyet=="b":
    if cinsiyet=="b" and boy>160 and (dil=="almanca" or dil=="ingilizce"or
                                  dil=="fransızca" or dil=="japonca"):
        print(" bayan aday için Subaylığa uygun")
    else:
        print(" bayan aday için Subaylığa uygun değil")
else:
    if cinsiyet=="e" and boy>170 and (dil=="almanca" or dil=="ingilizce"or
                                  dil=="fransızca" or dil=="japonca"):
        print(" erkek aday için Subaylığa uygun")
    else:
        print(" erkek aday için Subaylığa uygun değil")

