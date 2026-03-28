# BTK_Final
BTK Akademi iler seviye makine öğrenmesi ve derin öğrenme final dosyalarını içermektedir 
# 🎓 Öğrenci Terki ve Başarı Tahmini (Erken Uyarı Sistemi)

Bu proje, yükseköğretim kurumlarında öğrencilerin okulu bırakma (**dropout**) riskini henüz gerçekleşmeden tespit eden, veri odaklı bir **Erken Uyarı Sistemi** tasarımıdır.

## 🚀 Proje Amacı
Eğitimde "reaktif" (sorun çıktıktan sonra müdahale eden) yaklaşım yerine; [cite_start]öğrencinin demografik profili ve ilk dönem performans sinyalleri üzerinden **proaktif** bir koruma mekanizması oluşturmaktır.

## 🛠️ Teknik Özellikler & Yöntem
Proje, veri sızıntısını (Data Leakage) önleyen profesyonel **Scikit-Learn Pipeline** mimarisi üzerine kurulmuştur.

*Veri Ön İşleme:** Eksik veriler `IterativeImputer` ile tamamlanmış, aykırı değerler özel `OutlierClipper` (%1-%99 persentil) ile temizlenmiş ve veriler `RobustScaler` ile ölçeklendirilmiştir.
* [cite_start]**Sınıf Dengelenmesi:** Gerçek dünya verilerindeki dengesizliği (mezuniyet oranlarının terk oranlarından fazla olması) çözmek için **SMOTE** algoritması kullanılmıştır.
* **Model:** Yüksek genelleme başarısı sunan **Random Forest Classifier** tercih edilmiş; [cite_start]Bootstrap Sampling ve Feature Subsampling teknikleri uygulanmıştır.
* Optimizasyon:** En iyi model konfigürasyonu için `GridSearchCV` ve 5-fold `StratifiedKFold` doğrulama kullanılmıştır.

## 📊 Performans ve Bulgular
[cite_start]Model, test verisi üzerinde **%90'ın üzerinde doğruluk** (accuracy) oranına ulaşmıştır[cite: 84].

* [cite_start]**Mezuniyet Tahmini:** 442 mezun öğrenciden 423'ü (%95.7) doğru tahmin edilmiştir[cite: 78].
* [cite_start]**Terk (Dropout) Tahmini:** 284 terk eden öğrenciden 236'sı doğru tespit edilmiştir[cite: 79].

### En Kritik 5 Belirleyici Faktör:
1.  **2. [cite_start]Yarıyıl Onaylanan Krediler (%19 etki):** En güçlü mezuniyet sinyali[cite: 110, 143].
2.  **1. [cite_start]Yarıyıl Onaylanan Krediler:** İlk dönem adaptasyon başarısı[cite: 111].
3.  [cite_start]**Akademik Not Ortalamaları:** Kredi başarısıyla paralel seyreden etki[cite: 112].
4.  [cite_start]**Harç Ödeme Durumu:** Finansal istikrarın akademik odaklanmaya etkisi[cite: 113, 114].
5.  [cite_start]**Burs Durumu:** Maddi desteğin okulda kalma eğilimini artırması[cite: 115].

## 🔍 Açıklanabilirlik (XAI)
Modelin "kara kutu" doğasını kırmak için Oyun Teorisi temelli **SHAP (SHapley Additive exPlanations)** analizi kullanılmıştır.Bu sayede modelin kararları öznitelik ağırlıkları bazında gerekçelendirilebilmektedir.

---

## 👨‍💻 Hazırlayan
**Yunus Ayyıldız**
* Yönetim Bilişim Sistemleri
* 📩 ayyildizy824@gmail.com
* 🔗 [LinkedIn](https://www.linkedin.com/in/yunus-ayy%C4%B1ld%C4%B1z-80527a2b9/) [cite: 149]

---
*Bu çalışma BTK Akademi Makine Öğrenmesi Atölyesi final projesi kapsamında geliştirilmiştir.*
