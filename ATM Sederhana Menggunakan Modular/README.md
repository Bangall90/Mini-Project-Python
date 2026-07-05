# 💳 Simulasi ATM Sederhana dengan Python

Proyek ini merupakan program simulasi ATM berbasis Command Line Interface (CLI) yang dikembangkan menggunakan bahasa pemrograman Python. Program ini dirancang untuk mensimulasikan proses transaksi perbankan sederhana melalui terminal, sehingga cocok digunakan sebagai media pembelajaran dasar mengenai logika pemrograman.

Pengguna dapat melakukan beberapa transaksi seperti mengecek saldo, menyetor uang, dan menarik uang melalui menu interaktif. Setiap transaksi akan langsung memperbarui saldo dan dilengkapi dengan validasi agar proses berjalan sesuai aturan yang telah ditentukan.

## ✨ Fitur

- Cek saldo rekening.
- Setor tunai.
- Tarik tunai.
- Pembaruan saldo secara otomatis setelah transaksi.
- Validasi nominal transaksi.
- Mencegah penarikan melebihi saldo.
- Menu interaktif berbasis Command Line Interface (CLI).

## ⚙️ Logika Program

- Program dimulai dengan menetapkan saldo awal sebesar Rp1.000.000.
- Menu utama akan ditampilkan secara berulang menggunakan perulangan while.
- Pengguna memilih salah satu menu yang tersedia.
- Program menjalankan fungsi sesuai pilihan pengguna.
- Setiap transaksi akan memvalidasi nominal yang dimasukkan:
  Nominal harus lebih dari nol.
  Penarikan tidak boleh melebihi saldo yang tersedia.
- Setelah transaksi selesai, saldo akan diperbarui secara otomatis.
- Program akan berhenti ketika pengguna memilih menu Keluar.

##  📚 Algoritma Program

- Inisialisasi saldo awal.
- Tampilkan menu ATM.
- Minta pengguna memilih menu.
- Jika memilih Cek Saldo, tampilkan saldo saat ini.
- Jika memilih Setor Tunai, masukkan nominal lalu tambahkan ke saldo apabila valid.
- Jika memilih Tarik Tunai, masukkan nominal lalu kurangi saldo apabila saldo mencukupi.
- Jika memilih Keluar, akhiri program.
- Jika pilihan tidak tersedia, tampilkan pesan kesalahan dan kembali ke menu utama.

## 🎯 Tujuan Proyek

Proyek ini dibuat sebagai latihan dasar pemrograman Python untuk memahami implementasi fungsi, logika percabangan, perulangan, validasi input, penggunaan variabel global, serta penerapan algoritma sederhana dalam membangun simulasi sistem ATM berbasis terminal.
