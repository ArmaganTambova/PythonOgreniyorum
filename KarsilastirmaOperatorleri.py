"""
Karşılaştırma Operatörleri;
Eşit Mi, Eşit Değil Mi, Büyüktür, Küçüktür, Büyük Eşittir, Küçük Eşittir
Şeklinde ayrılır ve karşılaştırma yapmak için kullanılır.
Önemli bir nokta olarak True veya False şeklinde yanıt döndürür. Yani sonuç bize her zaman bool türünde gelir.

--

Eşit Mi = ==
Eşit Değil Mi = !=
Büyüktür = >
Küçüktür = <
Büyük Eşittir = >=
Küçük Eşittir = <=

--

Eşit Mi = İki farklı değişkenin birbirlerine eşit olup olmadığını kontrol eder.
Eşit Değil Mi = Eşit Mi ile aynı şekilde çalışır ama eşit olmama durumunu kontrol eder.
Büyüktür = Bir değişkenin diğer değişkenden büyük olup olmadığını kontrol eder.
Küçüktür = Bir değişkenin diğer değişkenden küçük olup olmadığını kontrol eder.
Büyük Eşittir = Bir değişkenin diğer değişkenden büyük olup olmadğını aynı zamanda eşit olup olmadıklarını aynı anda sorgular.
Küçük Eşittir = Bir değişkenin diğer değişkenden küçük olup olmadğını aynı zamanda eşit olup olmadıklarını aynı anda sorgular.

--

Önemli Not: Genellikle karşılaştırma operatörleri, int veya float türündeki değişkenlerde kullanılır. int ile int, float ile float karşılaştırması yapar.
Kesinlikle int ile float arasında bir karşılaştırma sağlıklı değildir ama yapılabilir. Aynı zamanda string ile string'i de karılaştırabilirsiniz ama bu daha kısıtlıdır.
Örneğin;

mesaj1 = "Dilara"
mesaj2 = "Armağan"

Bu iki değişkenin birbilerine Eşit Mi yoksa Eşit Değil Mi sorgulaması yapılailir ama eğer ki Büyüktür, Küçüktür, Büyük Eşittir veya Küçük Eşittir kullanırsanız, siste buna izin vermez.

Önemli Not: Aynı zamanda iki farklı bool türündeki değişken arasında da Eşit Mi veya Eşit Değil Mi karşılaştırması yapabilirsiniz, lakin diğer karşılaştırma operatörlerini kullanamazsınız.
"""

sifre_giris = input("Lütfen Şifrenizi Giriniz = ")
gercek_sifre = "5633"

print("Şifreler Eşleşiyor Mu? = ", sifre_giris == gercek_sifre)

yas = int(input("Yaşınızı Giriniz = "))
print("Ehliyet Alabilir Mi? = ", yas >= 18)

# input() Fonksiyonu input("Deneme") şeklinde içerisine string olarak veri alabilir. Bunun sonucunda konsola önce bu string veriyi yazıp ardından input işlemi için beklemeye başlar.