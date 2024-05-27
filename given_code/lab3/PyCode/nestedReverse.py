#
# nestedReverse.py -- computes the reverse of a sequence, 
#                     at all its nesting levels
#
def deepReverse(L):
   if L == []:
     return L
   if isinstance(L[-1],list):
     return [deepReverse(L[-1])]+deepReverse(L[:-1])
   else:
     return ([L[-1]]+deepReverse(L[:-1]))

#------------------
##L = [1,[2,3,[4,5]],6]
##print( deepReverse(L) )
