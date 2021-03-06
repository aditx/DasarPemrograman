############################################
#   Created by : Aditya Putra Indrayanto   #
#   Program untuk menghitung IPK Mahasiswa #
############################################

data_nilai = {}
data_sks = {}
data_IPK = {}
data_SUM_SKS = {}
IPK_Akhir = {}

def main():
    print "========================================="
    print "====     Masukkan nilai mahasiswa    ===="
    print "====   Berupa huruf (A,B,C,D atau E) ===="
    print "====  Dan jumlah SKS dari tiap matkul ==="
    print "========================================="
    print "\n"
    jml_mhs = int(input("Input Jumlah Mahasiswa : "))
    jml_nilai = int(input("Input Jumlah nilai tiap Mahasiswa : "))
    hitung_ipk(jml_mhs, jml_nilai)

def hitung_ipk(jml_mhs, jml_nilai):
    data_rata_ipk = 0
    for x in range(jml_mhs):
        data_nilai[x] = []
        data_sks[x] = []
        for y in range(jml_nilai):
            nilai = raw_input("Input nilai Ke-%d dari Mahasiswa %d : " % ((y+1), (x+1)))
            if nilai == 'A' or nilai == 'a':
                bobot = 4
            elif nilai == 'B' or nilai == 'b':
                bobot = 3
            elif nilai == 'C' or nilai == 'c':
                bobot = 2
            elif nilai == 'D' or nilai == 'd':
                bobot = 1
            elif nilai == 'E' or nilai == 'e':
                bobot = 0
            else:
                print "Maaf inputan nilai anda salah !! Mohon ulangi lagi"
                exit()
            data_nilai[x].append(bobot)
            sks = int(input("Input sks Ke-%d dari Nilai %d : " % ((y+1), (x+1))))
            data_sks[x].append(sks)

    for z in range(jml_mhs):
        data_IPK[z] = []
        data_SUM_SKS[z] = []
        IPK_Akhir[z] = []
        temp_data_ipk = 0
        temp_sum_sks = 0
        for i in range(len(data_nilai[z])):
            temp_data_ipk += (data_nilai[z][i] * data_sks[z][i])
            temp_sum_sks += (data_sks[z][i])
        data_IPK[z].append(temp_data_ipk)
        data_SUM_SKS[z].append(temp_sum_sks)
        IPK_Akhir[z] = (float(data_IPK[z][0]) / float(data_SUM_SKS[z][0]))
        data_rata_ipk += IPK_Akhir[z]
        print "================= Result IPK Mahasiswa {} =================".format(z+1)
        print "Total Jumlah Nilai yang didapat Mahasiswa {} : {}".format(z+1, data_IPK[z])
        print "Total Jumlah SKS yang ditempuh Mahasiswa {} : {}".format(z+1, data_SUM_SKS[z])
        print "IPK Mahasiswa {} : {} ".format(z+1, round(IPK_Akhir[z], 2))

    total_rata_ipk = data_rata_ipk/jml_mhs
    print "\n"
    print "================= SUMMARY ================="
    print "Jumlah Total Mahasiswa adalah : {}".format(jml_mhs)
    print "Rata-rata IPK semua Mahasiswa adalah : {}".format(round(total_rata_ipk, 2))

main()