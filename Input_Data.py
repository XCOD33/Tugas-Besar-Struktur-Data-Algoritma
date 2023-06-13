class BSTNode:
  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val = val
    
  def insert(self, val):
    if not self.val:
      self.val = val
      return
    if self.val == val:
      return
    if val < self.val:
      if self.left:
        self.left.insert(val)
        return
      self.left = BSTNode(val)
      return
    if self.right:
      self.right.insert(val)
      return
    self.right = BSTNode(val)
    
  def get_min(self):
    current = self
    while current.left is not None:
      current = current.left
    return current.val
    
  def inorder(self, vals):
    if self.left is not None:
      self.left.inorder(vals)
    if self.val is not None:
      vals.append(self.val)
    if self.right is not None:
      self.right.inorder(vals)
    return vals
  
r = BSTNode(0, "Buku Tulis", 2000, 10)
r.insert(28)
r.insert(1)
print(r.inorder([]))