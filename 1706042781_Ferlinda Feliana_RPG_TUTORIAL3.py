#Untuk input

kodementah=str(input("Masukkan kode mentah: "))
namalokasi=str(input("Masukkan nama lokasi: "))
binernya=input("Masukkan biner: ")

#Melakukan assignment untuk password

if 1<=len(kodementah)<=5:
    if namalokasi=="dapur" or namalokasi=="matahari" or namalokasi=="taman" or namalokasi=="bukit" or namalokasi=="mikrofon":
        password="Anja5"
    else:
        print("wrong location!")

elif 6<=len(kodementah)<=10:
    if namalokasi=="bukit":
        password="y3KAI1"
    elif namalokasi=="matahari":
        password="AkUK4mU"
    elif namalokasi=="dapur" or namalokasi=="mikrofon" or namalokasi=="taman":
        password="c4p3DEh"
    else:
        print("wrong location!")
        break
elif 11<=len(kodementah)<=15:
    if namalokasi=="mikrofon":
        password="g46Un4"
    elif namalokasi=="dapur" or namalokasi=="matahari" or namalokasi=="taman" or namalokasi=="bukit":
        password="54nsAE"
    else:
        print("wrong location!")
        break
elif 16<=len(kodementah)<=20:
    if namalokasi=="taman":
        password="k3PO"
    elif namalokasi=="dapur" or namalokasi=="matahari" or namalokasi=="mikrofon" or namalokasi=="bukit":
        password="s3LOW"
    else:
        print("Wrong location!")
        break
elif 20<=len(kodementah)<=100:
    if namalokasi=="dapur":
        password="s04L1niEZ"
    elif namalokasi=="taman" or namalokasi=="matahari" or namalokasi=="mikrofon" or namalokasi=="bukit":
        password="C4b5kUy"
    else:
        print("Wrong location!")
        break
else:
    password="x00000x"

#Konversi biner ke desimal

n=len(binernya)
konversi=0
for i in range(1,n+1):
    konversi=konversi+int(binernya[i-1])*2**(n-1)

#Hasil dari input yang diberikan

print("========== Dipsi LIVE Hack =========")
print("============ SANDI DATA ============")    
print("Kode awal sandi: ", password)
print("Hasil konversi desimal: "+ str(konversi))
print("Hasil akhir: ///"+password+"///"+str(konversi)+"///")
print("====================================")
print("Sandi berhasil diterjemahkan !")
print("Pencuri akan segera ditangkap !")
print("====================================")

