barang = []
stock = []

while True:
    print("\n--Sistem Gudang Sederhana-- \n1. Tambah Barang \n2. Lihat Barang \n3. Keluar")
    pilihan = int(input("Silahkan Input 1/2/3 : "))

    if pilihan == 1:
        Barang_Masuk = input("Silahkan Masukkan Nama Barang : ")
        Stock_Masuk = int(input("Silahkan Masukkan Jumlah Stock : "))

        barang.append(Barang_Masuk)
        stock.append(Stock_Masuk)

    elif pilihan == 2:
        print(f"\nBarang Yang Tersimpan Digudang : {barang} \nJumlah Stock Yang Tersedia : {stock}")

    elif pilihan == 3:
        break

    else:
        print("Input anda tidak valid")