import streamlit as st
import pandas as pd
import joblib

# ======= Konfigurasi Halaman =======
st.set_page_config(
    page_title="Prediksi Biaya Asuransi",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Prediksi Biaya Asuransi")
st.write("Masukkan data pasien untuk mendapatkan estimasi biaya asuransi kesehatan.")

# ======= Load Model =======
@st.cache_resource
def load_model():
    model = joblib.load("models/insurance_model.joblib")
    return model

model = load_model()

# ======= Form Input =======
st.subheader("📝 Isi Data Pasien")

col1, col2 = st.columns(2)

col1.number_input("Usia (tahun):", min_value=18, max_value=64, value=30, key="age")
col1.number_input("BMI (Body Mass Index):", min_value=15.0, max_value=54.0, value=25.0, step=0.1, key="bmi")
col1.number_input("Jumlah Anak:", min_value=0, max_value=5, value=0, key="children")

col2.selectbox("Jenis Kelamin:", options=["male", "female"], key="sex")
col2.selectbox("Status Perokok:", options=["no", "yes"], key="smoker")
col2.selectbox("Region:", options=["southwest", "southeast", "northwest", "northeast"], key="region")

# ======= Tombol Prediksi =======
if st.button("🔮 Prediksi Sekarang", use_container_width=True):

    input_data = pd.DataFrame([{
        "age"     : st.session_state.age,
        "sex"     : st.session_state.sex,
        "bmi"     : st.session_state.bmi,
        "children": st.session_state.children,
        "smoker"  : st.session_state.smoker,
        "region"  : st.session_state.region
    }])

    prediction = model.predict(input_data)[0]

    st.divider()
    st.success(f"💰 Estimasi biaya asuransi: **${prediction:,.2f}**")
    st.info("ℹ️ Hasil ini adalah estimasi berdasarkan model Machine Learning, bukan angka pasti.")