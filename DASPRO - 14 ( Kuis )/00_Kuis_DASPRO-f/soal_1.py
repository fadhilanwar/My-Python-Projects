'''
Nama : Fadhil Anwar Ahsani
'''

filename = "files/buku.txt"

def insertBuku():
    file = open(filename, "a")

    judul = str(input("Masukan Judul Buku: "))
    nama_penulis = str(input("Masukan Penulis Buku: "))
    kode_buku = str(input("Masukan Kode Buku: "))
    status = "tersedia"

    content = f"{judul},{nama_penulis},{kode_buku},{status}\n"


    file.write(content)

    file.close()


def viewBuku():
    file = open(filename, "r")
    bukus = file.read()
    # print(bukus)

    file.close()

def pinjamBuku(kode_buku):
    file = open(filename, "r")
    line = file.readlines()

    
    for row in line:
        data = row.strip().split(",")

        nama_buku = data[0]
        penulis_buku = data[1]
        id = data[2]
        status = "tidak_tersedia"

        # print(f"{kode_buku}, {id}")

        if kode_buku == id:
            with open('files/buku.txt', 'w') as file:
                for buku in file:
                    buku.write(f"{nama_buku},{penulis_buku},{kode_buku},{status}\n")
                    
            


choice = int(input('Masukan Ingin Melakukan aksi apa (1/2/3)\n1.Insert Buku\n2. Lihat Buku\n 3. Pinjam Buku\n Masukan Input= '))

if choice == 1:
    insertBuku()
elif choice == 2:
    viewBuku()
elif choice == 3:
    pinjamBuku()