# Bike Sharing Dashboard

Dashboard ini merupakan proyek analisis data Bike Sharing yang menampilkan visualisasi interaktif menggunakan Streamlit. Proyek ini memanfaatkan data dari file CSV (misalnya `main_data.csv`) dan memberikan insight melalui berbagai grafik dan filter.

## Struktur Proyek

```
submission/
├── dashboard/
│   ├── main_data.csv     # Data utama untuk dashboard
│   ├── dashboard.py      # Script utama dashboard
├── data/
│   ├── day.csv        # Data tambahan (opsional)
│   ├── hour.csv        # Data tambahan (opsional)
├── notebook.ipynb        # Notebook eksplorasi data
├── README.md             # Panduan menjalankan dashboard
├── requirements.txt      # Dependency yang dibutuhkan
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
- Jika Anda mengalami error terkait file tidak ditemukan, pastikan path di dalam `dashboard.py` sudah menggunakan path absolut atau menyesuaikan dengan struktur proyek.

## Troubleshooting

- **FileNotFoundError:**  
  Pastikan file `main_data.csv` sudah ada di folder `dashboard`. Jika error muncul, cek juga working directory dengan:
  ```python
  import os
  print(os.getcwd())
  print(os.listdir())
  ```
- **Dependency Error:**  
  Pastikan semua library yang dibutuhkan telah terinstall sesuai versi yang ditentukan di `requirements.txt`.

---

Dengan mengikuti langkah-langkah di atas, Anda seharusnya dapat menjalankan dashboard dan mendapatkan visualisasi data interaktif dengan Streamlit.

Happy Coding! 🚀