nama=str(input("Nama:"))
a=float(input('Tingkat kejujuran '+nama+':'))
b=float(input('Tingkat kecerdasan '+nama+':'))
c=float(input('Tingkat Kemapanan '+nama+':'))
d=float(input('Tingkat Keberuntungan '+nama+':'))
P=(3*a)+(3*b)+(2.5*c)+(1.5*d)
Q=0.125*((a+b+c+d)**2)/2
print("Nilai P "+nama+" adalah ", round(P,2))
print("Nilai Q "+nama+" adalah ",round(Q,2))
if 1<=a<=10 and 1<=b<=10 and 1<=c<=10 and 1<=d<=10:
    if 85<=P<=95 and Q>=45:
        print(nama+" lolos standar calon suami Loly dan Lily")
    elif Q>=45:
        print(nama+" lolos standar calon suami Lily")
    else:
        print(nama+" tidak lolos standar siapapun :(")
else:
    print("Anda memasukkan nilai yang salah. Range adalah 1-10. Coba lagi")
