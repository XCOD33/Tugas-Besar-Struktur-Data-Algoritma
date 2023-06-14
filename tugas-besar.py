from BST import BSTNode
from transaksi import Transaksi
import pandas as pd

bst = BSTNode()

transaksi = Transaksi({
    "nama_konsumen": "",
    "no_sku": 0000,
    "jumlah_beli": 0,
    "subtotal": 0
})

answer = True
dataTransaksi = []

while answer:
    print("Selamat Datang di Aplikasi Kelola Barang\n1) Kelola Stok Barang\n2) Kelola Transaksi Konsumen\n0) Keluar\n")

    input_menu = input("Masukkan Menu : ")

    if (input_menu == "1"):
        
        sub_answer_1 = True
        
        while sub_answer_1:
            print("\nKelola Stok Barang\n1) Input Data Stok Barang\n2) Restok Barang\n3) Daftar Barang\n0) Keluar\n")
            
            sub_menu_1 = input("Masukkan Menu : ")
            
            if(sub_menu_1 == "1"):
                print("\n=== Input Data Stok Barang ===\n")
                
                input_sku = input("Masukkan SKU Barang : ")
                
                if len(str(input_sku)) < 4 or len(str(input_sku)) > 4:
                    print("\nSKU harus 4 digit")
                    continue
                if bst.exists(input_sku) == True:
                    print("\nSKU sudah ada")
                    continue
                
                input_nama_barang = input("Masukkan Nama Barang : ")
                input_harga_satuan = int(input("Masukkan Harga Barang : "))
                input_jumlah_stok = int(input("Masukkan Jumlah Stok : "))
                
                bst.insert({
                    "sku": input_sku,
                    "nama_barang": input_nama_barang,
                    "harga_satuan": input_harga_satuan,
                    "jumlah_stok": input_jumlah_stok,
                })
                print(bst.inorder([]))
                
            elif(sub_menu_1 == "2"):
                print("\n=== Restok Barang ===\n")
                input_sku = input("Masukkan SKU Barang : ")
                if bst.exists(input_sku) == False:
                    print("\nSKU tidak ditemukan")
                    continue
                input_jumlah_stok = int(input("Masukkan Jumlah Stok : "))
                bst.restok_barang(input_sku, input_jumlah_stok)
                
            elif(sub_menu_1 == "3"):
                df = pd.DataFrame(bst.inorder([]), columns=['sku', 'nama_barang', 'harga_satuan', 'jumlah_stok'])
                print(f"\nDaftar Transaksi\n{df}\n")
                
            elif(sub_menu_1 == "0"):
                print("\nKeluar\n")
                sub_answer_1 = False
                
            else:
                print("\nPilihan tidak tersedia\n")
                
    elif input_menu == "2":
        sub_answer_2 = True

        while sub_answer_2:
            print("\nKelola Transaksi\n1) Input Data Transaksi\n2) Lihat Data Seluruh Transaksi Konsumen\n3) Lihat Data Transaksi Berdasarkan Subtotal\n0) Keluar\n")

            sub_menu_2 = input("Masukkan Menu : ")

            if sub_menu_2 == "1":
                print("\n=== Input Data Transaksi ===\n")

                input_nama_konsumen = input("Masukkan nama konsumen = ")
                
                input_sku_answer = True
                while input_sku_answer:
                    while input_sku_answer:
                        input_sku = input("Masukkan SKU Barang : ")
                        if bst.exists(input_sku) == False:
                            print("\nNo. SKU yang diinputkan belum terdaftar")
                            input_lanjut_transaksi = input("Apakah ingin melanjutkan transaksi (Y/N)? : ")
                            if input_lanjut_transaksi == "Y" or input_lanjut_transaksi == "y":
                                continue
                            break
                        break
                    input_jumlah_beli_answer = True
                    while input_jumlah_beli_answer:
                        input_jumlah_beli = int(input("Masukkan jumlah beli = "))
                        barang = bst.exists(input_sku)
                        if barang.jumlah_stok < input_jumlah_beli:
                            print("Jumlah Stok No.SKU yang Anda beli tidak mencukupi")
                            input_lanjut_transaksi = input("Apakah ingin melanjutkan transaksi (Y/N)? : ")
                            if input_lanjut_transaksi == "Y" or input_lanjut_transaksi == "y":
                                continue
                            break
                        barang.jumlah_stok -= input_jumlah_beli
                        subtotal = input_jumlah_beli * barang.harga_satuan

                        transaksi.inputData({
                            "nama_konsumen": input_nama_konsumen,
                            "no_sku": input_sku,
                            "jumlah_beli": input_jumlah_beli,
                            "subtotal": subtotal
                        })

                        dataTransaksi.append({
                            "nama_konsumen": input_nama_konsumen,
                            "no_sku": input_sku,
                            "jumlah_beli": input_jumlah_beli,
                            "subtotal": subtotal
                        })

                        print('\nData Transaksi Konsumen Berhasil Diinputkan\n')
                        print(dataTransaksi)
                        break
                    input_tambah_beli = input('Apakah ingin menambahkan data pembelian untuk konsumen ini (Y/N)? : ')
                    if input_tambah_beli == "Y" or input_tambah_beli == "y":
                        continue
                    break

            elif sub_menu_2 == "2":
                print("\n=== Lihat Data Transaksi ===\n")

                transaksi.checkAllTransactions(dataTransaksi)
            
            elif sub_menu_2 == "3":
                print("\n=== Data Transaksi Berdasarkan Subtotal===\n")

                transaksi.checkTransactionBySubtotal(dataTransaksi)
                
            elif sub_menu_2 == "0":
                print("\nKeluar")
                sub_answer_2 = False

            else:
                print("Menu tidak tersedia")
                continue
        
    elif input_menu == "0":
        print("\nKeluar")
        answer = False
        
    else:
        print("\nPilihan tidak tersedia")
