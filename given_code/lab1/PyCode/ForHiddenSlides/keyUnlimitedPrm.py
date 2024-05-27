#
# keyUnlimitedPrm.py
#
def orderTotal(**order):
   # every formal parameter is a part name
   # every actual parameter is the qty of bought units
   inStock = {'p1':100.0, 'p2':250.0, 'p3':50.0}
   notInStock = dict([]) 
   total = 0.0
   if order:
     for pName, pQty in order.items():
        if pName in inStock:
          total += inStock[pName]*pQty
        elif pName not in notInStock:
          notInStock[pName] = pQty
        else:
          notInStock[pName] += pQty
   return (total, notInStock)
#
