my_file=input('File: ') # Menyerahkan input nama file

try:
    f=open(my_file,'r') # Membuka file
    semuakartu=f.read().split() # Mendefinisikan isi file dengan split agar terpisah antar spasi
    list(semuakartu) # Jadikan list agar mudah diindex dengan urutan

    # Print masing-masing kartu dalam file
    for i in semuakartu:
        print(i, end=' ')
    print('')


    # Ini merupakan urutan seharusnya tepok nyamuk sesuai soal yang diberikan
    urutan=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'AS']


    # Melakukan loop untuk tepok

    giliran=0 # Menyesuaikan giliran kartu dalam urutan
    hasil='Tepok: ' # Hasil awal berupa tepok, nanti akan ditambahkan dengan kartunya

    for kartu in semuakartu:
        if giliran==13: 
            giliran=0 # Mengembalikan giliran jika semua urutan telah diperiksa, balik ke 2 lagi
        if kartu=='JOKER' or kartu==urutan[giliran]: # Cek tepokkan
            hasil+='['+kartu+']' #Kalau tepok, kartu akan ditambahkan []
            print(hasil) 
            hasil='Tepok: ' # Mengembalikan hasil lagi ke bentuk awal
            giliran=0 # giliran kembali mulai dari 2 setelah ditepok
        else:
            hasil+=' '+kartu # Jika tidak sama, kartu ditambahkan tanpa[] dan tidak diprint, disimpan untuk nanti dipanggil saat tertepok
            giliran+=1 # Incarnate giliran agar bertambah sesuai kartu
    print('Permainan selesai.') #Print permainan selesai

    f.close() # Tutup file

except FileNotFoundError:
    print('Nama File tidak ditemukan.')
