############################################
#   Created by : Aditya Putra Indrayanto   #
#   Program untuk menghitung IPK Mahasiswa #
############################################

jml_mhs = int(input("Input Jumlah Mahasiswa : "))
jml_nilai = int(input("Input Jumlah nilai tiap Mahasiswa : "))

data_nilai = {}
data_sks = {}
data_IPK = {}
data_SUM_SKS = {}
IPK_Akhir = {}

def main():
    for x in range(jml_mhs):
        data_nilai[x] = []
        data_sks[x] = []
        for y in range(jml_nilai):
            nilai = raw_input("Input nilai Ke-%d dari Mahasiswa %d : " % ((y+1), (x+1)))
            if nilai == 'A':
                bobot = 4
            elif nilai == 'B':
                bobot = 3
            elif nilai == 'C':
                bobot = 2
            elif nilai == 'D':
                bobot = 1
            else:
                bobot = 0
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
        print "================= Result ================="
        print "Total Jumlah Nilai Mahasiswa {} : {}".format(z+1, data_IPK[z])
        print "Total Jumlah SKS yang ditempuh Mahasiswa {} : {}".format(z+1, data_SUM_SKS[z])
        print "IPK Mahasiswa {} : {} ".format(z+1, round(IPK_Akhir[z], 2))

main()