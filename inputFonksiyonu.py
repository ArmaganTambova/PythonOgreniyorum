input("Deneme Amaçlı Input")

"""
input() sistemi durdurarak kullanıcıdan veri almayı bekler.
input() iki farklı şekilde kullanılabilir.
input() = Direkt kullanıp veri alabilirsiniz.
input("Herhangi Bişi") = Veri almadan önce herhangi bir şey yazdırarak da kullanabilirsiniz.
input() aldığı her veriyi string (str) türünde alır.,
yani siz 5 yazarsanız o Python için aslında "5" dir.
"""

isim = input("Lütfen Adınızı Giriniz: ")

print("Kullanıcının İsmi = " + isim)

print(type(isim))

# type() içerisine girmiş olduğunuz değişkenin türünü verir.