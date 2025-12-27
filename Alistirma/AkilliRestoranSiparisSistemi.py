"""
Bir restoran için dijital adisyon sistemi yazılacak.

1- Menüyü Göster
2- Sipariş Ekle
3- Son Siparişi İptal Et
4- Hesabı Kes ve Çık

Sistem hesap kesilene kadar sonsuz döngü içerisinde çalışacak.
Menüde; (Index + 1) - Yemek Adı - Tutar TL
Sipariş eklerken, yemeğin indexini alacaksın.
En son hesabı kes dediğinde toplam tutar ve tüm siparişlerin listesini menüdeki gibi ver.
"""

MenuYemekler = ["Lahmacun", "Tavuk Şiş", "Ciğer", "Adana", "Kola", "Ayran"]
MenuFiyatlar = [100.00, 149.99, 248.65, 300.00, 23.50, 12.75]

Siparisler = []

while True:
    secim = ""

    print("1- Menüyü Yazdır")
    print("2- Sipariş Ekle")
    print("3- Son Siparişi Sil")
    print("4- Hesabı Kes")

    secim = input("Lütfen Seçim Yapınız")

    if secim == "1":
        i = 0
        while i < len(MenuYemekler):
            print(f"{i + 1} - {MenuYemekler[i]} - {MenuFiyatlar[i]}TL")
            i += 1
    elif secim == "2":
        siparis_secenegi = int(input("Lütfen Kaçıncı İtemi Eklemek İstediğinizi Giriniz")) - 1

        if siparis_secenegi < 0 or siparis_secenegi > len(MenuYemekler):
            print("Geçerli Bir Değer Girmediniz")

        Siparisler.append(siparis_secenegi)
    elif secim == "3":
        if len(Siparisler) > 0:
            Siparisler.pop()
        else:
            print("Son Sipariş Bulunmamaktadır")
    elif secim == "4":
        i = 0
        ToplamUcret = 0
        while i < len(Siparisler):
            print(f"{i + 1} - {MenuYemekler[i]} - {MenuFiyatlar[i]}TL")
            ToplamUcret += Siparisler[i]
            i += 1

        print(f"Toplam Tutar: {ToplamUcret}")
        break
    else:
        print("Hatalı Bir Seçim Yaptınız")
