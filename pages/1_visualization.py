import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from models.modelbaru import get_data_with_membership, get_membership_ranges

# ======= Konfigurasi Halaman =======

st.set_page_config(
    page_title="Visualisasi Data E-Commerce",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Visualisasi Data E-Commerce")
st.write("Halaman ini menampilkan berbagai visualisasi dari dataset e-commerce berdasarkan status membership.")

# ======= Load Data =======

@st.cache_data
def load_and_process_data():
    df, bins = get_data_with_membership()
    range_df = get_membership_ranges(bins)
    return df, range_df

df, range_df = load_and_process_data()

# ======= Sidebar Filter =======

st.sidebar.header("🔍 Filter Data")

membership_options = ["Semua", "New", "Developing", "Loyal", "VIP"]
membership_filter = st.sidebar.selectbox(
    "Status Membership",
    options=membership_options
)

# Terapkan filter ke dataframe
if membership_filter != "Semua":
    filtered_df = df[df["Membership_Group"] == membership_filter]
else:
    filtered_df = df.copy()

st.write(f"Menampilkan **{len(filtered_df)} data** dari total {len(df)} data.")

# ======= Visualisasi =======

st.subheader("📊 Rentang Durasi Membership")
st.write("Pembagian klasifikasi membership berdasarkan durasi bergabung (dalam tahun):")
st.dataframe(range_df, use_container_width=True, hide_index=True)

st.subheader("📊 Distribusi Data")

# Baris pertama: 2 chart
col1, col2 = st.columns(2)

with col1:
    st.write("**Waktu Akses Aplikasi**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(filtered_df["Time on App"], bins=20, color="steelblue", kde=True, ax=ax)
    ax.set_xlabel("Waktu Akses Aplikasi (menit)")
    ax.set_ylabel("Jumlah")
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.write("**Waktu Akses Website**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(filtered_df["Time on Website"], bins=20, color="coral", kde=True, ax=ax)
    ax.set_xlabel("Waktu Akses Website (menit)")
    ax.set_ylabel("Jumlah")
    st.pyplot(fig)
    plt.close(fig)

# Baris kedua: 2 chart
col3, col4 = st.columns(2)

with col3:
    st.write("**Rata-Rata Pengeluaran per Kategori Membership**")
    fig, ax = plt.subplots(figsize=(6, 4))
    avg_spending = df.groupby('Membership_Group', observed=False)['Yearly Amount Spent'].mean().reset_index()
    sns.barplot(x="Membership_Group", y="Yearly Amount Spent", data=avg_spending, ax=ax, palette="viridis")
    ax.set_xlabel("Status Membership")
    ax.set_ylabel("Rata-rata Pengeluaran Tahunan ($)")
    st.pyplot(fig)
    plt.close(fig)

with col4:
    st.write("**Hubungan Lama Membership dan Pengeluaran**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x="Length of Membership", y="Yearly Amount Spent", hue="Membership_Group", data=filtered_df, ax=ax, palette="viridis")
    ax.set_xlabel("Lama Membership (tahun)")
    ax.set_ylabel("Pengeluaran Tahunan ($)")
    st.pyplot(fig)
    plt.close(fig)

# ======= Tampilkan Dataframe =======

st.subheader("📄 Data Hasil Filter")
st.dataframe(filtered_df[["Avatar", "Avg. Session Length", "Time on App", "Time on Website", "Length of Membership", "Yearly Amount Spent"]], use_container_width=True)
