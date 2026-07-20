# 💰 Aplikasi Manajemen Keuangan Sederhana Menggunakan Penyimpanan JSON

Aplikasi manajemen keuangan berbasis **command line (CLI)** yang dibuat menggunakan Python

Aplikasi ini cocok untuk pemula yang ingin belajar konsep dasar Python seperti list, dictionary, fungsi, perulangan, percabangan, dan penyimpanan data ke file.

## ✨ Fitur

- Tambah pemasukan
- Tambah pengeluaran
- Lihat riwayat transaksi
- Hitung saldo otomatis
- Hapus transaksi
- Data tersimpan permanen ke file `data_keuangan.json`

## 🛠️ Teknologi

- Python 3
- Modul bawaan `json` dan `os`

## 🚀 Cara Penggunaan

Silahkan jalankan program ini diterimal(CLI), Setelah dijalankan kamu akan melihat menu berikut:

```
=============================================
APLIKASI MANAJEMEN KEUANGAN SEDERHANA
=============================================
1. Tambah Pemasukan
2. Tambah Pengeluaran
3. Lihat Riwayat & Saldo
4. Hapus Transaksi
5. Keluar
=============================================
```

Pilih menu dengan mengetik angka 1-5, lalu ikuti instruksi yang muncul di layar.

Contoh menambah pemasukan:
```
Pilih menu (1-5): 1
Keterangan pemasukan: Gaji Bulanan
Jumlah pemasukan: 5000000
```

Semua transaksi akan otomatis tersimpan ke file `data_keuangan.json`, sehingga data tidak hilang saat program ditutup dan dibuka kembali.


## 🧩 Daftar Fungsi

| Fungsi | Deskripsi |
|---|---|
| `muat_data()` | Membaca data transaksi dari file JSON saat program dimulai |
| `simpan_data()` | Menyimpan list transaksi ke file JSON |
| `tambah_pemasukan()` | Menambahkan data pemasukan |
| `tambah_pengeluaran()` | Menambahkan data pengeluaran |
| `hitung_saldo()` | Menghitung total saldo dari seluruh transaksi |
| `tampilkan_riwayat()` | Menampilkan seluruh riwayat transaksi dan saldo |
| `hapus_transaksi()` | Menghapus transaksi berdasarkan nomor urut |
| `menu()` | Menampilkan tampilan menu utama |

## 📄 Lisensi

Project ini menggunakan lisensi **MIT License**.
