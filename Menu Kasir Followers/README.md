#MENU KASIR FOLLOWERS

Aplikasi sederhana berbasis **Streamlit** yang mensimulasikan proses pembelian paket followers untuk berbagai platform media sosial. Pengguna dapat memilih paket followers, menambahkannya ke keranjang, melihat total harga, dan mengosongkan keranjang.

## ✨ Fitur

- Menampilkan daftar harga (pricelist) followers.
- Mendukung tiga platform media sosial:
  - TikTok
  - Instagram
  - Facebook
- Memilih paket followers melalui dropdown.
- Menambahkan produk ke keranjang.
- Menghitung total harga secara otomatis.
- Mengosongkan keranjang dengan tombol **Reset Keranjang**.
- Menggunakan `st.session_state` agar data keranjang tetap tersimpan selama aplikasi berjalan.

## 🛠️ Teknologi yang digunakan

- Python 3
- Streamlit

## ▶️ Cara Menjalankan

### 1. Clone repository
### 2. Masuk ke folder project
### 3. Install Library Streamlit Melalui Terminal
```bash
pip install streamlit
```

atau

```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi / program
```bash
streamlit run Menukasir_followers.py
```

## 📚 Konsep yang Dipelajari

Project ini dibuat sebagai latihan untuk mempelajari:

- Dictionary
- Session State (`st.session_state`)
- Streamlit Components
- Select Box
- Button
- Perhitungan Total
- Simulasi Keranjang Belanja

## 🎯 Tujuan Project

- Melatih penggunaan Streamlit.
- Memahami cara menyimpan data sementara menggunakan Session State.
- Menerapkan konsep dictionary pada Python.
- Membuat simulasi aplikasi sederhana dengan antarmuka web.

## 📄 Lisensi

Project ini menggunakan lisensi **MIT License**.
