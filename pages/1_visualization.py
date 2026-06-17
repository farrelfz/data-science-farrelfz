import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======= Konfigurasi Halaman =======

st.set_page_config(
    page_title="Visualisasi Data Asuransi",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Visualisasi Data Asuransi")
st.write("Halaman ini menampilkan berbagai visualisasi dari dataset asuransi kesehatan.")

# ======= Load Data =======

@st.cache_data
def load_data():
    df = pd.read_csv("data/insurance.csv")
    return df

df = load_data()


# ======= Sidebar Filter =======

st.sidebar.header("🔍 Filter Data")

smoker_filter = st.sidebar.selectbox(
    "Status Perokok:",
    options=["Semua", "Perokok", "Bukan Perokok"]
)

# Terapkan filter ke dataframe
if smoker_filter == "Perokok":
    filtered_df = df[df["smoker"] == "yes"]
elif smoker_filter == "Bukan Perokok":
    filtered_df = df[df["smoker"] == "no"]
else:
    filtered_df = df.copy()

st.write(f"Menampilkan **{len(filtered_df)} data** dari total {len(df)} data.")

# ======= Visualisasi =======

st.subheader("📈 Distribusi Data")

# Baris pertama: 2 chart
col1, col2 = st.columns(2)

with col1:
    st.write("**Distribusi Usia**")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(filtered_df["age"], bins=20, color="steelblue", edgecolor="white")
    ax.set_xlabel("Usia")
    ax.set_ylabel("Jumlah")
    st.pyplot(fig)
    plt.close(fig)  # penting: tutup figure setelah ditampilkan

with col2:
    st.write("**Distribusi BMI**")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(filtered_df["bmi"], bins=20, color="coral", edgecolor="white")
    ax.set_xlabel("BMI")
    ax.set_ylabel("Jumlah")
    st.pyplot(fig)
    plt.close(fig)

# Baris kedua: 2 chart
col3, col4 = st.columns(2)

with col3:
    st.write("**Charges berdasarkan Status Perokok**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x="smoker", y="charges", data=filtered_df, ax=ax)
    ax.set_xlabel("Status Perokok")
    ax.set_ylabel("Charges ($)")
    st.pyplot(fig)
    plt.close(fig)

with col4:
    st.write("**BMI vs Charges**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x="bmi", y="charges", hue="smoker", data=filtered_df, ax=ax)
    ax.set_xlabel("BMI")
    ax.set_ylabel("Charges ($)")
    st.pyplot(fig)
    plt.close(fig)

# ======= Tampilkan Dataframe =======

st.subheader("📄 Data Hasil Filter")
st.dataframe(filtered_df, use_container_width=True)

