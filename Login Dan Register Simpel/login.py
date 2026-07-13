from database import cursor

def login_akun():
    print("=" * 50)
    print("LOGIN AKUN ANDA")
    print("=" * 50)
    username = input("Silahkan Masukkan Username Anda: ")
    password = input("Silahkan Masukkan Password Anda: ")

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    users = cursor.fetchone()

    if users:
        print("\nLogin anda berhasil!")
    else:
        print("\nLogin anda gagal, silahkan coba lagi!")

    print("-" * 50)