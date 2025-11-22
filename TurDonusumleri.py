"""
Tür dönüşümleri, türlerin birbirleri arasında değişim yapmasına olanak sağlar,
tabii ki de belirli kısıtlamalar çerçevesinde.
Örneğin input() fonksiyonundan almış olduğunuz string türde bir veriyi,
integer türüne dönüştürerek matematiksel işlemlerde kullanabilirisiniz.
"""

# STR -> INT (Metinden, Tam Sayıya)

"""
Eğer kullanıcıdan alınan sayı ile matematiksel işlem yapılacaksa,
o metni tam sayıya (INTEGER) çevirmemiz gerekir. Bunun için int() fonksiyonu kullanılır.
"""

dogum_yili = int(input("Lütfen Doğum Yılınızı Giriniz: "))

"""
dogum_yili = int(dogum_yili)
veya
dogum_yili_int = int(dogum_yili)
da kullanılabilir.
"""

yas = 2025 - dogum_yili

print("Yaşınız = ", yas)

# STR -> FLOAT (Metinden, Ondalıklı Sayıya)

"""
Eğer kullanıcıdan alınan sayı ile ondalıklı matematiksel işlem yapılacaksa,
o metni ondalıklı sayıya (FLOAT) çevirmemiz gerekir. Bunun için float() fonksiyonu kullanılır.
"""

boy_cm = float(input("Lütfen Boyunuzu Giriniz: "))

boy_metre = boy_cm / 100

print("Boyunuz Metre Cinsinden ", boy_metre, " m'dir")

print("Lütfen İsteyeceğimiz Verileri cm Cinsinden Giriniz.")
silindirin_yaricapi = float(input("Lütfen Elinizdeki Silindirin Yarıçapını Giriniz: "))
silindirin_yuksekligi = float(input("Lütfen Elinizdeki Silindirin Yüksekliğini Giriniz:"))

silindirin_hacmi = 3.141592 * (silindirin_yaricapi ** 2) * silindirin_yuksekligi

print("Silindirin Hacmi ", silindirin_hacmi, " cm3'dir")

# INT or FLOAT -> STR (Tam Sayıdan veya Ondalıklı Sayıdan, Metne)

"""
Örneğin print() fonksiyonunda print("String Veri" + int_veri) yaptığımız zaman,
Python bize hata çıkaracaktır (TypeError). Bu hatayı alamamak için str() fonksiyonu ile,
tür dönüşümü gerçekleştirmemiz gerekir.
"""

maas = 375562 # int
prim = 56132.93 # float

# İkisi de matematiksel değişkenler

toplam_maas = maas + prim # toplam_maas = float

"""
Python iki farklı değişkene, yani int ve float türüne sahip iki farklı değişkene,
matematiksel işlemler sırasında type Error vermemek için arka planda
otomatik olarak int olan değişkeni float yapar. Çünkü iki değişkende matematiksel
değişkenlerdir. Bu sebepten sadece bu duruma özel olarak bu işlem gerçekleşir.
"""

print("Toplam Maaşınız = " + str(toplam_maas) + "$'dır")
print("1 Yıldaki Toplam Maaşınız = " + str(toplam_maas * 12) + "$'dır. TL Cinsinden = " + str((toplam_maas * 12) * 42.33) + "TL'dir")

# Özet

"""
Özet:
1. input() = Hep string Veri Verir.
2. int() = Metni, Tam Sayıya Çevirir.
3. float() = Metni, Ondalık Sayıya Çevirir.
4. str() = Sayıyı (int or float) metne çevirir.

Uyarı:
Eğer ki int() veya float() içerisine matematiksel olmayan bir değer girilirse (ÖRN: "beş"),
Python "ValueError" hatası verir ve program çöker. 
(Bu hatayı yönetmeyi ileride "Hata Ayıklama" dersinde göreceğiz.)
"""