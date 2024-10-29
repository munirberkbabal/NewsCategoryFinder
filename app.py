import tkinter as tk
import pickle

# 1. Eğitilmiş modeli yükleme (vektörizer Pipeline'ın içinde olabilir)
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# 2. Kategori isimlerini Türkçeye çevirme
kategori_map = {
    'u.s. news': 'ABD HABERLERİ',
    'comedy': 'KOMEDİ',
    'parenting': 'EBEVEYNLİK',
    'tech': 'TEKNOLOJİ',
    'sports': 'SPOR',
    'politics': 'POLİTİKA',
    'health': 'SAĞLIK',
    'entertainment': 'EĞLENCE',
    'world news': 'DÜNYA HABERLERİ'
}

# 3. Tahmin fonksiyonu
def tahmin_et():
    haber_basligi = entry.get()  # Kullanıcıdan başlık al
    if haber_basligi:
        kategori = model.predict([haber_basligi])  # Pipeline içindeki vektörizer otomatik olarak başlığı dönüştürür
        kategori_turkce = kategori_map.get(kategori[0].lower(), "Bilinmeyen Kategori")  # Kategoriyi Türkçeye çevir
        sonuc_label.config(text=f"Bu haber başlığı '{kategori_turkce}' kategorisine aittir.")  # Sonucu göster
    else:
        sonuc_label.config(text="Lütfen bir haber başlığı girin.")  # Hata mesajı

# 4. Analiz edilebilecek başlıklar
def analiz_edilebilecek_basliklar():
    return ("Bu uygulama aşağıdaki başlıkları analiz edebilir:\n"
            "- ABD HABERLERİ\n"
            "- KOMEDİ\n"
            "- EBEVEYNLİK\n"
            "- TEKNOLOJİ\n"
            "- SPOR\n"
            "- POLİTİKA\n"
            "- SAĞLIK\n"
            "- EĞLENCE\n"
            "- DÜNYA HABERLERİ")

# 5. Tkinter GUI ayarları
root = tk.Tk()
root.title("Haber Başlığı Sınıflandırma")
root.geometry("500x400")

label = tk.Label(root, text="Haber Başlığını Girin:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button_tahmin = tk.Button(root, text="Tahmin Et", command=tahmin_et)
button_tahmin.pack(pady=20)

# 6. Analiz edilebilecek başlıklar gösterme
basliklar_label = tk.Label(root, text=analiz_edilebilecek_basliklar(), justify=tk.LEFT)
basliklar_label.pack(pady=10)

sonuc_label = tk.Label(root, text="", wraplength=400, fg="blue")
sonuc_label.pack(pady=10)

# 7. Uygulamayı çalıştır
root.mainloop()
