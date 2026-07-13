# 🔐 Login & Register Simpel

Program CLI (command line) sederhana untuk latihan konsep **login dan register** menggunakan Python dan database **SQLite3**. Dibuat sebagai project belajar dasar-dasar koneksi database, query SQL, dan struktur program modular.

## Fitur

- ✅ Registrasi akun baru (simpan username & password ke database)
- ✅ Login dengan validasi username & password
- ✅ Data tersimpan permanen di file `users.db` (tetap ada meski program ditutup)
- ✅ Struktur kode modular (dipisah per file: database, register, login)

## Struktur Project

```
Login Dan Register/
├── main.py          # Program utama, menampilkan menu & mengatur alur
├── database.py      # Koneksi ke SQLite3 & pembuatan tabel users
├── register.py      # Logic untuk registrasi akun baru
├── login.py         # Logic untuk validasi login
└── users.db         # File database (otomatis dibuat saat pertama kali dijalankan)
```

## Teknologi yang Dipakai

- **Python 3**
- **`sqlite3`** — modul bawaan Python untuk database ringan berbasis file (tidak perlu instalasi tambahan)

## Cara Kerja Singkat

**`database.py`** membuka koneksi ke `users.db` dan membuat tabel `users` (kalau belum ada) dengan struktur:

| Kolom | Tipe | Keterangan |
|---|---|---|
| `id` | INTEGER | Primary key, auto increment |
| `username` | TEXT | Nama akun |
| `password` | TEXT | Kata sandi (disimpan plain text — lihat catatan di bawah) |

**`register.py`** meminta input username & password, lalu menyimpannya ke tabel `users` lewat `INSERT`, dan mengunci perubahan dengan `conn.commit()`.

**`login.py`** meminta input username & password, mencocokkannya ke database lewat `SELECT ... WHERE username = ? AND password = ?`, lalu mengecek apakah datanya ditemukan (`cursor.fetchone()`).

**`main.py`** menampilkan menu berulang (`while True`) dan memanggil fungsi `registrasi_akun()` atau `login_akun()` sesuai pilihan user.

## ⚠️ Catatan Pembelajaran

Project ini dibuat murni untuk **latihan konsep dasar** sqlite3 dan alur login/register. Ada beberapa hal yang **belum** diterapkan dan sengaja disederhanakan dulu:

- **Password masih disimpan dalam bentuk plain text** (belum di-hash). Untuk project belajar ini tidak masalah, tapi **jangan dipakai untuk aplikasi nyata** tanpa hashing (misalnya pakai `hashlib`, atau lebih baik `bcrypt`/`passlib`) — kalau file `users.db` bocor, semua password user langsung kebaca.
- Belum ada validasi tambahan seperti: cek username kosong, cek username sudah terdaftar sebelumnya (duplikat), atau batas panjang password.
- Path database (`Login Dan Register/users.db`) bersifat relatif terhadap folder tempat program dijalankan.

## Rencana Pengembangan Selanjutnya

- Tambah hashing password (`hashlib` untuk belajar, `bcrypt` untuk versi lebih aman)
- Validasi username tidak boleh duplikat (`UNIQUE constraint`)
- Validasi input kosong
- Batasi percobaan login yang salah

## 📄 Lisensi

Project ini menggunakan lisensi **MIT License**.
