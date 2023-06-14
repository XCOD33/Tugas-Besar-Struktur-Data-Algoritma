import pandas as pd

class Transaksi:
    def __init__(self, transaksi={}):
        self.nama_konsumen = transaksi['nama_konsumen']
        self.no_sku = transaksi['no_sku']
        self.jumlah_beli = transaksi['jumlah_beli']
        self.subtotal = transaksi['subtotal']
        

    def inputData(self, transaksi):
        if not self.no_sku:
            # Jika data transaksi kosong, inisialisasi atribut dengan data transaksi baru
            self.nama_konsumen = transaksi['nama_konsumen']
            self.no_sku = transaksi['no_sku']
            self.jumlah_beli = transaksi['jumlah_beli']
            self.subtotal = transaksi['subtotal']
            return
        
        print("Transaksi berhasil ditambahkan")

    def checkAllTransactions(self, transactions):
        if len(transactions) == 0:
            print("Belum ada data transaksi")
        else:
            print("Data transaksi konsumen:")
            print("Nama Konsumen\tNo. SKU barang\tJumlah Beli\tSubtotal")
            for transaction in transactions:
                # Menampilkan data transaksi secara berurutan
                print("{}\t\t{}\t\t{}\t\t{}".format(
                    transaction['nama_konsumen'],
                    transaction['no_sku'],
                    transaction['jumlah_beli'],
                    transaction['subtotal']
                ))

    def checkTransactionBySubtotal(self, transactions):
        if len(transactions) == 0:
            print("Belum ada data transaksi")
        else:
            def bubble_sort(arr):
                n = len(arr)
                for i in range(n - 1):
                    for j in range(n - i - 1):
                        if arr[j]['subtotal'] < arr[j + 1]['subtotal']:
                            # Melakukan bubble sort berdasarkan subtotal transaksi
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
            def display_transaksi(transactions):
                print("Data transaksi konsumen:")
                print("Nama Konsumen\tNo. SKU barang\tJumlah Beli\tSubtotal")
                for transaction in transactions:
                    # Menampilkan data transaksi secara berurutan setelah diurutkan berdasarkan subtotal
                    print("{}\t\t{}\t\t{}\t\t{}".format(
                        transaction['nama_konsumen'],
                        transaction['no_sku'],
                        transaction['jumlah_beli'],
                        transaction['subtotal']
                    ))

            bubble_sort(transactions)
            display_transaksi(transactions)
