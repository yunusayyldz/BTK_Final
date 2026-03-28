# 🎓 Öğrenci Terki ve Başarı Tahmini (Erken Uyarı Sistemi)

Bu proje, yükseköğretim kurumlarında öğrencilerin okulu bırakma (**dropout**) riskini henüz gerçekleşmeden tespit eden, veri odaklı bir **Erken Uyarı Sistemi** tasarımıdır.

## 🚀 Proje Amacı
Eğitimde "reaktif" (sorun çıktıktan sonra müdahale eden) yaklaşım yerine; [cite_start]öğrencinin demografik profili ve ilk dönem performans sinyalleri üzerinden **proaktif** bir koruma mekanizması oluşturmaktır.

## 🛠️ Teknik Özellikler & Yöntem
Proje, veri sızıntısını (Data Leakage) önleyen profesyonel **Scikit-Learn Pipeline** mimarisi üzerine kurulmuştur.

*Veri Ön İşleme:** Eksik veriler `IterativeImputer` ile tamamlanmış, aykırı değerler özel `OutlierClipper` (%1-%99 persentil) ile temizlenmiş ve veriler `RobustScaler` ile ölçeklendirilmiştir.
Sınıf Dengelenmesi:** Gerçek dünya verilerindeki dengesizliği (mezuniyet oranlarının terk oranlarından fazla olması) çözmek için **SMOTE** algoritması kullanılmıştır.
* **Model:** Yüksek genelleme başarısı sunan **Random Forest Classifier** tercih edilmiş; Bootstrap Sampling ve Feature Subsampling teknikleri uygulanmıştır.
* Optimizasyon:** En iyi model konfigürasyonu için `GridSearchCV` ve 5-fold `StratifiedKFold` doğrulama kullanılmıştır.

## 📊 Performans ve Bulgular
Model, test verisi üzerinde **%90'ın üzerinde doğruluk** (accuracy) oranına ulaşmıştır.

* **Mezuniyet Tahmini:** 442 mezun öğrenciden 423'ü (%95.7) doğru tahmin edilmiştir.
* **Terk (Dropout) Tahmini:** 284 terk eden öğrenciden 236'sı doğru tespit edilmiştir.

### En Kritik 5 Belirleyici Faktör:
1.  Yarıyıl Onaylanan Krediler (%19 etki):** En güçlü mezuniyet sinyali.
2.  Yarıyıl Onaylanan Krediler: İlk dönem adaptasyon başarısı.
3.  Akademik Not Ortalamaları: Kredi başarısıyla paralel seyreden etki.
4.  Harç Ödeme Durumu: Finansal istikrarın akademik odaklanmaya etkisi.
5.  Burs Durumu: Maddi desteğin okulda kalma eğilimini artırması.

## 🔍 Açıklanabilirlik (XAI)
Modelin "kara kutu" doğasını kırmak için Oyun Teorisi temelli **SHAP (SHapley Additive exPlanations)** analizi kullanılmıştır.Bu sayede modelin kararları öznitelik ağırlıkları bazında gerekçelendirilebilmektedir.

---<img width="1294" height="861" alt="Ekran görüntüsü 2026-03-28 160446" src="https://github.com/user-attachments/assets/d359aade-0ee2-456d-b522-7fe7b3a2c19b" />
<img width="821" height="701" alt="Ekran görüntüsü 2026-03-28 160438" src="https://github.com/user-attachments/assets/e138c61d-2ccd-4225-bba3-be2dede45669" />

## 📦 Veri : https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention

## 👨‍💻 Hazırlayan
**Yunus Ayyıldız**
* Yönetim Bilişim Sistemleri
* 📩 ayyildizy824@gmail.com
* 🔗 [LinkedIn](https://www.linkedin.com/in/yunus-ayy%C4%B1ld%C4%B1z-80527a2b9/) [cite: 149]

---
# BTK_Final
BTK Akademi iler seviye makine öğrenmesi ve derin öğrenme final dosyalarını içermektedir 
*Bu çalışma BTK Akademi Makine Öğrenmesi Atölyesi final projesi kapsamında geliştirilmiştir.*
