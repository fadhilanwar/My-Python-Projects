'''
Nama    : Fadhil Anwar Ahsani
Kelas   : 1A - RPL
Nim     :2407136
'''

# Menghitung Selisih Waktu dari yang diinputkan

jam_awal = int(input("Masukan Jam Permulaan: "))
menit_awal = int(input("Masukan Menit Permulaan: "))
detik_awal = int(input("Masukan Detik Permulaan: "))

if jam_awal > 24 or menit_awal > 60 or detik_awal > 60:
    print("Salah satu format waktu yang anda masukkan, Tidak Valid!")
else:
    if menit_awal == 60 and detik_awal == 60:
        jam_awal = jam_awal + 1
        menit_awal = menit_awal + 1
        menit_awal = 0
        detik_awal = 0
    elif menit_awal == 60:
        jam_awal = jam_awal + 1
        menit_awal = 0
    elif detik_awal == 60:
        menit_awal = menit_awal + 1
        detik_awal = 0

    print(f"Noted!, Waktu awal anda adalah Jam: {jam_awal}, Menit: {menit_awal}, Detik: {detik_awal}")

    jam_akhir = int(input("Masukan Jam Tujuan: "))
    menit_akhir = int(input("Masukan Menit Tujuan: "))
    detik_akhir = int(input("Masukan Detik Tujuan: "))

    if jam_akhir > 24 or menit_akhir > 60 or detik_akhir > 60:
        print("Salah satu format waktu yang anda masukkan, Tidak Valid!")
    else:
        selisih_jam = 0
        selisih_menit = 0
        selisih_detik = 0
        if menit_akhir == 60 and detik_akhir == 60:
            jam_akhir = jam_akhir + 1
            menit_akhir = menit_akhir + 1
            menit_akhir = 0
            detik_akhir = 0
        elif menit_akhir == 60:
            jam_akhir = jam_akhir + 1
            menit_akhir = 0
        elif detik_akhir == 60:
            menit_akhir = menit_akhir + 1
            detik_akhir = 0

        
        selisih_jam = jam_akhir - jam_awal
        selisih_menit = menit_akhir - menit_awal
        selisih_detik = detik_akhir - detik_awal
        
        
        if jam_akhir > jam_awal:
            selisih_jam = jam_akhir - jam_awal
        if menit_akhir > menit_awal:
            selisih_menit = menit_akhir - menit_awal
        if detik_akhir > detik_awal:
            selisih_detik = detik_akhir - detik_awal
        if jam_awal > jam_akhir:
            selisih_jam = 24 - (jam_awal - jam_akhir)
        if menit_awal > menit_akhir:
            selisih_menit = menit_awal - menit_akhir
        if detik_awal > detik_akhir:
            selisih_detik = detik_awal - detik_akhir
        

        print(f"Selisih Waktu: {selisih_jam} Jam, {selisih_menit} Menit, {selisih_detik} Detik")
