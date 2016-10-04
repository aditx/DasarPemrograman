##Created by : Aditya Putra

data_nim = list()
data_matkul = list()

jml_mhs = input("Input Jumlah Mahasiswa : ")

for x in range(int(jml_mhs)):
    nim_mhs = input("Input Nim Mahasiswa Ke-%d : " % (x+1))
    data_nim.append(str(nim_mhs))
    jml_matkul = input("Input Jumlah Matkul yang diambil Mahasiswa Ke-%d: " % (x+1))
    for j in range(int(jml_matkul)):
        matkul_mhs = raw_input("Matkul Ke-%d : " % (j+1))
        data_matkul.append(str(matkul_mhs))


print data_nim
print data_matkul