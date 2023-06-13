class BSTNode:
  def __init__(self, barang = {}):
    self.left = None
    self.right = None
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
    
  def get_min(self):
    current = self
    while current.left is not None:
      current = current.left
    return current.sku
    
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