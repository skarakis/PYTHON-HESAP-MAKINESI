sayi1=int(input("1.sayiyi giriniz:"))
sayi2=int(input("2.sayiyi giriniz:"))
print("islemler:toplama/cikarma/carpma/bölme")
print("toplama icin 1'e basiniz/cikarma için 2'e basiniz/carpma icin 3'e basiniz/bölme icin 4'e basiniz")
islem=int(input("islem seciniz:"))

if islem==1:
    toplam= sayi1+sayi2
    print("toplama",toplam)
elif islem==2:
    cikarma=sayi1-sayi2
    print("cikarma",cikarma)
elif islem==3:
    carpma=sayi1*sayi2
    print("carpma",carpma)
elif islem ==4:
    bolme = sayi1 / sayi2
    print("bolme", bolme)
else:
    print("BİR İSLEM GİRİNİZ!")