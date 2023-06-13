class BSTNode:
  def __init__(self, barang = None):
    self.left = None
    self.right = None
    self.sku = None
    self.nama_barang = None
    self.harga_satuan = None
    self.jumlah_stok = None
    if barang:
      self.sku = barang['sku']
      self.nama_barang = barang['nama_barang']
      self.harga_satuan = barang['harga_satuan']
      self.jumlah_stok = barang['jumlah_stok']
    
  def insert(self, barang):
    if not self.sku:
      self.sku = barang['sku']
      self.nama_barang = barang['nama_barang']
      self.harga_satuan = barang['harga_satuan']
      self.jumlah_stok = barang['jumlah_stok']
      return
    if self.sku == barang['sku']:
      print("\nSKU sudah ada")
      return
    print("\nSKU telah dimasukkan")
    if barang['sku'] < self.sku:
      if self.left:
        self.left.insert(barang)
        return
      self.left = BSTNode(barang)
      return
    if self.right:
      self.right.insert(barang)
      return
    self.right = BSTNode(barang)
    
  def exists(self, sku):
    if sku == self.sku:
      return True
    
    if not self.sku:
      return False
    
    if sku < self.sku:
      if self.left == None:
        return False
      return self.left.exists(sku)
    
    if self.right == None:
      return False
    return self.right.exists(sku)
  
  def restok_barang(self, sku, jumlah_stok):
    if self.exists(sku):
      self.jumlah_stok += jumlah_stok
      print("\nBarang berhasil di restok")
      return
    print("\nSKU tidak ditemukan")
    return  
    
  def inorder(self, barangs):
    if self.left is not None:
      self.left.inorder(barangs)
    if self.sku is not None:
      barangs.append({
        "sku": self.sku,
        "nama_barang": self.nama_barang,
        "harga_satuan": self.harga_satuan,
        "jumlah_stok": self.jumlah_stok,
      })
    if self.right is not None:
      self.right.inorder(barangs)
    return barangs
  
# dict1 = {
#   "sku": 0000,
#   "nama_barang": "AAA",
#   "harga_satuan": 1000,
#   "jumlah_stok": 10,
# }
# dict2 = {
#   "sku": 1111,
#   "nama_barang": "BBBB",
#   "harga_satuan": 2000,
#   "jumlah_stok": 20,
# }
# dict3 = {
#   "sku": 22222,
#   "nama_barang": "CCC",
#   "harga_satuan": 3000,
#   "jumlah_stok": 30,
# }
# dict4 = {
#   "sku": 1111,
#   "nama_barang": "DDD",
#   "harga_satuan": 4000,
#   "jumlah_stok": 40,
# }

# r = BSTNode(dict1)
# r.insert(dict2)
# r.insert(dict3)
# print(r.exists(1111))