##
##===============================================================================
##
## FUNTION NAME: unnest
## PARAMETERS: list of lists (of indefinite nesting depth)
## DESCRIPTION: returns a top-level list containing all atoms of the nested list
##              if the list is empty, the function returns an empty list
##
## run example:  unnest([2, [5 ,'g', ['b', ['w', 4 ,5], 8], 10]])
##               [2 5 'g' 'b' 'w' 4 5 8 10]
## 
def unnest(L):
   #if not L:
   #if L == []:
   if len(L)==0:
     return []
   else:
     head = L[0]
     tail = L[1:]
     if isinstance(head,(tuple,list)): 
       return unnest(head) + unnest(tail)
     else:
       return [head] + unnest(tail)	 
##
print( unnest([2, [5 ,'g', ['b', ['w', 4 ,5], 8], 10]])  )

##>>> 
##[2, 5, 'g', 'b', 'w', 4, 5, 8, 10]
##>>>
