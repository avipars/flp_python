#
# given a list containing any data items,
# tell if all of them, at all nested levels, are numbers 
#
def isnumber(X):
   return isinstance(X,(int,float))
#
def nestedallnumbers1(L):
   if L == []:
     return True
   elif isinstance(L[0],list):
     return nestedallnumbers1(L[0]) and nestedallnumbers1(L[1:])
   elif isnumber(L[0]):
     return nestedallnumbers1(L[1:])
   else:
     return False
#
def nestedallnumbers2(L):
   # using high-order functions reduce and map, together with recursion
   def allnumbersInItem(item):
      if isinstance(item,list):
        return nestedallnumbers2(item)
      elif isnumber(item):
        return True
      else:
        return False
   return reduce(lambda x,y : x and y, map(allnumbersInItem,L))
#
def nestedallnumbers3(L):
   # using high-order function filter, together with recursion
   def allnumbersFilter(L):
      def numbersInItem(item):
         if type(item) != list:
           if isnumber(item):
             return True
           else:
             return False
         else:
           return (len(item) == len(allnumbersFilter(item)))
      return filter(numbersInItem, L)
   return (len(L) == len(allnumbersFilter(L)))
#
def nestedSum(L):
   if L == []:
     return 0
   elif isinstance(L[0],list):
     return nestedSum(L[0]) + nestedSum(L[1:])
   elif isnumber(L[0]):
     return L[0] + nestedSum(L[1:])
   else:
     return nestedSum(L[1:])
#
L = [2 ,[3 , 4],[5 , [[12] , 8]], 11]
print( nestedallnumbers1(L) )

L = [2 ,[3 , 4],[5 , [[12] , 'a']], 11]
print( nestedallnumbers1(L) )






















