from BST import BSTNode

bst = BSTNode()

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
                
            elif(sub_menu_1 == "2"):
                print("\n=== Restok Barang ===\n")
                input_sku = input("Masukkan SKU Barang : ")
                if bst.exists(input_sku) == False:
                    print("\nSKU tidak ditemukan")
                    continue
                input_jumlah_stok = int(input("Masukkan Jumlah Stok : "))
                bst.restok_barang(input_sku, input_jumlah_stok)
                print(bst.inorder([]))
                
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
