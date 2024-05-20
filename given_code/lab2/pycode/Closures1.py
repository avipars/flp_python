#
# Closures1.py
#
def build_taxer(name, rate):
    def taxer(amount):
       return amount * (float(rate) / 100)
    return (name, taxer)

def add_x(x):
   def adder(y):
      return x + y
   return adder
#
# an adders "factory"
adders = dict([])
for i in range(5):
   adders[i] = add_x(i)

# using the adders
for k in adders:
   print (adders[k](10), end=' ')
print ()
#
# a taxers "factory"
taxers  = []
people  = ['Iosi','Rachel','Anna','Naomi','Jack']
rates   = (25.0, 30.0, 20.0, 25.0, 35.0)
amounts = (10000.0, 15000.0, 8000.0, 10000.0, 25000.0)
for i in range(len(people)):
   taxers.append(build_taxer(people[i],rates[i]))
# using the taxers
for i in range(len(amounts)):
   print ((taxers[i][0], taxers[i][1](amounts[i])), end=' ')
#
   
