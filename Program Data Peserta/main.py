from data_peserta import daftar_peserta
from perhitungan_ratarata import rata_rata_umur
from perhitungan_ratarata import Jumlah_Jenis_kelamin

nomer_peserta = 1

for peserta in daftar_peserta():
    print("=" * 50)
    print("PESERTA", nomer_peserta)
    print("=" * 50)

    print(f"Nama Peserta\t: {peserta["Nama"]}")
    print(f"Umur Peserta\t: {peserta["Umur"]}")
    print(f"Kelamin Peserta\t: {peserta["Jenis Kelamin"]}")
    print("-" * 50, "\n")

    nomer_peserta += 1

print(f"Rata Rata Umur Peserta: {rata_rata_umur()}")

laki_laki, perempuan = Jumlah_Jenis_kelamin()
print(f"Jumlah Laki Laki : {laki_laki} dan Perempuan : {perempuan}")