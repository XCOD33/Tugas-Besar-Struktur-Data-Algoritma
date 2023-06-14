class BSTNode:
  # Inisialisasi node
  def __init__(self, barang=None):
    self.left = None
    self.right = None
    self.sku = None
    self.nama_barang = None
    self.harga_satuan = None
    self.jumlah_stok = None

    # Jika ada data barang, inisialisasi atribut node dengan data tersebut
    if barang:
      self.sku = barang['sku']
      self.nama_barang = barang['nama_barang']
      self.harga_satuan = barang['harga_satuan']
      self.jumlah_stok = barang['jumlah_stok']
    
  def insert(self, barang):
    if not self.sku:
      # Jika node kosong, masukkan data barang ke dalam node
      self.sku = barang['sku']
      self.nama_barang = barang['nama_barang']
      self.harga_satuan = barang['harga_satuan']
      self.jumlah_stok = barang['jumlah_stok']
      return

    # Jika SKU barang sudah ada dalam node, cetak pesan dan hentikan operasi penambahan
    if self.sku == barang['sku']:
      print("\nSKU sudah ada")
      return

    print("\nSKU telah dimasukkan")

    if barang['sku'] < self.sku:
      if self.left:
        # Jika ada child node di sebelah kiri, rekursif panggil method insert pada child node tersebut
        self.left.insert(barang)
        return
      self.left = BSTNode(barang)
      return

    if self.right:
      # Jika ada child node di sebelah kanan, rekursif panggil method insert pada child node tersebut
      self.right.insert(barang)
      return

    self.right = BSTNode(barang)
    
  def exists(self, sku):
    if sku == self.sku:
      return self

    if not self.sku:
      return False
    
    if sku < self.sku:
      if self.left == None:
        return False
      # Jika ada child node di sebelah kiri, rekursif panggil method exists pada child node tersebut
      return self.left.exists(sku)
    
    if self.right == None:
      return False
    # Jika ada child node di sebelah kanan, rekursif panggil method exists pada child node tersebut
    return self.right.exists(sku)
  
  def restok_barang(self, sku, jumlah_stok):
    if self.exists(sku):
      barang = self.exists(sku)
      if barang:
        # Jika SKU barang ditemukan, tambahkan jumlah stok baru ke stok barang yang ada
        barang.jumlah_stok += jumlah_stok
        print("\nBarang berhasil di restok")
        return

    print("\nSKU tidak ditemukan")
    return  
    
  def inorder(self, barangs):
    if self.left is not None:
      # Rekursif panggil method inorder pada child node di sebelah kiri
      self.left.inorder(barangs)

    if self.sku is not None:
      # Tambahkan data barang ke dalam list barangs
      barangs.append({
        "sku": self.sku,
        "nama_barang": self.nama_barang,
        "harga_satuan": self.harga_satuan,
        "jumlah_stok": self.jumlah_stok,
      })

    if self.right is not None:
      # Rekursif panggil method inorder pada child node di sebelah kanan
      self.right.inorder(barangs)

    return barangs
