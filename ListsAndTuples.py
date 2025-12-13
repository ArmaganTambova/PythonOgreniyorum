# LİSTELER (LISTS) VE DEMETLER (TUPLES)

"""
Şu ana kadar değişkenlerde sadece tek bir veri tutuyorduk (yas = 25 gibi).
Ancak gerçek hayatta veriler gruplar halindedir (Öğrenci listesi, Alışveriş sepeti vb.).
Python'da birden çok veriyi tek bir değişkende tutmak için 'Liste' yapılarını kullanırız.
"""

# ================================================================
# 1. LİSTE OLUŞTURMA VE ERİŞİM
# ================================================================

"""
Listeler köşeli parantez [] ile tanımlanır.
İçine string, int, float, boolean... her şeyi karışık koyabilirsiniz.
"""

print("--- 1. Liste Tanımlama ---")

# Boş liste
bos_liste = []

# Dolu liste
meyveler = ["Elma", "Armut", "Muz", "Çilek"]
notlar = [10, 50, 90, 100]
karisik_liste = ["Ahmet", 25, True, 3.14] # Python'da bu mümkündür!

print("Meyveler:", meyveler)
print("Karışık Liste:", karisik_liste)


"""
LİSTE ELEMANLARINA ERİŞİM (INDEXING):
Bilgisayarlar saymaya 0'dan başlar!
İlk eleman [0], ikinci eleman [1]... diye gider.
"""

print("\n--- 2. Elemanlara Erişim (Indexing) ---")

print("İlk meyve (Index 0):", meyveler[0])  # Elma
print("İkinci meyve (Index 1):", meyveler[1]) # Armut

# Negatif Indexing (Sondan başlama)
# -1 listenin EN SONUNDAKİ elemanı verir.
print("Son meyve (Index -1):", meyveler[-1]) # Çilek


# ================================================================
# 2. LİSTE METODLARI (EKLEME - SİLME - GÜNCELLEME)
# ================================================================

"""
Listeler 'Mutable' (Değiştirilebilir) yapılardır.
Yani sonradan eleman ekleyebilir, silebilir veya değiştirebiliriz.
"""

print("\n--- 3. Listeyi Değiştirme ---")

# 1. Veri Güncelleme
meyveler[1] = "Karpuz" # 'Armut' gitti, yerine 'Karpuz' geldi.
print("Güncel Liste:", meyveler)

# 2. Veri Ekleme (append) -> En sona ekler
meyveler.append("Portakal")
print("Portakal Eklendi:", meyveler)

# 3. Araya Veri Ekleme (insert) -> Belirtilen indexe ekler
meyveler.insert(0, "Kiraz") # 0. sıraya Kiraz'ı koy, diğerlerini kaydır.
print("Kiraz Başa Eklendi:", meyveler)

# 4. Veri Silme (remove) -> İsme göre siler
meyveler.remove("Muz")
print("Muz Silindi:", meyveler)

# 5. Veri Silme (pop) -> Indexe göre siler (veya sonuncuyu siler)
silinen = meyveler.pop() # En sonuncuyu (Portakal) siler ve bize verir.
print("Son eleman silindi:", silinen)
print("Son Durum:", meyveler)


# ================================================================
# 3. LİSTE PARÇALAMA (SLICING)
# ================================================================

"""
Listenin sadece belli bir kısmını almak istersek ':' kullanırız.
Mantık: [Başlangıç : Bitiş] (Bitiş dahil değildir!)
"""

print("\n--- 4. Liste Parçalama (Slicing) ---")

sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Tüm liste:", sayilar)
print("İlk 3 eleman [0:3]:", sayilar[0:3]) # 0, 1, 2
print("3. indeksten 6'ya kadar [3:6]:", sayilar[3:6]) # 3, 4, 5
print("Baştan 4. indekse kadar [:4]:", sayilar[:4]) # 0, 1, 2, 3


# ================================================================
# 4. DEMETLER (TUPLES)
# ================================================================

"""
Tuple (Demet), listelere çok benzer ama TEK BİR FARKI vardır:
Tuple'lar DEĞİŞTİRİLEMEZ (Immutable).
Yani bir kere oluşturduktan sonra eleman ekleyemez, silemez veya güncelleyemezsiniz.

Neden kullanılır?
- Değişmemesi gereken sabit veriler için (Örn: TC Kimlik No, Koordinatlar).
- Listelerden daha hızlı çalışır ve daha az yer kaplar.

Tanımlama: Normal parantez () kullanılır.
"""

print("\n--- 5. Demetler (Tuples) ---")

# Liste [] ile, Tuple () ile tanımlanır.
sabit_bilgiler = ("admin", "12345", "localhost")

print("Tuple:", sabit_bilgiler)
print("İlk eleman:", sabit_bilgiler[0])

# HATA ALMA DENEMESİ
# Aşağıdaki satırın yorumunu kaldırıp çalıştırırsanız hata alırsınız!
# sabit_bilgiler[0] = "yeni_admin"
# Hata: 'tuple' object does not support item assignment (Tuple değişimi desteklemez)


# ================================================================
# 5. len() FONKSİYONU
# ================================================================

"""
Bir listenin veya tuple'ın kaç elemanlı olduğunu bulmak için len() kullanılır.
(Length - Uzunluk kelimesinden gelir)
"""

print("\n--- 6. Uzunluk Bulma ---")

print("Meyveler listesinde kaç eleman var?:", len(meyveler))
print("Sabit bilgilerde kaç eleman var?:", len(sabit_bilgiler))