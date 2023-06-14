from BST import BSTNode
from transaksi import Transaksi
import pandas as pd

bst = BSTNode()  # Membuat instance objek dari kelas BSTNode

transaksi = Transaksi({  # Membuat instance objek dari kelas Transaksi
    "nama_konsumen": "",
    "no_sku": 0000,
    "jumlah_beli": 0,
    "subtotal": 0
})

answer = True  # Variabel untuk menjaga agar program tetap berjalan
dataTransaksi = []  # List untuk menyimpan data transaksi

while answer:
    print("Selamat Datang di Aplikasi Kelola Barang\n1) Kelola Stok Barang\n2) Kelola Transaksi Konsumen\n0) Keluar\n")

    input_menu = input("Masukkan Menu : ")  # Mengambil input menu dari pengguna

    if input_menu == "1":  # Jika menu yang dipilih adalah 1 (Kelola Stok Barang)
        sub_answer_1 = True  # Variabel untuk menjaga agar tetap berada di dalam sub-menu 1

        while sub_answer_1:
            print("\nKelola Stok Barang\n1) Input Data Stok Barang\n2) Restok Barang\n3) Daftar Barang\n0) Keluar\n")

            sub_menu_1 = input("Masukkan Menu : ")  # Mengambil input sub-menu 1 dari pengguna

            if sub_menu_1 == "1":  # Jika sub-menu yang dipilih adalah 1 (Input Data Stok Barang)
                print("\n=== Input Data Stok Barang ===\n")

                input_sku = input("Masukkan SKU Barang : ")  # Mengambil input SKU barang dari pengguna

                if len(str(input_sku)) < 4 or len(str(input_sku)) > 4:  # Validasi panjang SKU harus 4 digit
                    print("\nSKU harus 4 digit")
                    continue
                if bst.exists(input_sku) == True:  # Validasi SKU barang sudah ada
                    print("\nSKU sudah ada")
                    continue

                input_nama_barang = input("Masukkan Nama Barang : ")  # Mengambil input nama barang dari pengguna
                input_harga_satuan = int(input("Masukkan Harga Barang : "))  # Mengambil input harga satuan dari pengguna
                input_jumlah_stok = int(input("Masukkan Jumlah Stok : "))  # Mengambil input jumlah stok dari pengguna

                bst.insert({  # Menyisipkan data barang ke dalam BST
                    "sku": input_sku,
                    "nama_barang": input_nama_barang,
                    "harga_satuan": input_harga_satuan,
                    "jumlah_stok": input_jumlah_stok,
                })
                print(bst.inorder([]))  # Menampilkan daftar barang menggunakan traversal inorder BST

            elif sub_menu_1 == "2":  # Jika sub-menu yang dipilih adalah 2 (Restok Barang)
                print("\n=== Restok Barang ===\n")
                input_sku = input("Masukkan SKU Barang : ")  # Mengambil input SKU barang yang akan direstok

                if bst.exists(input_sku) == False:  # Validasi SKU barang tidak ditemukan
                    print("\nSKU tidak ditemukan")
                    continue

                input_jumlah_stok = int(input("Masukkan Jumlah Stok : "))  # Mengambil input jumlah stok yang akan ditambahkan
                bst.restok_barang(input_sku, input_jumlah_stok)  # Melakukan restok barang

            elif sub_menu_1 == "3":  # Jika sub-menu yang dipilih adalah 3 (Daftar Barang)
                df = pd.DataFrame(bst.inorder([]), columns=['sku', 'nama_barang', 'harga_satuan', 'jumlah_stok'])
                print(f"\nDaftar Transaksi\n{df}\n")  # Menampilkan daftar barang menggunakan Pandas DataFrame

            elif sub_menu_1 == "0":  # Jika sub-menu yang dipilih adalah 0 (Keluar)
                print("\nKeluar\n")
                sub_answer_1 = False  # Keluar dari sub-menu 1

            else:
                print("\nPilihan tidak tersedia\n")

    elif input_menu == "2":  # Jika menu yang dipilih adalah 2 (Kelola Transaksi Konsumen)
        sub_answer_2 = True  # Variabel untuk menjaga agar tetap berada di dalam sub-menu 2

        while sub_answer_2:
            print("\nKelola Transaksi\n1) Input Data Transaksi\n2) Lihat Data Seluruh Transaksi Konsumen\n3) Lihat Data Transaksi Berdasarkan Subtotal\n0) Keluar\n")

            sub_menu_2 = input("Masukkan Menu : ")  # Mengambil input sub-menu 2 dari pengguna

            if sub_menu_2 == "1":  # Jika sub-menu yang dipilih adalah 1 (Input Data Transaksi)
                print("\n=== Input Data Transaksi ===\n")

                input_nama_konsumen = input("Masukkan nama konsumen = ")  # Mengambil input nama konsumen dari pengguna

                input_sku_answer = True
                while input_sku_answer:
                    while input_sku_answer:
                        input_sku = input("Masukkan SKU Barang : ")  # Mengambil input SKU barang dari pengguna

                        if bst.exists(input_sku) == False:  # Validasi SKU barang belum terdaftar
                            print("\nNo. SKU yang diinputkan belum terdaftar")
                            input_lanjut_transaksi = input("Apakah ingin melanjutkan transaksi (Y/N)? : ")
                            if input_lanjut_transaksi == "Y" or input_lanjut_transaksi == "y":
                                continue
                            break
                        break

                    input_jumlah_beli_answer = True
                    while input_jumlah_beli_answer:
                        input_jumlah_beli = int(input("Masukkan jumlah beli = "))  # Mengambil input jumlah beli dari pengguna
                        barang = bst.exists(input_sku)

                        if barang.jumlah_stok < input_jumlah_beli:  # Validasi jumlah stok barang tidak mencukupi
                            print("Jumlah Stok No.SKU yang Anda beli tidak mencukupi")
                            input_lanjut_transaksi = input("Apakah ingin melanjutkan transaksi (Y/N)? : ")
                            if input_lanjut_transaksi == "Y" or input_lanjut_transaksi == "y":
                                continue
                            break

                        barang.jumlah_stok -= input_jumlah_beli  # Mengurangi jumlah stok barang yang dibeli
                        subtotal = input_jumlah_beli * barang.harga_satuan  # Menghitung subtotal transaksi

                        transaksi.inputData({  # Memasukkan data transaksi ke dalam objek Transaksi
                            "nama_konsumen": input_nama_konsumen,
                            "no_sku": input_sku,
                            "jumlah_beli": input_jumlah_beli,
                            "subtotal": subtotal
                        })

                        dataTransaksi.append({  # Menyimpan data transaksi ke dalam list
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

            elif sub_menu_2 == "2":  # Jika sub-menu yang dipilih adalah 2 (Lihat Data Seluruh Transaksi Konsumen)
                print("\n=== Lihat Data Transaksi ===\n")
                transaksi.checkAllTransactions(dataTransaksi)  # Menampilkan semua data transaksi

            elif sub_menu_2 == "3":  # Jika sub-menu yang dipilih adalah 3 (Lihat Data Transaksi Berdasarkan Subtotal)
                print("\n=== Data Transaksi Berdasarkan Subtotal===\n")
                transaksi.checkTransactionBySubtotal(dataTransaksi)  # Menampilkan data transaksi berdasarkan subtotal

            elif sub_menu_2 == "0":  # Jika sub-menu yang dipilih adalah 0 (Keluar)
                print("\nKeluar")
                sub_answer_2 = False  # Keluar dari sub-menu 2

            else:
                print("Menu tidak tersedia")
                continue

    elif input_menu == "0":  # Jika menu yang dipilih adalah 0 (Keluar)
        print("\nKeluar")
        answer = False  # Keluar dari program

    else:
        print("\nPilihan tidak tersedia")
