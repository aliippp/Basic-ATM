import random
import time
from customer import Customer

atm = Customer(id)

while(True):
    id = int(input("Masukan Pin Anda: "))
    trial = 0

    while(id != atm.cekPin() and trial < 3):
        id = int(input("Pin masih salah silahkan masukan lagi :"))
        trial += 1

        if trial == 3:
            print("Pin anda salah, silahkan coba lagi nanti")
            exit()
            
    print("Selamat datang di ATM")
    print("Silahkan pilih")
    print("1.Cek Saldo")
    print("2.Setor Tunai")
    print("3.Tarik Tunai")
    print("4.Bayar Pulsa")
    print("5.Keluar")
    selectMenu = int(input("Masukan Pilihan Anda :"))
    if selectMenu == 1:
        print("Saldo anda sekarang :", str(atm.cekSaldo()))

    elif selectMenu == 2:
        nominal = int(input("Masukan jumlah uang yang ingin anda setor :"))
        atm.setorUang(nominal)
        print("Saldo anda sekarang", str(atm.cekSaldo()))

    elif selectMenu == 3:
        nominal = int(input("Masukan nominal uang yang akan ditarik :"))
        atm.tarikUang(nominal)
        print("Saldo anda sekarang :", atm.cekSaldo())
    
    elif selectMenu == 4:
        nomor = int(input("Masukan nomor telefon tujuan :"))
        nominal = int(input("Masukan jumlah pulsa yang akan dimasukkan :"))
        atm.tarikUang(nominal)
        print("Pengisian pulsa ke nomor :", nomor, "sukses")
        print("Saldo anda sekarang :", atm.cekSaldo())

    elif selectMenu == 5:
        print("Terima Kasih telah menggunakan ATM")
        exit()
    
    else :
        print("Input anda tidak diterima.")
        exit()

    print("Apakah anda ingin melakukan transaksi lagi ?")
    print("1. Iya")
    print("2. tidak")
    selectAkhir = int(input("Masukan pilihan anda"))
    if selectAkhir == 2:
        print("Terima kasih")
        exit()