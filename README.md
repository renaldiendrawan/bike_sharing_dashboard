# Bike Sharing Dashboard

Dashboard ini merupakan proyek analisis data Bike Sharing yang menampilkan visualisasi interaktif menggunakan Streamlit. Proyek ini memanfaatkan data dari file CSV (misalnya `main_data.csv`) untuk menyajikan insight bisnis melalui berbagai grafik dan filter. Visualisasi yang disajikan di dashboard telah disusun secara konsisten dengan analisis di notebook, sehingga audiens dapat dengan mudah memahami temuan dan rekomendasi bisnis.

## Struktur Proyek

```
submission/
├── dashboard/
│   ├── main_data.csv     # Data utama untuk dashboard (hasil pembersihan dan penggabungan dari day.csv dan hour.csv)
│   ├── dashboard.py      # Script utama dashboard Streamlit
├── data/
│   ├── day.csv           # Data harian (opsional, sumber data asli)
│   ├── hour.csv          # Data per jam (opsional, sumber data asli)
├── notebook.ipynb        # Notebook eksplorasi dan analisis data
├── README.md             # Panduan menjalankan dashboard
├── requirements.txt      # Daftar dependency yang dibutuhkan
└── url.txt               # (Opsional) Link referensi atau dataset
```

## Cara Menjalankan Dashboard

### 1. Setup Environment

#### Menggunakan Anaconda

1. Buka terminal/Anaconda Prompt dan buat environment baru:
   ```bash
   conda create --name main-ds python=3.9
   conda activate main-ds
   ```
2. Install dependency yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

#### Menggunakan Shell/Terminal dengan Pipenv

1. Buka terminal dan masuk ke folder proyek:
   ```bash
   cd submission
   ```
2. Inisialisasi Pipenv dan install dependency:
   ```bash
   pipenv install
   pipenv shell
   pip install -r requirements.txt
   ```

### 2. Menjalankan Dashboard

Pastikan Anda berada di folder `submission`, lalu jalankan perintah:

```bash
streamlit run dashboard/dashboard.py
```

*Catatan:*  
- Pastikan file `dashboard.py` dan `main_data.csv` berada di dalam folder `dashboard`.  
- Jika terjadi error terkait file tidak ditemukan, pastikan path yang digunakan dalam `dashboard.py` sudah sesuai (menggunakan path absolut atau path relatif yang tepat).

## Troubleshooting

- **FileNotFoundError:**  
  Pastikan file `main_data.csv` sudah ada di folder `dashboard`. Untuk memeriksa, jalankan:
  ```python
  import os
  print(os.getcwd())
  print(os.listdir())
  ```
- **Dependency Error:**  
  Pastikan semua library yang dibutuhkan telah terinstall sesuai dengan versi yang ditentukan di `requirements.txt`.

---

Dengan mengikuti langkah-langkah di atas, Anda seharusnya dapat menjalankan dashboard dan menikmati visualisasi data interaktif yang telah disusun secara konsisten dengan analisis pada notebook.

Happy Coding! 🚀