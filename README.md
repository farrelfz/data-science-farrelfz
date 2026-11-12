# Data Science Portfolio — Farrel Fauzan

Kumpulan proyek data science end-to-end: analisis eksploratif, pemodelan prediktif
(ANN & machine learning klasik), dan aplikasi interaktif berbasis Streamlit.

| Proyek | Deskripsi | Teknologi |
|---|---|---|
| [`attrition/`](attrition/) | Diagnosis & prediksi risiko attrition (pengunduran diri) karyawan dari data historis HR — aplikasi Streamlit multi-halaman + Artificial Neural Network | Python, TensorFlow/Keras, Streamlit, pandas |
| [`insurance/`](insurance/) | Estimasi biaya premi asuransi kesehatan — aplikasi Streamlit + model regresi terlatih | Python, scikit-learn, Streamlit |
| [`subscription/`](subscription/) | Prediksi langganan pelanggan e-commerce — aplikasi Streamlit + model terlatih | Python, scikit-learn, Streamlit |
| [`data/`](data/) | Dataset yang dipakai proyek-proyek di atas | CSV, XLSX |

## Menjalankan

Tiap aplikasi mandiri:

```bash
cd attrition       # atau insurance / subscription
pip install -r requirements.txt
streamlit run app.py
```

Notebook eksplorasi & pemodelan ada di `attrition/notebook/` (MP01: EDA & preprocessing,
MP02: ANN modeling & evaluasi).

## Skill yang ditunjukkan

- **Exploratory Data Analysis** — pembersihan, visualisasi, dan pemahaman pola data tabular (pandas, matplotlib/seaborn)
- **Pemodelan prediktif** — Artificial Neural Network (TensorFlow/Keras) dan machine learning klasik (scikit-learn: regresi, klasifikasi)
- **Evaluasi model** — metrik klasifikasi/regresi, validasi, dan tuning
- **Deployment** — model dikemas sebagai aplikasi web interaktif (Streamlit)
- **Manajemen artefak** — model terlatih (`.keras`, `.joblib`) dan dataset dikelola rapi per proyek

## Catatan

- Model terlatih ikut disimpan karena dipakai langsung oleh aplikasi Streamlit.
- Dataset besar (`data/mamikos/`) disimpan apa adanya; kalau repositori membesar, pindahkan ke GitHub Releases.
- Dataset yang dipakai `attrition/` ada di `attrition/data/` agar aplikasi tetap bisa dijalankan dari foldernya sendiri; salinan dataset bersama ada di `data/datasets/`.
