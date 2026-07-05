saldo = 1000000

def tampilkan_menu():
    print("\n--- MENU ATM ---")
    print("1. Cek Saldo")
    print("2. Setor Tunai")
    print("3. Tarik Tunai")
    print("4. Keluar")

def cek_saldo():
    print(f"\nSaldo Anda saat ini: Rp{saldo: }")

def setor_tunai():
    global saldo
    nominal = float(input("Masukkan jumlah setoran: Rp"))
    if nominal > 0:
        saldo += nominal
        print(f"Berhasil setor tunai! Saldo baru: Rp{saldo: }")
    else:
        print("Nominal tidak valid.")

def tarik_tunai():
    global saldo
    nominal = float(input("Masukkan jumlah penarikan: Rp"))
    if nominal > saldo:
        print("Saldo tidak mencukupi!")
    elif nominal <= 0:
        print("Nominal tidak valid.")
    else:
        saldo -= nominal
        print(f"Penarikan berhasil. Sisa saldo: Rp{saldo: }")

def jalankan_atm():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            cek_saldo()
        elif pilihan == '2':
            setor_tunai()
        elif pilihan == '3':
            tarik_tunai()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan ATM kami.")
            break
        else:
            print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    jalankan_atm()