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

t = Transaksi('Sugeng', 'SKU001', 5, 100000)
t1 = Transaksi('Sogong', 'SKU002', 2, 350000)
transactions = [t,t1]
print(len(transactions))
Transaksi.checkTransactionBySubtotal(transactions)