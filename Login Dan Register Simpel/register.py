from database import cursor, conn

def registrasi_akun():
    print("=" * 50)
    print("REGISTRASI AKUN ANDA")
    print("=" * 50)
    username = input("Silahkan Buat Username Anda: ")
    password = input("Silahkan Buat Password Anda: ")

    print("\nSelamat Akun Anda Selesai Dibuat!")

    print("-" * 50)

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()