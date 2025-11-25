"""
if - elif - else

Şu ana kadar yazdığımız tüm kodlar yukarıdan aşağıya sırayla çalışıyordu.
Ancak gerçek hayatta hep düz gitmeyiz, duruma göre karar veririz.

Örneğin: Hava yağmurluysa şemsiye al, değilse alma.

Python'da bu kurar mekanizmasını if, elif ve else ile kurarız.
"""
from DegiskenlerVeTurler import kullanici_adi

# if BLOĞU (EĞER)

"""
if kelimesi İngilizcede "eğer" anlamına gelir.
Yanına yazılan koşul true ise, altındaki kodlar çalışır.
Koşul False (Yanlış) ise, Python o satırları görmezden gelir ve atlar.

ÇOK ÖNEMLİ KURAL: GİRİNTİ (INDENTATION)
Python'da bir koda "Bu kod if'e aittir" demek için baş taraftan boşluk bırakılır (Tab tuşu).
Buna 'Girinti' denir. Girinti olmazsa Python hata verir (IndentationError).
"""

print("-- 1. if Örneği --")

yas = int(input("Lütfen Yaşınızı Giriniz: "))

if yas >= 18:
    print("Reşitsiniz")
    print("Ehliyet Alabilirsiniz")

print("Bu mesaj her zaman çalışır. (Çünkü girinti yok, if'e bağlı değil)")

# if-else BLOĞU (EĞER - DEĞİLSE)

"""
Sadece koşulun tuttuğu durumu değil, tutmadığı durumu da yönetmek istersek 'else' kullanırız.
else: "Yukarıdaki koşul sağlanmadıysa, o zaman bunu yap" demektir.
else bloğu ASLA koşul almaz.
"""

print("-- 2. if-else Örneği --")

sifre = input("Sisteme Girmek İçin Lütfen Şifrenizi Yazınız: ")
dogru_parola = "python123456"

if sifre == dogru_parola:
    print("Giriş İşlemi Başarılı")
else:
    print("Şifre Yanlış")

# if-elif-else (ÇOKLU KOŞULLAR)

"""
Hayat her zaman 'Siyah' veya 'Beyaz' değildir. Bazen 3. veya 4. ihtimaller vardır.
Birden fazla koşulu sırayla kontrol etmek için 'elif' (else if'in kısaltması) kullanılır.

Sıralama Mantığı:
1. Python if'e bakar. Tutarsa yapar ve çıkar.
2. Tutmazsa elif'e bakar. Tutarsa yapar ve çıkar.
3. Hiçbiri tutmazsa en son else çalışır.
"""

print("-- 3. if-elif-else Örneği --")

sayi = int(input("Lütfen Bir Tam Sayı Giriniz: "))

if sayi > 0:
    print("Sayı Pozitiftir")
elif sayi < 0:
    print("Sayı Negatiftir")
else:
    print("Sayı Nötrdür")

# Mantıksal Operatörlerle Kullanımı (and - or)

"""
Daha önce öğrendiğimiz 'and' ve 'or' operatörlerini if içinde kullanarak
daha güçlü sorgular yapabiliriz.
"""

print("-- 4. Mantıksal Operatörler Örneği")

kullanici_adi = input("Lütfen Kullanıcı Adınızı Giriniz: ")
kullanici_sifresi = input("Lütfen Şifrenizi Giriniz: ")

if kullanici_adi == "admin" and kullanici_sifresi == "123456":
    print("Yönetici Girişi Yapıldı")
else:
    print("Giriş İşlemi Başarısız")

# ÖZET

"""
1. if   -> Koşul doğruysa çalışır.
2. elif -> if çalışmazsa alternatif koşulları dener. (İstediğiniz kadar kullanabilirsiniz)
3. else -> Yukarıdaki hiçbir koşul tutmazsa çalışan 'son çare' bloğudur.
4. Girinti -> if, elif ve else'in içindeki kodlar mutlaka içeriden (Tab) başlamalıdır.
"""