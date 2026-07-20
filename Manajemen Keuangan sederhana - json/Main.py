import json
import os

NAMA_FILE = "Manajemen Keuangan App/data_keuangan.json"

transaksi = []

def muat_data():
    global transaksi
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r") as f:
            try:
                transaksi = json.load(f)
            except json.JSONDecodeError:
                transaksi = []

def simpan_data():
    with open(NAMA_FILE, "w") as f:
        json.dump(transaksi, f, indent=2)

def tambah_pemasukan(keterangan, jumlah):
    transaksi.append({"jenis": "Pemasukan", "keterangan": keterangan, "jumlah": jumlah})
    simpan_data()
    print(f"Pemasukan '{keterangan}' sebesar Rp{jumlah:,} berhasil ditambahkan.\n")

def tambah_pengeluaran(keterangan, jumlah):
    transaksi.append({"jenis": "Pengeluaran", "keterangan": keterangan, "jumlah": jumlah})
    simpan_data()
    print(f"Pengeluaran '{keterangan}' sebesar Rp{jumlah:,} berhasil ditambahkan.\n")

def hitung_saldo():
    saldo = 0
    for t in transaksi:
        if t["jenis"] == "Pemasukan":
            saldo += t["jumlah"]
        else:
            saldo -= t["jumlah"]
    return saldo

def tampilkan_riwayat():
    if not transaksi:
        print("Belum ada transaksi.\n")
        return
    
    print("\n")
    print("=" * 45)
    print("RIWAYAT TRANSAKSI")
    print("=" * 45)
    for i, t in enumerate(transaksi, start=1):
        tanda = "+" if t["jenis"] == "Pemasukan" else "-"
        print(f"{i}. [{t['jenis']}] {t['keterangan']} : {tanda}Rp{t['jumlah']:,}")
    print("=" * 45)
    print(f"SALDO SAAT INI: Rp{hitung_saldo():,}")
    print("=" * 45 + "\n")

def hapus_transaksi(nomor):
    if 1 <= nomor <= len(transaksi):
        data = transaksi.pop(nomor - 1)
        simpan_data()
        print(f"Transaksi '{data['keterangan']}' berhasil dihapus.\n")
    else:
        print("Nomor transaksi tidak ditemukan.\n")

def menu():
    print("=" * 45)
    print("APLIKASI MANAJEMEN KEUANGAN SEDERHANA")
    print("=" * 45)
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Riwayat & Saldo")
    print("4. Hapus Transaksi")
    print("5. Keluar")
    print("=" * 45)

muat_data()

while True:
    menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        keterangan = input("Keterangan pemasukan: ")
        jumlah = int(input("Jumlah pemasukan: "))
        tambah_pemasukan(keterangan, jumlah)

    elif pilihan == "2":
        keterangan = input("Keterangan pengeluaran: ")
        jumlah = int(input("Jumlah pengeluaran: "))
        tambah_pengeluaran(keterangan, jumlah)

    elif pilihan == "3":
        tampilkan_riwayat()

    elif pilihan == "4":
        tampilkan_riwayat()
        if transaksi:
            nomor = int(input("Masukkan nomor transaksi yang dihapus: "))
            hapus_transaksi(nomor)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan aplikasi ini!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.\n")