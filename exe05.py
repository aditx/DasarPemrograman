#Soal Nomor 3

#Start
bil_1 = input("Masukkan bilangan 1 = ")
bil_2 = input("Masukkan bilangan 2 = ")
bil_3 = input("Masukkan bilangan 3 = ")

min = bil_1
max = bil_1

if (min > bil_2):
    min = bil_2
if (min > bil_3):
    min = bil_3
if (max < bil_2):
    max = bil_2
if (max < bil_3):
    max = bil_3

sum = bil_1 + bil_2 + bil_3
avg = sum / 3

print "Min : ", min
print "Max : ", max
print "Avg : ", avg