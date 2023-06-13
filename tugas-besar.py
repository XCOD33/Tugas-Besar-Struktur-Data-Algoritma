import Input_Data

input_data_barang = Input_Data.BSTNode({
    "sku": 0000,
    "nama_barang": "",
    "harga_satuan": 0,
    "jumlah_stok": 0,
})

answer = True

while answer:
    print("Selamat Datang di Aplikasi Kelola Barang\n1) Kelola Stok Barang\n2) Kelola Transaksi Konsumen\n0) Keluar\n")

    input_menu = input("Masukkan Menu : ")

    if (input_menu == "1"):
        
        sub_answer_1 = True
        
        while sub_answer_1:
            print("\nKelola Stok Barang\n1) Input Data Stok Barang\n2) Restok Barang\n0) Keluar\n")
            sub_menu_1 = input("Masukkan Menu : ")
            if(sub_menu_1 == "1"):
                print("\n=== Input Data Stok Barang ===\n")
                input_sku = input("Masukkan SKU Barang : ")
                if len(str(input_sku)) < 4 or len(str(input_sku)) > 4:
                    print("\nSKU harus 4 digit")
                    continue
                input_nama_barang = input("Masukkan Nama Barang : ")
                input_harga_satuan = input("Masukkan Harga Barang : ")
                input_jumlah_stok = input("Masukkan Jumlah Stok : ")
                input_data_barang.insert({
                    "sku": input_sku,
                    "nama_barang": input_nama_barang,
                    "harga_satuan": input_harga_satuan,
                    "jumlah_stok": input_jumlah_stok,
                })
            elif(sub_menu_1 == "2"):
                print("\n=== Restok Barang ===\n")
            elif(sub_menu_1 == "0"):
                print("\nKeluar\n")
                sub_answer_1 = False
            else:
                print("\nPilihan tidak tersedia\n")
    elif input_menu == "2":
        print("\nKelola Transaksi Konsumen")
    elif input_menu == "0":
        print("\nKeluar")
        answer = False
    else:
        print("\nPilihan tidak tersedia")
