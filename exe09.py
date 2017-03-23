############################################
#   Created by : Aditya Putra Indrayanto   #
#        Menyimpan data pada Array         #
############################################

import collections

data_buku = {}
buku = collections.namedtuple('buku', ['judul', 'halaman', 'harga'])

def main():
    jml_buku = int(input("Input Jumlah Buku yang ingin disimpan : "))

    for x in range(jml_buku):
        buku.judul = raw_input("Input judul buku ke-%d : " % (x+1))
        buku.halaman = int(input("Input halaman buku ke-%d : " % (x+1)))
        buku.harga = int(input("Input harga buku ke-%d : " % (x+1)))
        data_buku[x] = buku

        print data_buku[x].judul, data_buku[x].halaman, data_buku[x].harga

main()
