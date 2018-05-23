# Masukkan

keyone=int(input('Masukkan Key 1 : '))
keytwo=int(input('Masukkan Key 2 : '))
pesan=str(input('Masukkan pesan : '))

# Membuat string kosong

kosong=""
kosongdua=""

for i in pesan:
    baru=pesan[0:keyone]
    pesan=pesan[keyone::] #Potong jadi perbagian tiap 3 char
    barudua=baru[::-1] #Pembalik
    kosong+=barudua #3 syarat terpenuhi
    
for i in kosong:
    ordernya=ord(i)         # Mendapatkan order
    orderbaru=ordernya+keytwo
    if orderbaru>123:        # Ini jika angka kembali dari z
        sisa=orderbaru-122   # Dapat sisa dari pengurangan order
        orderbaru=96+sisa    # Dikembalikan ke a lagi
    hasil=chr(orderbaru)     # Dikembalikan ke character
    kosongdua+=hasil
print('Pesan hasil enkripsi: ', kosongdua)

# BONUS
'''

keyone=int(input('Masukkan Key 1 : '))
keytwo=int(input('Masukkan Key 2 : '))
pesan=str(input('Masukkan Pesan Rahasia: '))

# Membuat string kosong

kosong=""
kosongdua=""

# Kode dari Taku dan Mitsuha

for i in pesan:
    baru=pesan[:keyone]
    pesan=pesan[keyone::]
    barudua=baru[::-1]
    kosong+=barudua

# Caesar dechiper
        
for i in kosong:
    ordernya=ord(i)         # Mendapatkan order
    orderbaru=ordernya-keytwo
    if orderbaru<97:        # Ini jika angka kembali dari a
        sisa=97-orderbaru   # Dapat sisa dari pengurangan order
        orderbaru=123-sisa    # Dikembalikan ke z lagi
    hasil=chr(orderbaru)     # Dikembalikan ke character
    kosongdua+=hasil
print('Pesan asli: ', kosongdua)
    
'''
