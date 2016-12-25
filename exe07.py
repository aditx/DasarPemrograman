##Created by : Aditya Putra

jml_mhs = int(input("Input Jumlah Mahasiswa : "))
jml_nilai = int(input("Input Jumlah nilai tiap Mahasiswa : "))

data_nilai = {}
data_sks = {}
data_IPK = {}

def main():
    for x in range(jml_mhs):
        data_nilai[x] = []
        data_sks[x] = []
        for y in range(jml_nilai):
            nilai = int(input("Input nilai Ke-%d dari Mahasiswa %d : " % ((y+1), (x+1))))
            data_nilai[x].append(nilai)
            sks = int(input("Input sks Ke-%d dari Nilai %d : " % ((y+1), (x+1))))
            data_sks[x].append(sks)

    for nilai in data_nilai.keys():
        print 'Mahasiswa Ke-{}, Nilai : {}'.format(nilai+1, data_nilai[nilai])
    for sks in data_sks.keys():
        print 'Mahasiswa Ke-{}, SKS Nilai ke-{} : {}'.format(sks+1, sks+1, data_sks[sks])

    #for z in range(jml_mhs):
        #for i in range(jml_nilai):

    i_data_nilai = 0
    i_data_sks = 0
    if jml_nilai <= 1:
        temp_nilai = 2
    else:
        temp_nilai = jml_nilai

    for i in range(temp_nilai-1):
        print i
        for ext_data_nilai in data_nilai[i]:
            i_data_nilai += ext_data_nilai
            print ext_data_nilai
    #for ext_data_sks in data_sks[0]:
        #i_data_sks += ext_data_sks
        #print ext_data_sks

main()