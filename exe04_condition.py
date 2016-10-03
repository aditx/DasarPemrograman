# Created by : API

# Start
s_nilai = input("Masukkan Nilai Mahasiswa : ")
s_hasil = ''

if s_nilai >= 81 and s_nilai <= 100:
    s_hasil = 'A : SANGAT BAIK'
elif 71 <= s_nilai <= 80:
    s_hasil = 'B : BAIK'
elif 61 <= s_nilai <= 70:
    s_hasil = 'C : CUKUP'
elif 51 <= s_nilai <= 60:
    s_hasil = 'D : KURANG'
elif 0 <= s_nilai <= 50:
    s_hasil = 'E : GAGAL'
else: print 'Inputan salah'

print s_hasil
