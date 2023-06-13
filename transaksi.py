class Transaksi:
    def __init__(self, nama_konsumen, no_sku, jumlah_beli, subtotal):
        self.nama_konsumen = nama_konsumen
        self.no_sku = no_sku
        self.jumlah_beli = jumlah_beli
        self.subtotal = subtotal
        

    def inputData():
        input_nama = input("Masukkan Nama = ")
        input_no_sku = input("Masukkan SKU = ")
        input_jml = int(input("Masukkan Jumlah = "))
        subtotal = input_jml * 1000
        data = Transaksi(input_nama, input_no_sku, input_jml, subtotal)

        return data

    def checkTransactionBySubtotal(transactions):
        if len(transactions) == 0:
            print("Belum ada data transaksi")
        else:
            def bubble_sort(arr):
                n = len(arr)
                for i in range(n - 1):
                    for j in range(n - i - 1):
                        if arr[j].subtotal < arr[j + 1].subtotal:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            def display_transaksi(transactions):
                print("Data transaksi konsumen:")
                print("Nama Konsumen\tNo. SKU barang\tJumlah Beli\tSubtotal")
                for transaction in transactions:
                    print("{}\t\t{}\t\t{}\t\t{}".format(transaction.nama_konsumen, transaction.no_sku, transaction.jumlah_beli, transaction.subtotal))

            bubble_sort(transactions)
            display_transaksi(transactions)

transaksi = []

# tes = Transaksi("aa", 99, 2, 22)
transaksi.append(Transaksi.inputData())
Transaksi.checkTransactionBySubtotal(transaksi)
transaksi.append(Transaksi.inputData())
Transaksi.checkTransactionBySubtotal(transaksi)