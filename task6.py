class Node:
    def __init__(self, code, price):
      self.left = None
      self.right = None
      self.code = code
      self.price = price

    def insert(self, code, price):
      if self.code:
         if code < self.code:
            if self.left is None:
               self.left = Node(code, price)
            else:
               self.left.insert(code, price)
         elif code > self.code:
            if self.right is None:
               self.right = Node(code, price)
            else:
               self.right.insert(code, price)
      else:
         self.code = code
         self.price = price

    def search(self, val):
        if val == self.code:
            return self.price
        elif val < self.code:
            if self.left:
                return self.left.search(val)
            else:
                return str(val)+" not found"
        
        else:
            if self.right:
                return self.right.search(val)
            else:
                return str(val)+" not found" 
