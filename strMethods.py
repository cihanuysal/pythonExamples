website="http://www.teknoparkistanbulmtal.com"
course="Python Kursu: Burda python ile temel programlama derslerini tamalayacağız."

# 1- ' Hello World ' karakter dizisinde baş ve sondaki boşluk karakterlerini silin
# 2- 'www.teknoparkistanbulmtal.com' içindeki teknoparkistanbulmtal haricindeki her karakteri silin ve sonucu ekrana yazınız.
# 3- 'course' karakter dizisindeki tüm karakterleri küçük harf yapın
# 4- 'website' içinde kaç tane a karakteri vardır?
# 5- 'website' www ile başlayıp com ile bitiyor mu?
# 6- 'website' içinde .com ifadesi var mı?
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
# 8- 'İçerik' ifadesini satırda 20 karakter içine yarleştirip sağ ve soluna  ekleyiniz
# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın
# CEVAPLAR
#cevap 1 :
c1=' Hello World '.strip()

#cevap 2 :  
c2="www.teknoparkistanbulmtal.com".lstrip("w.").rstrip(".com")
print(c2)

#cevap 3 :
c3=course.lower()
print(c3)

#cevap 4:
c4=website.count("a")
print(c4," tane a karakteri var")

#cevap 5:
if(website.startswith("wwww")):
    print("ifade www başlıyor")
else :
    print("ifade www ile BAŞLAMIYOR.")
if(website.endswith("com")):
    print("ifade com ile bitiyor.")
else:
    print("ifade com ile BİTMİYOR.")

#cevap 6:
if (website.find(".com")>-1) :
    print("com ifadesi var")
else :
    print("com ifadesi yok")

#cevap 7:
if (course.isalpha()==True) :
    print("ifade ALFABETİK")
else:
    print("ifade ALFABETİK DEĞİL")

#-- EK ÖRNEK 
test=["1234","12Abc","Aabc::**!","Abc","İĞÇÖÜİ"]
for t in test :
    if (t.isdigit()==True):
        print(t," Rakamlardan oluşur")
    else:
        print(t, " Rakamlardan oluşmaz.")

    if (t.isalpha()==True) :
        print(t," Alfabetik karakterlerden oluşur.")
    else :
        print(t," Alfabetik karakterlerden oluşmaz.")
# cevap 8:
c8="İÇERİK".center(20,"*")
print (c8)

# cevap 9:
c9=course.replace(" ","_")
print(c9)

#cevap 10:
c10="Hello World".replace("World", "There")
print(c10)

#cevap 11:
c11=course.split();
print ("liste elde edilir.")
print(c11)





    
   




