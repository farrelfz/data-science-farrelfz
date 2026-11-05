# PPKD Data Science — Kumpulan Proyek

Monorepo proyek data science (PPKD Data Science Jakarta): aplikasi Streamlit, notebook, model, dan dataset.

Sebelumnya proyek-proyek ini tersebar di beberapa repositori terpisah — `analytics-employee`,
`insurance-app`, `langganan`, `mamikos`, `dataset-ppkd-2026`, dan `employee_salary` — yang sebagian
besar isinya kecil atau bahkan kosong. Semuanya disatukan di sini supaya tidak ada repositori ganda.
Riwayat commit tiap proyek tetap tersimpan sebagai merge commit di repositori ini.

## Isi

| Folder | Proyek | Catatan |
|---|---|---|
| [`attrition/`](attrition/) | Analisis & prediksi attrition karyawan | Streamlit multi-halaman + ANN (TensorFlow/Keras), notebook MP01–MP02, model terlatih |
| [`insurance/`](insurance/) | Estimasi biaya asuransi | Streamlit 2 halaman + model joblib |
| [`subscription/`](subscription/) | Prediksi langganan e-commerce | Streamlit 2 halaman + model joblib |
| [`data/`](data/) | Dataset mentah | `dataset-ppkd-2026/`, `mamikos/`, `employee-salary/` |

## Menjalankan

Tiap aplikasi mandiri:

```bash
cd attrition       # atau insurance / subscription
pip install -r requirements.txt
streamlit run app.py
```

## Catatan

- Model (`.keras`, `.joblib`) ikut disimpan karena dipakai langsung oleh aplikasi.
- Dataset besar (`data/mamikos/`) disimpan apa adanya; kalau repositori membesar, pindahkan ke GitHub Releases.
- Dataset yang dipakai `attrition/` ada di `attrition/data/` agar aplikasi tetap bisa dijalankan dari foldernya sendiri.