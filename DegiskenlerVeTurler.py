degisken_adi = "Deger"

# Python'da değişken tanımlamaları yukarıda gördüğünüz şekilde yapılır.

"""
Değişken adları sayi ile başlamaz.
Boşluk içeremez, genellikle alt çizgi kullanılır. (deneme_Deneme)
Türkçe karakter kullanmak tamamen yasaktır. (Benim tarafımca)
Python büyük küçük harf farkına duyarlı bir dildir. Bu sebepten Isim ve isim değişkenleri aslında iki farklı değişkeni temsil eder.
"""

# string

isim = "Dilara"
Mesaj = 'Ben bir Python öğrencisiyim.'

print(isim)
print(Mesaj)
print("Benim adım: " + isim + ". Ve benim size bir mesajım var o da, " + Mesaj)

# int (integer)

yas = 23
ogrenci_sayisi = 478

print(yas)
print(ogrenci_sayisi)
print("Benim adım: ", isim, ". Ve ben ", yas, " yaşımdayım. Aynı zamanda ", ogrenci_sayisi, " adet öğrencim var.")

# float

boy = 1.68
ortalama_not = 85.3

print(boy)
print(ortalama_not)
print("Benim adım: ", isim, ". Ve ben ", boy, " boyundayım. Aynı zamanda benim ortalamam", ortalama_not)

# bool (boolean)

giris_yapildi_mi = True
ders_bitti_mi = False

print("Giriş yapıldı mı? ", giris_yapildi_mi)
print("Ders bitti mi? ", ders_bitti_mi)

"""
Pythonda temel olarak 4 adet değişken türü vardır.
Bunlar yukarıdada görmüş olduğunuz gibi,
Metinsel ifadeler için = string
Matematiksel ifadeler için = int
Ondalık sayılı matematiksel ifadeler için = float
Tek bir veriyi bit olarak 0 veya 1 yani False veya True olarak tutmak için ise = bool
Vardır.
Bu değişken türleri siz değişken adını verip değişkenin içerisini doldurduğunuzda, Python tarafından değişkene otomatik olarak atanır.
Siz değişken türlerini eliniz ile girmezsiniz.
"""

# type()

kullanici_adi = "nur_sa"
kullanici_yasi = 23
kullanici_maasi = 25750.65
kullanici_evli_mi = True

print(type(kullanici_adi))
print(type(kullanici_yasi))
print(type(kullanici_maasi))
print(type(kullanici_evli_mi))

# type() size içerisine girmiş olduğunuz değişkenin türünü verir.