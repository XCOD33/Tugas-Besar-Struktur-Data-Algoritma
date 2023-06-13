from transaksi import Transaksi
tes = Transaksi("aa", 99, 2, 22)
answer = True

while answer:
    print("""
    Selamat Datang di Aplikasi Kelola Barang
    1) Kelola Stok Barang
    2) Kelola Transaksi Konsumen
    0) Keluar
    """)

    input_menu = input("Masukkan Menu : ")

    if (input_menu == "1"):
        print("\n Kelola Stok Barang")
    elif input_menu == "2":
        print("\n Kelola Transaksi Konsumen")
        transaksi = []
        transaksi.append(Transaksi.inputData())
        Transaksi.checkTransactionBySubtotal(transaksi)
    elif input_menu == "0":
        print("\n Keluar")
        answer = False
    else:
        print("\n Pilihan tidak tersedia")
