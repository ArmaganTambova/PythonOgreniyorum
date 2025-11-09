"""
Mantıksal Operatörler;
and, or ve not
Şeklinde ayrılır ve birden fazla karşılaştırma (Karşılaştırma Operatörleri) sonucu bir olarak kullanmak için birebirdir.

--

and = "ve" anlamı taşır. Her iki koşulda True ise True döner.
or = "veya" anlamı taşır. Koşullardan en az biri True ise True döner.
not = "değil" anlamı taşır. Koşul sonucunun tersini alır. Yani sonuç True ise False yapar, False ise True yapar.
"""

kullanici_adi = input("Lütfen Kullanıcı Adınızı Giriniz = ")
kullanici_sifresi = input("Lütfen Şifrenizi Giriniz = ")

gercek_kullanici_adi = "Murtaza_Suayipoglu"
gercek_sifre = "458963"

kullanici_adi_uyusuyor_mu = kullanici_adi == gercek_kullanici_adi
kullanici_sifresi_uyusuyor_mu = kullanici_sifresi == gercek_sifre

print("Giriş Başarılı Mı? (and) = ", kullanici_adi == gercek_kullanici_adi and kullanici_sifresi == gercek_sifre)

print("Giriş Başarılı Mı? (or) = ", kullanici_adi_uyusuyor_mu or kullanici_sifresi_uyusuyor_mu)

# not daha ileriki konularda tekrardan pekiştirilecek.