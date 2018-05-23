file_input=input("Masukkan nama file: ")

try:
    my_file=open(file_input,"r")
    file_hasil=open("out.out","w")
    ListFile=list(my_file.read().split())

    def FungsiA(a,b):
        return (a*a)+(b*b)
    def FungsiB(a,b):
        return ((FungsiA(a,b))**(1/2))+(a/b)
    def FungsiC(a,b):
        return (FungsiB(a,b)/2)
    def FungsiD(a,b):
        return ((FungsiA(a,b)+FungsiC(a,b))/a)/((FungsiA(a,b)+FungsiC(a,b)/b))

    counter=0
    
    while 0<counter<33:
        if ListFile[counter]=="FUNGSI-A":
            a=int(ListFile[counter+1])
            b=int(ListFile[counter+2])
            hasil=FungsiA(a,b)
            print("HASIL FUNGSI-A ("+str(a)+","+str(b)+")"+"= "+str(hasil), file=file_hasil)
        elif ListFile[counter]=="FUNGSI-B":
            a=int(ListFile[counter+1])
            b=int(ListFile[counter+2])
            hasil=FungsiB(a,b)
            print("HASIL FUNGSI-B ("+str(a)+","+str(b)+")"+"= "+str(hasil), file=file_hasil)
        elif ListFile[counter]=="FUNGSI-C":
            a=int(ListFile[counter+1])
            b=int(ListFile[counter+2])
            hasil=FungsiC(a,b)
            print("HASIL FUNGSI-C ("+str(a)+","+str(b)+")"+"= "+str(hasil), file=file_hasil)
        elif ListFile[counter]=="FUNGSI-D":
            a=int(ListFile[counter+1])
            b=int(ListFile[counter+2])
            hasil=FungsiD(a,b)
            print("HASIL FUNGSI-D ("+str(a)+","+str(b)+")"+"= "+str(hasil), file=file_hasil)
        counter+=3
        
except FileNotFoundError:
    print("File Tidak Ditemukan")

except TypeError:
    print("Terjadi kesalahan tipe data")

my_file.close()
file_hasil.close()
        
        
