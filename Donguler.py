# DÖNGÜLER (LOOPS)

"""
Programlamada bir işi tekrar tekrar yapmamız gerekiyorsa döngüleri kullanırız.
Python'da iki temel döngü çeşidi vardır:
1. for döngüsü: Belirli bir sayıda (veya bir listenin üzerinde) işlem yapmak için.
2. while döngüsü: Belirli bir koşul sağlandığı sürece işlem yapmak için.
"""

# ================================================================
# 1. FOR DÖNGÜSÜ ve range() FONKSİYONU
# ================================================================

"""
'for' döngüsü genellikle "kaç kere döneceği belli olan" durumlarda kullanılır.
En sık range() fonksiyonu ile birlikte görürüz.
"""

print("--- 1. Basit for Döngüsü ---")

# range(5) -> 0'dan başlar, 5'e kadar (5 dahil değil) gider. (0, 1, 2, 3, 4)
for sayi in range(5):
    print("Döngü çalışıyor, sayı:", sayi)

print("\n--- 2. range() Kullanım Çeşitleri ---")

# range(başlangıç, bitiş, artış_miktarı)
# 1'den başla, 10'a kadar git, 2'şer 2'şer art.
for i in range(1, 10, 2):
    print("Tek sayılar:", i)

print("\n--- 3. Metin Üzerinde Gezinmek ---")

# Stringler de aslında birer harf dizisidir.
isim = "Dilara"

for harf in isim:
    print("Sıradaki harf:", harf)

# ================================================================
# 2. WHILE DÖNGÜSÜ ( -dığı sürece )
# ================================================================

"""
'while' döngüsü, yanındaki koşul 'True' (Doğru) olduğu sürece dönmeye devam eder.
Mantığı 'if' yapısına benzer ama tek farkı, koşul bozulana kadar tekrar etmesidir.

ÇOK ÖNEMLİ: while döngüsü içinde koşulu değiştirecek bir işlem yapmazsanız,
döngü sonsuza kadar sürer (Sonsuz Döngü / Infinite Loop).
"""

print("\n--- 4. Basit while Döngüsü ---")

sayac = 1

while sayac <= 5:
    print("Sayaç değeri:", sayac)
    sayac = sayac + 1  # (veya sayac += 1) Bunu yazmazsak döngü asla bitmez!

print("Döngü bitti.")

# ================================================================
# 3. DÖNGÜ KONTROL İFADELERİ: break ve continue
# ================================================================

"""
Döngü normal seyrinde devam ederken bazen müdahale etmemiz gerekir.
break    -> Döngüyü anında KIRAR ve bitirir.
continue -> Döngünün sadece o turunu ATLAR ve başa döner.
"""

print("\n--- 5. break (Döngüyü Kırma) ---")

for i in range(1, 10):
    if i == 5:
        print("Sayı 5 oldu, döngü kırılıyor!")
        break  # Döngü burada biter, 6, 7, 8... yazılmaz.
    print("Sayı:", i)

print("\n--- 6. continue (Turu Atlama) ---")

for i in range(1, 6):
    if i == 3:
        print("Sayı 3 atlanıyor...")
        continue  # Aşağıdaki print çalışmaz, döngü direkt 4'e geçer.
    print("İşlenen Sayı:", i)

# ================================================================
# 4. PRATİK ÖRNEK: Şifre Deneme Simülasyonu
# ================================================================

"""
while döngüsünün en yaygın kullanımı, kullanıcı doğru veriyi girene kadar
tekrar tekrar sormaktır.
"""

print("\n--- 7. İnteraktif Örnek: Şifre Sorma ---")

gizli_sifre = "1234"
girilen_sifre = ""  # Başlangıçta boş

# Şifre yanlış olduğu sürece dönmeye devam et
while girilen_sifre != gizli_sifre:
    girilen_sifre = input("Lütfen şifreyi giriniz (Çıkış için 'q'): ")

    if girilen_sifre == "q":
        print("Programdan çıkılıyor...")
        break  # Döngüyü manuel olarak kırdık

    if girilen_sifre == gizli_sifre:
        print("Tebrikler, giriş başarılı!")
    else:
        print("Yanlış şifre, tekrar deneyin.")