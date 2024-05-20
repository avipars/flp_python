#
# Calc.py
#
def makeCalc():
   def add(x,y):
      return x+y
   def mult(x,y):
      return x*y
   def div (x,y):
      return x/y
   def minus (x,y):
      return x-y
   def dispatch(op):
      opNames   = ('add', 'mult', 'div', 'minus')
      Ops = (add, mult, div, minus)
      if op in opNames:
        return Ops[opNames.index(op)]
      else:
        print ("invalid operator")
        sys.exit()
   return dispatch
#
c1 = makeCalc()
c2 = makeCalc()
print (c1('add')(2,3))
print (c2('mult')(2,3))
#
        
