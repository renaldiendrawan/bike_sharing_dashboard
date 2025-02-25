import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Atur gaya Seaborn untuk tampilan yang modern dan konsisten
sns.set(style="whitegrid", context="talk")

# Tentukan path absolut ke file main_data.csv berdasarkan lokasi file dashboard.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "main_data.csv")

def main():
    st.title("Bike Sharing Dashboard")
    
    # ============================
    # Load Data dan Preview
    # ============================
    try:
        main_data_df = pd.read_csv(data_path)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return

    st.subheader("Data Preview")
    st.write(main_data_df.head())
    
    # ============================
    # Analysis 1: Rentals by Season & Weather
    # ============================
    st.header("Analysis 1: Rentals by Season & Weather")
    if 'season' in main_data_df.columns and 'weathersit' in main_data_df.columns:
        season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
        weathersit_mapping = {1: "Clear", 2: "Mist", 3: "Light Rain/Snow", 4: "Heavy Rain/Snow"}
        main_data_df['season_cat'] = main_data_df['season'].map(season_mapping)
        main_data_df['weathersit_cat'] = main_data_df['weathersit'].map(weathersit_mapping)
        
        # Agregasi: rata-rata penyewaan per kombinasi kategori
        agg_df = main_data_df.groupby(['season_cat', 'weathersit_cat'])['cnt'].mean().reset_index()
        agg_df.rename(columns={'cnt': 'avg_rental'}, inplace=True)
        
        fig1, ax1 = plt.subplots(figsize=(8,5))
        sns.barplot(data=agg_df, x='season_cat', y='avg_rental', hue='weathersit_cat', palette="viridis", ax=ax1)
        ax1.set_xlabel("Season", fontsize=12)
        ax1.set_ylabel("Average Rental Count", fontsize=12)
        ax1.set_title("Average Bike Rentals by Season & Weather", fontsize=14)
        # Legend ditempatkan di luar area diagram untuk menghindari tumpang tindih
        ax1.legend(title="Weather", bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=10, title_fontsize=11)
        st.pyplot(fig1)
        
        st.markdown("""
        **Diagram 1: Average Bike Rentals by Season & Weather**  
        Diagram ini menampilkan rata-rata penyewaan sepeda berdasarkan kombinasi musim dan kondisi cuaca.
        """)
    else:
        st.warning("Kolom 'season' atau 'weathersit' tidak ditemukan dalam data.")
    
    # ============================
    # Analysis 2: Temperature, Humidity & Rental Count
    # ============================
    st.header("Analysis 2: Temperature, Humidity & Rental Count")
    if all(col in main_data_df.columns for col in ['temp', 'hum', 'cnt']):
        # Membuat kategori kelembapan agar lebih mudah dibaca
        hum_bins = [main_data_df['hum'].min()-0.1, main_data_df['hum'].quantile(0.33), 
                    main_data_df['hum'].quantile(0.66), main_data_df['hum'].max()]
        hum_labels = ['Low', 'Medium', 'High']
        main_data_df['hum_cat'] = pd.cut(main_data_df['hum'], bins=hum_bins, labels=hum_labels)
        
        fig2, ax2 = plt.subplots(figsize=(8,5))
        sns.scatterplot(data=main_data_df, x='temp', y='cnt', hue='hum_cat', palette="coolwarm", s=80, ax=ax2)
        ax2.set_xlabel("Temperature", fontsize=12)
        ax2.set_ylabel("Rental Count", fontsize=12)
        ax2.set_title("Temperature vs. Rental Count by Humidity Category", fontsize=14)
        # Letakkan legend di luar agar tidak mengganggu area plot
        ax2.legend(title="Humidity", bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=10, title_fontsize=11)
        st.pyplot(fig2)
        
        st.markdown("""
        **Diagram 2: Temperature vs. Rental Count by Humidity Category**  
        Diagram ini menggambarkan hubungan antara suhu dan jumlah penyewaan, dengan kelembapan dikategorikan sebagai *Low*, *Medium*, dan *High*.  
        """)
    else:
        st.warning("Kolom 'temp', 'hum', atau 'cnt' tidak ditemukan dalam data.")
    
    # ============================
    # Additional Visualizations: Histogram & Boxplot
    # ============================
    st.header("Additional Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Histogram of Rental Count**")
        fig3, ax3 = plt.subplots(figsize=(6,4))
        sns.histplot(main_data_df, x='cnt', bins=30, color="#2ca02c", ax=ax3)
        ax3.set_title("Histogram of Rental Count", fontsize=12)
        ax3.set_xlabel("Rental Count", fontsize=10)
        ax3.set_ylabel("Frequency", fontsize=10)
        st.pyplot(fig3)
    with col2:
        st.markdown("**Boxplot of Rental Count**")
        fig4, ax4 = plt.subplots(figsize=(6,4))
        sns.boxplot(data=main_data_df, x='cnt', color="#d62728", ax=ax4)
        ax4.set_title("Boxplot of Rental Count", fontsize=12)
        ax4.set_xlabel("Rental Count", fontsize=10)
        st.pyplot(fig4)
    
    # ============================
    # Advanced Analysis: RFM Analysis & Clustering (Manual Binning)
    # ============================
    st.header("Advanced Analysis: RFM Analysis & Clustering")
    if 'dteday' in main_data_df.columns:
        max_date = pd.to_datetime(main_data_df['dteday']).max()
        main_data_df['Recency'] = (max_date - pd.to_datetime(main_data_df['dteday'])).dt.days
        main_data_df['Frequency'] = main_data_df['cnt']      # Asumsi: frequency = cnt
        main_data_df['Monetary'] = main_data_df['cnt']         # Asumsi: 1 sewa = 1 dollar
        
        # Visualisasi RFM dengan boxplot untuk seluruh data
        fig5, ax5 = plt.subplots(1, 3, figsize=(16,5))
        sns.boxplot(y=main_data_df['Recency'], ax=ax5[0], color="#a6cee3")
        ax5[0].set_title("Recency Distribution", fontsize=12)
        ax5[0].set_ylabel("Days", fontsize=10)
        
        sns.boxplot(y=main_data_df['Frequency'], ax=ax5[1], color="#1f78b4")
        ax5[1].set_title("Frequency Distribution", fontsize=12)
        ax5[1].set_ylabel("Transaction Count", fontsize=10)
        
        sns.boxplot(y=main_data_df['Monetary'], ax=ax5[2], color="#b2df8a")
        ax5[2].set_title("Monetary Distribution", fontsize=12)
        ax5[2].set_ylabel("Dollar Value", fontsize=10)
        st.pyplot(fig5)
        
        st.markdown("""
        **Diagram 3: RFM Analysis**  
        Diagram ini menampilkan distribusi keseluruhan metrik RFM:  
        - *Recency:* Jumlah hari sejak transaksi terakhir.  
        - *Frequency:* Jumlah transaksi harian.  
        - *Monetary:* Nilai total transaksi harian.  
        Nilai yang rendah pada Recency dan tinggi pada Frequency/Monetary menunjukkan aktivitas transaksi yang tinggi.
        """)
    else:
        st.warning("Kolom 'dteday' tidak ditemukan untuk RFM Analysis.")
    
    st.markdown("**Clustering (Manual Binning): Rental Count Categories**")
    bins = [0, 100, 200, 300, 400, main_data_df['cnt'].max()]
    cluster_labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
    main_data_df['cnt_cluster'] = pd.cut(main_data_df['cnt'], bins=bins, labels=cluster_labels)
    
    fig6, ax6 = plt.subplots(figsize=(8,4))
    sns.countplot(data=main_data_df, x='cnt_cluster', order=cluster_labels, palette="mako", ax=ax6)
    ax6.set_xlabel("Rental Count Category", fontsize=12)
    ax6.set_ylabel("Number of Days", fontsize=12)
    ax6.set_title("Distribution of Rental Count Categories", fontsize=14)
    st.pyplot(fig6)
    
    st.markdown("""
    **Diagram 4: Distribution of Rental Count Categories**  
    Diagram ini menyajikan distribusi hari berdasarkan kategori penyewaan.  
    Kategori ini membantu mengidentifikasi pola performa: banyak hari dengan kategori *Very Low* atau *High* dapat menandakan perlunya penyesuaian strategi operasional.
    """)

if __name__ == "__main__":
    main()
