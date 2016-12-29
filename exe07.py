##Created by : Aditya Putra

jml_mhs = int(input("Input Jumlah Mahasiswa : "))
jml_nilai = int(input("Input Jumlah nilai tiap Mahasiswa : "))

data_nilai = {}
data_sks = {}
data_IPK = {}
data_SUM_SKS = {}
IPK_Akhir = {}
sum_sks = {}

def main():
    for x in range(jml_mhs):
        data_nilai[x] = []
        data_sks[x] = []
        for y in range(jml_nilai):
            nilai = int(input("Input nilai Ke-%d dari Mahasiswa %d : " % ((y+1), (x+1))))
            data_nilai[x].append(nilai)
            sks = int(input("Input sks Ke-%d dari Nilai %d : " % ((y+1), (x+1))))
            data_sks[x].append(sks)

    # for nilai in data_nilai.keys():
    #     print 'Mahasiswa Ke-{}, Nilai : {}'.format(nilai+1, data_nilai[nilai])
    # for sks in data_sks.keys():
    #     print 'Mahasiswa Ke-{}, SKS Nilai ke-{} : {}'.format(sks+1, sks+1, data_sks[sks])

    for z in range(jml_mhs):
        data_IPK[z] = []
        data_SUM_SKS[z] = []
        IPK_Akhir[z] = []
        temp_data_ipk = 0
        temp_sum_sks = 0
        for i in range(len(data_nilai[z])):
            #print data_nilai[z][i]
            temp_data_ipk += (data_nilai[z][i] * data_sks[z][i])
            temp_sum_sks += (data_sks[z][i])
        data_IPK[z].append(temp_data_ipk)
        data_SUM_SKS[z].append(temp_sum_sks)
        IPK_Akhir[z] = (float(data_IPK[z][0]) / float(data_SUM_SKS[z][0]))
        print "Total Jumlah Nilai : {}".format(data_IPK[z])
        print "Total Jumlah SKS : {}".format(data_SUM_SKS[z])
        print "IPK : {} ".format(IPK_Akhir[z])

main()