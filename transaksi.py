class Transaksi:
    def __init__(self, nama_konsumen, no_sku, jumlah_beli, subtotal):
        self.nama_konsumen = nama_konsumen
        self.no_sku = no_sku
        self.jumlah_beli = jumlah_beli
        self.subtotal = subtotal

    def inputData():
        print('input')


























































































    def checkAllTransaction():
        data_transaksi = []
        print("=== Data Seluruh Transaksi Konsumen ===")
        if len(data_transaksi) == 0:
            print("Belum ada data transaksi.")
        else:
            for transaksi in data_transaksi:
                nama_konsumen, sku_barang, jumlah_beli, subtotal = transaksi
                print("Nama Konsumen:", nama_konsumen)
                print("No. SKU Barang:", sku_barang)
                print("Jumlah Beli:", jumlah_beli)
                print("Subtotal:", subtotal)
                print("---------------------------------------------------------------")
        # return 