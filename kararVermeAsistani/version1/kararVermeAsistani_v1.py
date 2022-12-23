import random

print("Nasılsınız? ")
print("Umarım iyisinizdir ")
print("Önce hangi derse çalışacağınıza karar veremiyor musunuz, seçmenize yardımcı olabiliriz")
i=int(input("Bu dönem kaç dersiniz var? "))
ders = [0]*i
bunucalisindex=list(range(0,i))
ders=list(range(0,i))
dersisimleri=ders

for derssayisi in ders:
    print(derssayisi)
    dersisimleri[derssayisi]=input("Dersinizin adını giriniz: ")

print("Bunlar arasından",dersisimleri)
    
def fonkiponki(ikna): 
    if ikna == 0:
        bunucalis=random.choice(bunucalisindex)
        if bunucalis==0:
            print("Öncelikle")
            print("şu dersi çalışınız: ",dersisimleri[0])
        elif bunucalis==1:
            print("Öncelikle")
            print("şu dersi çalışınız: ",dersisimleri[1])
        elif bunucalis==2:
            print("Öncelikle")
            print("şu dersi çalışınız: ",dersisimleri[2])
        elif bunucalis==3:
            print("Öncelikle")
            print("şu dersi çalışınız: ",dersisimleri[3])
        elif bunucalis==4:
            print("Öncelikle")
            print("şu dersi çalışınız: ",dersisimleri[4])
        elif bunucalis==5:
            print("Öncelikle")
            print("şu dersi çalışınız: ",dersisimleri[5])
        elif bunucalis==6:
            print("Öncelikle")
            print("şu dersi çalışınız: ",dersisimleri[6])
        elif bunucalis==7:
            print("Öncelikle")
            print("şu dersi çalışınız: ",dersisimleri[7])
        elif bunucalis==8:
            print("Öncelikle")
            print("şu dersi çalışınız: ",dersisimleri[8])
        elif bunucalis==9:
            print("Öncelikle")
            print("bu dersi çalışınız: ",dersisimleri[9])
        elif bunucalis==10:
            print("Öncelikle")
            print("bu dersi çalışınız: ",dersisimleri[10])
x=0
fonkiponki(x)


iknaoldunmu=int(input("İkna olduysanız 1'i olmadyısanız 0'ı tuşlayınız: "))
if iknaoldunmu == 1:
    print("İyi çalışmalar")

while iknaoldunmu == 0:
    if iknaoldunmu == 0:
        x=iknaoldunmu 
        fonkiponki(iknaoldunmu)
        iknaoldunmu=int(input("İkna olduysanız 1'i olmadıysanız 0'ı tuşlayınız: "))
        if iknaoldunmu == 1:
            print("İkna olduğunuza göre iyi çalışmalar")
            break
    else:
        print("Geçersiz değer girdiniz, Tekrar deneyiniz: ")
        iknaoldunmu=int(input("Tekrar değer giriniz: "))
        