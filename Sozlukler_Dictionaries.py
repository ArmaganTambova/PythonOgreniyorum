"""
SÖZLÜKLER (DICTIONARIES)

Şu ana kadar gördüğümüz Listeler (Lists), verileri sıralı bir şekilde tutuyordu.
Veriye ulaşmak için indeks numarasını (0, 1, 2) bilmemiz gerekiyordu.

Sözlükler ise verileri 'Anahtar' (Key) ve 'Değer' (Value) çiftleri halinde tutar.
Tıpkı gerçek bir sözlük gibi: Kelimeyi (Key) ararsınız, karşılığında anlamını (Value) bulursunuz.
"""

# ================================================================
# 1. SÖZLÜK OLUŞTURMA
# ================================================================

"""
Sözlükler süslü parantez {} ile tanımlanır.
Yapısı şöyledir: { "Anahtar" : "Değer" , "Anahtar2" : "Değer2" }
"""

print("--- 1. Sözlük Tanımlama ---")

# Boş sözlük
bos_sozluk = {}

# Öğrenci bilgi kartı (Sözlük kullanımı için harika bir örnektir)
ogrenci = {
    "isim": "Dilara",
    "yas": 24,
    "bolum": "Bilgisayar Mühendisliği",
    "ortalama": 3.45,
    "mezun_mu": False
}

print(ogrenci)


# ================================================================
# 2. VERİLERE ERİŞİM
# ================================================================

"""
Listelerde ogrenci[0] diyorduk.
Sözlüklerde ise ogrenci["isim"] diyoruz. Sıra numarası yok, anahtar kelime var.
"""

print("\n--- 2. Verilere Erişim ---")

print("Öğrencinin Adı:", ogrenci["isim"])
print("Öğrencinin Bölümü:", ogrenci["bolum"])

# Eğer olmayan bir anahtarı sorarsanız (örn: ogrenci["adres"]), Python hata verir (KeyError).
# Bunu önlemek için .get() metodu kullanılır. Varsa getirir, yoksa None döndürür.
print("Adres (get ile):", ogrenci.get("adres")) # Hata vermez, None yazar.


# ================================================================
# 3. VERİ EKLEME VE GÜNCELLEME
# ================================================================

"""
Sözlükler de listeler gibi değiştirilebilir (Mutable) yapılardır.
"""

print("\n--- 3. Ekleme ve Güncelleme ---")

# Yeni veri ekleme
ogrenci["sehir"] = "İstanbul"
print("Şehir eklendi:", ogrenci)

# Mevcut veriyi güncelleme
ogrenci["ortalama"] = 3.80 # Notu yükseldi
print("Ortalama güncellendi:", ogrenci["ortalama"])


# ================================================================
# 4. VERİ SİLME
# ================================================================

print("\n--- 4. Veri Silme ---")

# pop("Anahtar") metodu ile silinir.
silinen_yas = ogrenci.pop("yas")
print("Yaş bilgisi silindi:", silinen_yas)
print("Son Durum:", ogrenci)


# ================================================================
# 5. SÖZLÜKLERDE DÖNGÜ (İLERİ SEVİYE ERİŞİM)
# ================================================================

"""
Bir sözlüğün içindeki tüm verileri for döngüsü ile gezebiliriz.
Bunun için 3 farklı yöntem vardır:
1. .keys()   -> Sadece anahtarları verir.
2. .values() -> Sadece değerleri verir.
3. .items()  -> Hem anahtarı hem değeri verir (En çok kullanılan).
"""

print("\n--- 5. Sözlük Üzerinde Gezinme ---")

# Sadece Anahtarlar
print("--- Anahtarlar ---")
for anahtar in ogrenci.keys():
    print(anahtar)

# Sadece Değerler
print("\n--- Değerler ---")
for deger in ogrenci.values():
    print(deger)

# Hem Anahtar Hem Değer (En Sık Kullanılan)
print("\n--- Anahtar ve Değer ---")
for anahtar, deger in ogrenci.items():
    print(anahtar + " : " + str(deger))


# ================================================================
# 6. İÇ İÇE SÖZLÜKLER (NESTED DICTIONARIES)
# ================================================================

"""
Gerçek hayatta veriler karmaşıktır. Bir sözlüğün içinde başka bir sözlük veya liste olabilir.
Örneğin bir sınıftaki öğrencileri tutalım.
"""

print("\n--- 6. İç İçe Yapılar ---")

sinif = {
    "ogrenci1": {
        "isim": "Ahmet",
        "notlar": [10, 20, 30] # Sözlük içinde Liste!
    },
    "ogrenci2": {
        "isim": "Ayşe",
        "notlar": [90, 100, 100]
    }
}

# Ayşe'nin 2. sınav notuna erişelim:
# Önce sinif["ogrenci2"] -> Sonra ["notlar"] -> Sonra [1]
aysenin_notu = sinif["ogrenci2"]["notlar"][1]
print("Ayşe'nin 2. sınav notu:", aysenin_notu)