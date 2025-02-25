import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Atur gaya Seaborn untuk tampilan yang lebih modern
sns.set(style="whitegrid", context="talk")

# Tentukan path absolut ke file main_data.csv berdasarkan lokasi file ini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "main_data.csv")

def main():
    st.title("Bike Sharing Dashboard")
    
    # Load Data
    try:
        main_data_df = pd.read_csv(data_path)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return

    # Tampilkan preview data
    st.subheader("Data Preview")
    st.write(main_data_df.head())

    # Visualisasi: Distribusi Jumlah Sewa Harian
    st.subheader("Distribution of Daily Bike Rentals")
    fig, ax = plt.subplots(figsize=(10,5))
    sns.histplot(data=main_data_df, x='cnt', kde=True, ax=ax, color="#1f77b4", bins=30)
    ax.set_xlabel("Bike Rental Count")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Daily Bike Rentals")
    st.pyplot(fig)

    # Filter data berdasarkan season
    st.subheader("Filter by Season")
    if 'season' in main_data_df.columns:
        season_options = sorted(main_data_df['season'].unique())
        selected_season = st.selectbox("Select Season:", season_options)
        filtered_data = main_data_df[main_data_df['season'] == selected_season]
        st.write(filtered_data.head())

        # Visualisasi: Rata-rata Sewa Berdasarkan Kondisi Cuaca (weathersit)
        st.subheader("Average Rentals by Weathersit")
        if 'weathersit' in filtered_data.columns:
            avg_weathersit = filtered_data.groupby('weathersit')['cnt'].mean().reset_index()
            fig2, ax2 = plt.subplots(figsize=(8,5))
            sns.barplot(data=avg_weathersit, x='weathersit', y='cnt', palette="viridis", ax=ax2)
            ax2.set_xlabel("Weather Situation")
            ax2.set_ylabel("Average Rental Count")
            ax2.set_title("Average Rentals by Weather Condition")
            st.pyplot(fig2)
        else:
            st.warning("Kolom 'weathersit' tidak ditemukan dalam data.")
    else:
        st.warning("Kolom 'season' tidak ditemukan dalam data.")

    # Tambahkan opsi interaktif untuk memilih rentang nilai cnt (jika data cukup besar)
    st.subheader("Filter by Rental Count Range")
    min_cnt = int(main_data_df['cnt'].min())
    max_cnt = int(main_data_df['cnt'].max())
    cnt_range = st.slider("Select rental count range:", min_value=min_cnt, max_value=max_cnt, value=(min_cnt, max_cnt))
    cnt_filtered_df = main_data_df[(main_data_df['cnt'] >= cnt_range[0]) & (main_data_df['cnt'] <= cnt_range[1])]
    
    st.write(f"Data count after filtering: {cnt_filtered_df.shape[0]} rows")
    fig3, ax3 = plt.subplots(figsize=(10,5))
    sns.histplot(cnt_filtered_df, x='cnt', kde=True, color="#ff7f0e", bins=30, ax=ax3)
    ax3.set_title("Rental Count Distribution After Filtering")
    st.pyplot(fig3)

    # Layout kolom untuk menampilkan dua grafik berdampingan (misalnya: histogram dan boxplot)
    st.subheader("Additional Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Histogram Rental Count**")
        fig4, ax4 = plt.subplots(figsize=(6,4))
        sns.histplot(main_data_df, x='cnt', color="#2ca02c", bins=30, ax=ax4)
        ax4.set_title("Histogram of Rental Count")
        st.pyplot(fig4)
    with col2:
        st.markdown("**Boxplot Rental Count**")
        fig5, ax5 = plt.subplots(figsize=(6,4))
        sns.boxplot(data=main_data_df, x='cnt', color="#d62728", ax=ax5)
        ax5.set_title("Boxplot of Rental Count")
        st.pyplot(fig5)

if __name__ == "__main__":
    main()
