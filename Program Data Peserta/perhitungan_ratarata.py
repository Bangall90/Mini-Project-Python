from data_peserta import daftar_peserta

def rata_rata_umur():
    peserta = daftar_peserta()
    total = sum(i["Umur"] for i in peserta)
    jumlah = len(peserta)

    return round(total / jumlah)

def Jumlah_Jenis_kelamin():
    laki_laki = 0
    perempuan = 0

    for p in daftar_peserta():
        if p["Jenis Kelamin"] == "Laki Laki":
            laki_laki += 1
        elif p["Jenis Kelamin"] == "Perempuan":
            perempuan += 1
    
    return laki_laki, perempuan