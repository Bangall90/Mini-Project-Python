# 📚 Sistem Perpustakaan Sederhana (Python)

Sistem Perpustakaan Sederhana merupakan aplikasi berbasis **Python** yang dijalankan melalui **Command Line Interface (CLI)**. Program ini dirancang untuk membantu pengelolaan data buku dan proses peminjaman dengan menggunakan file **CSV** sebagai media penyimpanan data, sehingga tidak memerlukan database seperti MySQL atau SQLite.

Seluruh data buku disimpan pada file **books.csv**, sedangkan data peminjam disimpan pada file **peminjam.csv**. Program akan membuat kedua file tersebut secara otomatis apabila belum tersedia.

## ✨ Fitur

- Menambahkan data buku baru
- Menampilkan seluruh daftar buku
- Mengedit informasi buku
- Menghapus data buku
- Mencari buku berdasarkan ID atau judul
- Meminjam buku (stok otomatis berkurang)
- Menampilkan data peminjam
- Mengembalikan buku (stok otomatis bertambah dan data peminjam dihapus)

## 🛠️ Teknologi yang Digunakan

- Python 3
- Modul `csv`
- Modul `os`

## 🧠 Konsep yang Dipelajari

Project ini menerapkan beberapa konsep dasar pemrograman Python, antara lain:

- Function
- Percabangan (`if`, `elif`, `else`)
- Perulangan (`while`, `for`)
- List
- Dictionary
- File Handling
- CSV Reader & Writer
- CRUD (Create, Read, Update, Delete)
- Pencarian Data
- Manajemen Stok Buku

## ⚙️ Cara Kerja Program

1. Program memeriksa apakah file `books.csv` dan `peminjam.csv` sudah tersedia.
2. Jika file belum ada, program akan membuat file beserta header secara otomatis.
3. Pengguna memilih menu sesuai kebutuhan.
4. Data dibaca menggunakan `csv.DictReader()`.
5. Saat data diubah (edit, hapus, pinjam, atau kembalikan), seluruh data akan dibaca terlebih dahulu, diperbarui di memori, kemudian ditulis kembali ke file CSV menggunakan `csv.DictWriter()`.

## 📋 Menu Program

```
1. Tambah Buku
2. Lihat Buku
3. Edit Buku
4. Hapus Buku
5. Cari Buku
6. Pinjam Buku
7. Data Peminjam
8. Kembalikan Buku
9. Keluar
```

## 📌 Tujuan Project

Project ini dibuat sebagai media pembelajaran untuk memahami konsep dasar Python, pengelolaan file CSV, implementasi CRUD, serta simulasi sistem perpustakaan sederhana tanpa menggunakan database.

## 📄 Lisensi

Project ini menggunakan lisensi **MIT License**.
