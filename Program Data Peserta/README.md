# Program Data Peserta
 
Program sederhana berbasis Python untuk mengelola dan menghitung statistik dasar dari data peserta (nama, umur, dan jenis kelamin).

## Fitur
 
- Menampilkan daftar peserta beserta detailnya (nama, umur, jenis kelamin)
- Menghitung rata-rata umur peserta
- Menghitung jumlah peserta berdasarkan jenis kelamin (Laki-Laki / Perempuan)

## Penjelasan Singkat Kode
 
### `data_peserta.py`
Menyimpan data peserta dalam bentuk **list of dictionary**, di mana setiap peserta direpresentasikan sebagai satu dictionary dengan key `Nama`, `Umur`, dan `Jenis Kelamin`.

```python
def daftar_peserta():
    return [
        {"Nama": "Ali", "Umur": 21, "Jenis Kelamin": "Laki Laki"},
        ...
    ]
```

### `perhitungan_ratarata.py`
Berisi dua fungsi untuk mengolah data dari `daftar_peserta()`:
 
- `rata_rata_umur()` → menghitung rata-rata umur seluruh peserta
- `rata_rata_Jenis_kelamin()` → menghitung jumlah peserta laki-laki dan perempuan


### `main.py`
File utama yang meng-import fungsi dari kedua file di atas, lalu:
1. Menampilkan detail setiap peserta menggunakan perulangan `for`
2. Menampilkan hasil rata-rata umur
3. Menampilkan jumlah peserta berdasarkan jenis kelamin

## 📄 Lisensi

Project ini menggunakan lisensi **MIT License**.
