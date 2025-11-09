"""
Aritmatik Operatörler;
Toplama, Çıkartma, Çarpma, Bölme, Tam bölme, Mod Alma ve Üs Alma
Şeklinde ayrılır ve matematiksel olarak bize sonuç verir.
Genellikle int ve float türündeli değişkenlerdeki veriyi işlemek için kullanılır lakin daha önce de görmüş olduğumuz gibi,
print() fonksiyonunda string bir ifadeye string bir ifade eklemek için de kullanılabilir. Tek kısıtlama string ifadeye string ifade eklemek değildir.

--

Toplama = +
Çıkartma = -
Çarpma = *
Bölme = /
Tam Bölme = //
Mod Alma = %
Üs Alma = **

--

Toplama = İki değişkeni toplamaya yarar.
Çıkartma = İki değişkeni çıkartmaya yarar.
Çarpma = İki değişkeni çarpmaya yarar.
Bölme = İki değişkeni bölmeye yarar.
Tam Bölme = İki değişkenin bölmede çıkan sonucunun ondalık kısmını dahil etmez.
Mod Alma = İki değişkenin bölümünden kalan değeri verir.
Üs Alma = Bir değişkenin ... üssünü almaya yarar.
"""

print("Lütfen Projenin Daha Eğitici Olması İçin Bize 2 Adet Sayı Verin.")

sayi1 = int(input())
sayi2 = int(input())

print("Toplam = ", sayi1 + sayi2)
print("Çıkartma = ", sayi1 - sayi2)
print("Çarpma = ", sayi1 * sayi2)
print("Bölme = ", sayi1 / sayi2)
print("Tam Bölme = ", sayi1 // sayi2)
print("Mod Alma = ", sayi1 % sayi2)
print("Üs Alma = ", sayi1 ** sayi2)

# input() Kullanıcıdan konsol aracılığıyla veri almayı sağlar. Veriyi string türünde alır. Matematiksel işlemler için alınan verilerde int(input()) şeklinde,
# veri dönüşümü gerekmektedir.