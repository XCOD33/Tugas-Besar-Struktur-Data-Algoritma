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