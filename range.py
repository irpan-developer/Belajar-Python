print ("PROGRAM PYTHON MENGHITUNG NILAI TERKECIL & TERBESAR SERTA NILAI RATA-RATA")
n = int(input("\nMasukan Jumlah Bilangan = "))
bil = []
tot = 0
for x in range(n):
    m=n-x
    a = int(input("Bilangan ke %d = "%m))
    bil.append(a)
    tot += bil[x]
    rata2 = tot / n

print("\nBilangan Terkecil : %d" %min(bil))
print("Bilangan Terbesar : %d" %max(bil))
print("Nilai Rata-rata   : %0.2f" %rata2)
