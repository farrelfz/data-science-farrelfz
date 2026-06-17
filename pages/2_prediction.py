import streamlit as st
import pandas as pd
from models.modelbaru import train_prediction_model

# ======= Konfigurasi Halaman =======

st.set_page_config(
    page_title="Prediksi Pengeluaran Pelanggan",
    page_icon="💡",
    layout="centered"
)

st.title("💡 Prediksi Pengeluaran Tahunan")
st.write("Masukkan data pelanggan di bawah ini untuk memprediksi perkiraan total pengeluaran tahunan mereka.")

# ======= Load Model =======

@st.cache_resource
def load_model():
    return train_prediction_model()

model = load_model()

# ======= Form Input =======

with st.form("prediction_form"):
    st.subheader("Data Pelanggan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        avg_session = st.number_input(
            "Rata-rata Panjang Sesi (Menit)", 
            min_value=0.0, 
            max_value=100.0, 
            value=33.0, 
            step=0.5,
            help="Rata-rata waktu pelanggan dalam satu sesi (Avg. Session Length)"
        )
        time_app = st.number_input(
            "Waktu di Aplikasi (Menit)", 
            min_value=0.0, 
            max_value=100.0, 
            value=12.0, 
            step=0.5,
            help="Total waktu yang dihabiskan pelanggan di aplikasi (Time on App)"
        )
        
    with col2:
        time_website = st.number_input(
            "Waktu di Website (Menit)", 
            min_value=0.0, 
            max_value=100.0, 
            value=37.0, 
            step=0.5,
            help="Total waktu yang dihabiskan pelanggan di website (Time on Website)"
        )
        length_membership = st.number_input(
            "Lama Keanggotaan (Tahun)", 
            min_value=0.0, 
            max_value=20.0, 
            value=3.5, 
            step=0.1,
            help="Sudah berapa lama pelanggan menjadi member (Length of Membership)"
        )
        
    submit_button = st.form_submit_button("Prediksi Pengeluaran 🚀")

# ======= Prediksi =======

if submit_button:
    # Siapkan data untuk prediksi
    input_data = pd.DataFrame({
        'Avg. Session Length': [avg_session],
        'Time on App': [time_app],
        'Time on Website': [time_website],
        'Length of Membership': [length_membership]
    })
    
    # Lakukan prediksi
    prediction = model.predict(input_data)[0]
    
    # Tampilkan hasil
    st.success("Prediksi Berhasil!")
    
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        padding: 20px;
        border: 2px solid #1E88E5;
        border-radius: 10px;
        background-color: #E3F2FD;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div class="big-font">Estimasi Pengeluaran Tahunan: ${prediction:,.2f}</div>', unsafe_allow_html=True)
    
    st.info("Prediksi ini menggunakan model Linear Regression berdasarkan data historis pelanggan.")