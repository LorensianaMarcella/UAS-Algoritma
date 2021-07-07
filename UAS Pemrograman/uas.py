import os
import sys
def pindah (label) :
    global nomor 
    nomor = label
        
def clearscreen():
    os.system('cls')

def keluar():
    sys.exit()
        
def ulang():
    ulang = input("Apakah anda ingin mengulang lagi? [y/n] ")
    if ulang == "y" or ulang == "Y" :
        pindah(0)
        clearscreen()
    elif ulang == "n" or ulang == "N" :
        clearscreen()
        keluar()
        
    else :
        keluar()
        
def rumus() :
    global gaji_pokok, tunjangan_istri, tunjangan_anak, gaji_bruto, biaya_jabatan, iuran_pensiun, iuran_organisasi, gaji_netto  
    gaji_bruto = gaji_pokok + tunjangan_anak + tunjangan_istri
    if tunjangan_anak > 3 :
        tunjangan_anak = jumnak * anak
        
    gaji_netto = gaji_bruto - iuran_pensiun - iuran_organisasi
    biaya_jabatan = 0.05
    total = gaji_bruto - biaya_jabatan - iuran_pensiun - iuran_organisasi
        
def cetak() :
    print("=============================")
    print("         Slip Gaji           ")
    print("         Tanggal:            ")
    print("=============================")
    print("Nama : ", nama)
    print("Golongan : ", golongan)
    print("Jenis Kelamin : " , jenis_kelamin)
    print("Status Kawin : " , status_kawin  )   
    print("Gaji Pokok : " , gaji_pokok)
    print("Tunjangan Istri " , tunjangan_istri)
    print("Tunjangan Anak" , tunjangan_anak)
    print(">> Gaji Bruto" , gaji_bruto)
    print("-------------------------------")
    print("Biaya Jabatan" , biaya_jabatan)
    print("Iuran Pensiun" , iuran_pensiun)
    print("Iuran Organisasi" , iuaran_organisasi)
    print(">>Gaji Netto" ,  gaji_neto)
    print("")
            
nomor = 0

while True :
    if nomor == 0 :
        clearscreen()
        print ("==============================")
        print ("           Slip Gaji          ")
        print ("           Tanggal            ")
        print ("")
        nama = input("Masukan nama : ")
        golongan = input("Masukan golongan : ")
        jenis_kelamin = input("Masukan jenis kelamin : ")
        status_kawin = input("masukan status kawin : ")
        gaji_pokok = int(input("masukan gaji pokok : "))
        tunjangan_istri =int(input("Masukan tunjangan istri : "))
        tunjangan_anak = int(input("Masukan tunjangan anak : "))
        gaji_bruto = int(input("Masukan >> gaji bruto : "))
        print ("-------------------------------")
        print ("")
        biaya_jabatan = int(input("Masukan biaya jabatan : "))
        iuran_pensiun = int(input("Masukan iuran pensiun : "))
        iuran_organisasi = int(input("Masukan iuran organisasi : "))
        gaji_netto = int(input("Masukan >>gaji netto : "))
        if golongan == 1 :
            pindah(1)
        elif golongan == 2 :
            pindah(2)
        elif golongan == 3 :
            pindah(3)
        else : 
            pindah(0)
            
    elif nomor == 1 :
        gaji_pokok = 2500000
        tunjangan_istri = 0.01
        tunjangan_anak = 0.02
        clearscreen()
        rumus()
        cetak()
        ulang()
        
    elif nomor == 2 :
        gaji_pokok = 4500000
        tunjangan_istri = 0.03
        tunjangan_anak = 0.02
        clearscreen()
        rumus()
        cetak()
        ulang()
        
    elif nomor == 3 :
        gaji_pokok = 6500000
        tunjangan_istri = 0.05
        tunjangan_anak = 0.02
        clearscreen()
        rumus()
        cetak()
        ulang()
            
    else :
        keluar()