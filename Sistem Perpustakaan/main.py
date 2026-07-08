import csv
import os

if not os.path.exists("Sistem Perpustakaan/peminjam.csv"):
    with open("Sistem Perpustakaan/peminjam.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id_buku", "nama_peminjam"])

if not os.path.exists("Sistem Perpustakaan/books.csv"):
    with open("Sistem Perpustakaan/books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "judul", "penulis", "kategori", "stok"])

def tambah_buku():
    id_buku = int(input("ID Buku: "))
    judul = input("Judul: ")
    penulis = input("Penulis: ")
    kategori = input("Kategori: ")
    stok = int(input("Stok: "))

    with open("Sistem Perpustakaan/books.csv", "a", newline="", encoding="utf-8") as file:
        tambah_data = csv.writer(file)
        tambah_data.writerow([id_buku, judul, penulis, kategori, stok])

    print("\nData berhasil ditambahkan.")

def lihat_buku():
    with open("Sistem Perpustakaan/books.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print("=" * 50)
        print("DAFTAR BUKU")
        print("=" * 50)

        for buku in reader:
            print(f"ID       : {buku['id']}")
            print(f"Judul    : {buku['judul']}")
            print(f"Penulis  : {buku['penulis']}")
            print(f"Kategori : {buku['kategori']}")
            print(f"Stok     : {buku['stok']}")
            print("-" * 50)

def edit_buku():
    id_cari = input("Masukkan id buku yang ingin di edit: ")

    data_buku = []

    with open("Sistem Perpustakaan/books.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for buku in reader:
            if buku["id"] == id_cari:
                print("Data ditemukan!\n")

                buku["judul"] = input("Judul baru    : ")
                buku["penulis"] = input("Penulis baru  : ")
                buku["kategori"] = input("Kategori baru : ")
                buku["stok"] = int(input("Stok baru     : "))

            data_buku.append(buku)

    with open("Sistem Perpustakaan/books.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "judul", "penulis", "kategori", "stok"]

        edit_data = csv.DictWriter(file, fieldnames=fieldnames)

        edit_data.writeheader()
        edit_data.writerows(data_buku)

    print("Data berhasil diubah.")

def hapus_buku():
    id_hapus = input("Masukkan id buku yang ingin dihapus: ")

    data_buku = []
    ditemukan = False

    with open("Sistem Perpustakaan/books.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for buku in reader:

            if buku["id"] == id_hapus:
                ditemukan = True
            else:
                data_buku.append(buku)

    with open("Sistem Perpustakaan/books.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "judul", "penulis", "kategori", "stok"]

        hapus_data = csv.DictWriter(file, fieldnames=fieldnames)

        hapus_data.writeheader()
        hapus_data.writerows(data_buku)

    if ditemukan:
        print("\nData berhasil dihapus.")
    else:
        print("\nID buku tidak ditemukan.")
        
def cari_buku():
    keyword = input("Masukkan id atau Judul Buku: ").lower()

    ditemukan = False

    with open("Sistem Perpustakaan/books.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for buku in reader:

            if (keyword == buku["id"].lower() or
                keyword in buku["judul"].lower()):

                ditemukan = True

                print("\n===== DATA BUKU =====")
                print(f"ID       : {buku['id']}")
                print(f"Judul    : {buku['judul']}")
                print(f"Penulis  : {buku['penulis']}")
                print(f"Kategori : {buku['kategori']}")
                print(f"Stok     : {buku['stok']}")
                print("-" * 30)

    if not ditemukan:
        print("Buku tidak ditemukan.")

def pinjam_buku():
    id_pinjam = input("Masukkan ID Buku: ")
    nama = input("Nama Peminjam: ")

    data_buku = []
    ditemukan = False

    with open("Sistem Perpustakaan/books.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for buku in reader:

            if buku["id"] == id_pinjam:
                ditemukan = True

                if int(buku["stok"]) > 0:

                    buku["stok"] = str(int(buku["stok"]) - 1)

                    with open("Sistem Perpustakaan/peminjam.csv", "a", newline="", encoding="utf-8") as file2:
                        tambah_peminjam = csv.writer(file2)
                        tambah_peminjam.writerow([id_pinjam, nama])

                    print("Buku berhasil dipinjam.")

                else:
                    print("Stok habis.")

            data_buku.append(buku)

    with open("Sistem Perpustakaan/books.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["id","judul","penulis","kategori","stok"]

        pinjam_data = csv.DictWriter(file, fieldnames=fieldnames)
        pinjam_data.writeheader()
        pinjam_data.writerows(data_buku)

    if not ditemukan:
        print("ID Buku tidak ditemukan.")

def data_peminjam():

    with open("Sistem Perpustakaan/peminjam.csv","r",newline="",encoding="utf-8") as file:

        reader = csv.DictReader(file)

        print("\n===== DATA PEMINJAM =====")

        for data in reader:

            print(f"ID Buku : {data['id_buku']}")
            print(f"Nama    : {data['nama_peminjam']}")
            print("-"*30)

def kembalikan_buku():

    id_kembali = input("Masukkan ID Buku: ")
    nama = input("Nama Peminjam: ")

    data_buku = []
    data_peminjam = []

    with open("Sistem Perpustakaan/books.csv","r",newline="",encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for buku in reader:

            if buku["id"] == id_kembali:
                buku["stok"] = str(int(buku["stok"]) + 1)

            data_buku.append(buku)

    with open("Sistem Perpustakaan/peminjam.csv","r",newline="",encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for data in reader:

            if not (data["id_buku"] == id_kembali and data["nama_peminjam"] == nama):
                data_peminjam.append(data)

    with open("Sistem Perpustakaan/books.csv","w",newline="",encoding="utf-8") as file:

        fieldnames=["id","judul","penulis","kategori","stok"]

        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_buku)

    with open("Sistem Perpustakaan/peminjam.csv","w",newline="",encoding="utf-8") as file:

        fieldnames=["id_buku","nama_peminjam"]

        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_peminjam)

    print("Buku berhasil dikembalikan.")

while True:
    print("\n====Menu Perpustkaan====")
    print(" 1. Tambah Buku" \
    " \n 2. Lihat Buku" \
    " \n 3. Edit Buku" \
    " \n 4. Hapus Buku" \
    " \n 5. Cari Buku" \
    " \n 6. Pinjam Buku" \
    " \n 7. Data Peminjam" \
    " \n 8. Kembalikan Buku" \
    " \n 9. keluar"
    )

    pilihan = int(input("Silahkan Pilih Menu 1/2/3/4/5/6/7/8/9: "))

    if pilihan == 1:
        tambah_buku()
    elif pilihan == 2:
        lihat_buku()
    elif pilihan == 3:
        edit_buku()
    elif pilihan == 4:
        hapus_buku()
    elif pilihan == 5:
        cari_buku()
    elif pilihan == 6:
        pinjam_buku()
    elif pilihan == 7:
        data_peminjam()
    elif pilihan == 8:
        kembalikan_buku()
    elif pilihan == 9:
        break
    else:
        print("Input anda tidak valid silahkan input ulang")