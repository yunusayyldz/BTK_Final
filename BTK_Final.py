import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
import os

def main():
    print("Veri seti yükleniyor...")
    try:
        # 1. Veri Hazırlığı ve Hedef Tanımlama
        # Dosyanın python betiğiyle aynı klasörden okunmasını garanti edelim:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dataset_path = os.path.join(script_dir, 'dataset.csv')
        df = pd.read_csv(dataset_path)
    except FileNotFoundError:
        print("Hata: 'dataset.csv' dosyası bulunamadı. Lütfen betik ile aynı klasörde olduğundan emin olun.")
        return

    # 'Target' sütununda 'Enrolled' olanları filtrele (sadece Dropout ve Graduate kalsın)
    df = df[df['Target'] != 'Enrolled'].copy()

    # 'Dropout' değerini 0, 'Graduate' değerini 1 olarak map et ve 'basari' adlı yeni sütuna aktar
    df['basari'] = df['Target'].map({'Dropout': 0, 'Graduate': 1})

    # Orijinal 'Target' sütununu kaldır
    df = df.drop('Target', axis=1)

    # Hedef ve özellikleri ayır
    X = df.drop('basari', axis=1)
    y = df['basari']

    # 2. Özellik Mühendisliği
    # Sayısal ve kategorik sütunları otomatik seç
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = X.select_dtypes(include=['object']).columns.tolist()

    # ColumnTransformer ile ön işleme (preprocessing)
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    # imblearn'den Pipeline oluştur (SMOTE dahil edildiği için scikit-learn Pipeline yerine imblearn Pipeline kullanılmalı)
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('smote', SMOTE(random_state=42)),
        ('classifier', RandomForestClassifier(class_weight='balanced', random_state=42))
    ])

    # 3. Model Eğitimi ve Validasyon
    # Veriyi %80 eğitim, %20 test olacak şekilde ayır, hedef değişkene göre stratify et
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("\nModel eğitiliyor ve 5-Katlı Çapraz Doğrulama (Cross-Validation) hesaplanıyor...")
    # 5 katlı Cross-Validation
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5)
    print(f"Çapraz Doğrulama Ortalama Skoru: {cv_scores.mean():.4f}")

    # Modeli tüm eğitim verisiyle eğit
    pipeline.fit(X_train, y_train)

    # 4. Değerlendirme ve Görselleştirme
    print("\nModel tahminleri yapılıyor...")
    y_pred = pipeline.predict(X_test)

    print("\n--- Model Değerlendirme Sonuçları ---")
    print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Confusion Matrix Görselleştirme
    disp = ConfusionMatrixDisplay.from_estimator(
        pipeline, X_test, y_test, 
        display_labels=['Dropout (0)', 'Graduate (1)'], 
        cmap=plt.cm.Blues
    )
    plt.title("Hata Matrisi (Confusion Matrix)")
    plt.show()

    # Feature Importance Görselleştirme (İlk 10 Özellik)
    try:
        # Preprocessor'dan transforme adımlarını alıp feature isimlerini elde edelim
        feature_names = pipeline.named_steps['preprocessor'].get_feature_names_out()
        importances = pipeline.named_steps['classifier'].feature_importances_
        
        # DataFrame içerisine alarak en yüksek 10 değeri sırala
        import numpy as np
        feat_importances = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        feat_importances = feat_importances.sort_values(by='Importance', ascending=False).head(10)
        
        plt.figure(figsize=(10, 6))
        # Yatay bar grafik (en önemlisi en üstte olsun diye ters çeviriyoruz)
        plt.barh(feat_importances['Feature'][::-1], feat_importances['Importance'][::-1], color='skyblue')
        plt.xlabel('Önem Derecesi (Feature Importance)')
        plt.title('En Etkili 10 Özellik')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"\nÖzellik isimleri alınırken bir hata oluştu (eski scikit-learn sürümü vb.): {e}")

if __name__ == "__main__":
    main()
