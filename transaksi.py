class Transaksi:
    def __init__(self, nama_konsumen, no_sku, jumlah_beli, subtotal):
        self.nama_konsumen = nama_konsumen
        self.no_sku = no_sku
        self.jumlah_beli = jumlah_beli
        self.subtotal = subtotal
        self.allData = []

    def inputData(self):
        input_nama = input("Masukkan nama = ")
        input_no_sku = input("Masukkan No SKU = ")
        input_jumlah_beli = input("Masukkan jumlah = ")
        subtotal = input_jumlah_beli * 1000
        self.allData.append(Transaksi(input_nama, input_no_sku, input_jumlah_beli, subtotal))

    def checkAllTransaction(self):
        for data in self.allData :
            print(data)
        

    def checkTransactionBySubtotal(self):
        print('input')


test = Transaksi("udin", 123, 12, 1100)
print(test)