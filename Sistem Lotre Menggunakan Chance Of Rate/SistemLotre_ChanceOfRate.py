print("====LOTRE LIBURAN KEJOGJA====")

import random

rate = [80, 15, 4, 1]
prize_pool = ["zoonk", "teh sariwangi 1 renceng", "kopi 1 renceng", "pulsa Rp100.000", "LIBURAN JOGJA"]

while True:
    pilihan = input("Silahkan ketik [play] untuk bermain atau ketik [exit] untuk keluar: ")
    if pilihan == "play":
        token = int(input("\nSilahkan input jumlah token: "))
        print("- Token anda saat ini adalah = ", token)
    
        while token > 0:
            spin = int(input("\nsillahkan input [1] untuk spin 1x atau input [10] untuk spin 10x: "))
        
            if spin == 1 and token >= 1:
                roll = random.randint(1, 100)
                token = token-1
        
                if roll <= rate[0]:
                    print(
                    "- Sisa token anda = ", token,
                    "\n- Selamat anda mendapatkan = ", prize_pool[0]
                    )
                elif roll <= rate[0] + rate[1]:
                    print(
                    "- Jumlah token anda = ", token,
                    "\n- Selamat anda mendapatkan = ", prize_pool[1], " dan ", prize_pool[2],
                    )
                elif roll<= rate[2] + rate[3]:
                    print(
                    "- Jumlah token anda = ", token,
                    "\n- Selamat anda mendapatkan = ", prize_pool[3],
                    )
                else:
                    print(
                    "- Jumlah token anda = ", token,
                    "\n- Selamat anda mendapatkan = ", prize_pool[4],
                    )
            
            elif spin == 10 and token >= 10:
                
                for spin in range(0, 10):
                    roll = random.randint(1,100)
                    token = token - 1

                    if roll <= rate[0]:
                        print(
                        "- Sisa token anda = ", token,
                        "\n- Selamat anda mendapatkan = ", prize_pool[0]
                        )
                    elif roll <= rate[0] + rate[1]:
                        print(
                        "- Jumlah token anda = ", token,
                        "\n- Selamat anda mendapatkan = ", prize_pool[1], " dan ", prize_pool[2],
                        )
                    elif roll<= rate[2] + rate[3]:
                        print(
                        "- Jumlah token anda = ", token,
                        "\n- Selamat anda mendapatkan = ", prize_pool[3],
                        )
                    else:
                        print(
                        "- Jumlah token anda = ", token,
                        "\n- Selamat anda mendapatkan = ", prize_pool[4],
                        )
            else:
                print("Input tidak valid atau jumlah token kurang untuk spin")

    elif pilihan == "exit":
        break
