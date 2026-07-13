from register import registrasi_akun
from login import login_akun

while True:
    print("=" * 50)
    print("SELAMAT DATANG DI RYUUO STORE")
    print("=" * 50)

    print("1. LOGIN \n2. REGISTER \n3. KELUAR")
    pilihan = int(input("Silahkan Input 1/2/3 untuk Menjalankan Menu: "))

    print("-" * 50)

    if pilihan == 1:
        login_akun()
    elif pilihan == 2:
        registrasi_akun()
    elif pilihan == 3:
        break
    else:
        print("Input tidak valid")