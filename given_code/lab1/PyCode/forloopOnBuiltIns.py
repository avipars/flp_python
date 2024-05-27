#
# forloopOnBuiltIns.py
#
typeSet = set([])
for i in range(5):
   while True:
     Obj = eval(input("Enter the iterable object to loop on : "))
     ObjType = type(Obj)
     if ObjType not in typeSet:
       typeSet.add(ObjType)
       L = []
       for item in Obj:
          L.append(item)
       print (L)
       break
     else:
       print ("You already tried this object type")
print ("Done !")
#
## RESTART: P:\forloopOnBuiltIns.py 
##Enter the iterable object to loop on : ['a','b','edf',2.0]
##['a', 'b', 'edf', 2.0]
##Enter the iterable object to loop on : (3,'abf',12)
##[3, 'abf', 12]
##Enter the iterable object to loop on : set([34,10,'abc',10])
##['abc', 34, 10]
##Enter the iterable object to loop on : dict(zip([1,2,3], ['a','b','c']))
##[1, 2, 3]
##Enter the iterable object to loop on : 'str example'
##['s', 't', 'r', ' ', 'e', 'x', 'a', 'm', 'p', 'l', 'e']
##Done !
