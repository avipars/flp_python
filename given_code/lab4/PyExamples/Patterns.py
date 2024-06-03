#
from tailrecurse import *
#==========================================================
#
# Map Pattern
#
# Iterative (Non-Functional) implementations
#
def MapIter1(Fnc, In):
    Out = []
    for item in In:
       Out.append(Fnc(item))
    return Out
#
def MapIter2(Fnc, In):
    Out = []
    for item in In:
       Out += [Fnc(item)]
    return Out
#
# List Comprehension implementation
#
def MapLCompr(Fnc, In):
   return [Fnc(item)  for item in In]
#    
#
# Recursive (Functional) implementation
#
def MapRec(Fnc, In):
   if In == []:
     return []
   else:
     return [Fnc(In[0])] + MapRec(Fnc, In[1:])
#
@tail_call_optimized
def MapTailRec(Fnc, In, Result = []):
   if In == []:
     return Result
   else:
     return MapTailRec(Fnc, In[1:], Result + [Fnc(In[0])])
#
#==========================================================
#
# Filter Pattern
#
# Iterative (Non-Functional) implementation
#
def FilterIter1(bF, In):
    Out = []
    for item in In:
       if bF(item):
         Out.append(item)
    return Out
#
def FilterIter2(bF, In):
    Out = []
    for item in In:
       if bF(item):
         Out += [item]
    return Out
#
# Recursive (Functional) implementation
#
def FilterRec(bF, In):
   if In == []:
     return []
   elif bF(In[0]):
     return [In[0]] + FilterRec(bF, In[1:])
   else:
     return FilterRec(bF, In[1:])  
#
@tail_call_optimized
def FilterTailRec(bF, In, Result = []):
   if In == []:
     return Result
   elif bF(In[0]):
     return FilterTailRec(bF, In[1:], Result + [In[0]])
   else:
     return FilterTailRec(bF, In[1:], Result)  
#
# List Comprehension implementation
#
def FilterLCompr(bF, In):
   return [item  for item in In  if bF(item)]
#
#==========================================================
#
# Map-Filter Pattern
#
# Iterative (Non-Functional) implementation
#
def mapFilterIter(bF, func, In):
    Out = []
    for item in In:
       if bF(item):
         Out.append(func(item))
    return Out
#
# Recursive (Functional) implementation
#
def mapFilterRec(bF, func, In):
   if In == []:
     return []
   elif bF(In[0]):
     return [func(In[0])] + mapFilterRec(bF, func, In[1:])
   else:
     return mapFilterRec(bF, func, In[1:])  
#
@tail_call_optimized
def mapFilterTailRec(bF, func, In, Result = []):
   if In == []:
     return Result
   elif bF(In[0]):
     return mapFilterTailRec(bF, In[1:], Result + [func(In[0])])
   else:
     return mapFilterTailRec(bF, In[1:], Result)  
#
# List Comprehension implementation
#
def mapFilterLCompr(bF, func, In):
   return [func(item)  for item in In  if bF(item)]
#
#==========================================================
#
# Reduce Pattern
#
# Iterative (Non-Functional) implementation
#
def reduceIter(Fnc, In):
   result = In[0]
   for item in In[1:]:
      result = Fnc(result, item)
   return result
#
# Recursive (Functional) implementation
#
def reduceRec1(Fnc, In):
   if len(In) == 1:
     return In[0]
   else:
     return Fnc(In[0], reduceRec1(Fnc, In[1:]))
#
@tail_call_optimized
def reduceTailRec1(Fnc, In, Result = 0):
   if In == []:
     return Result
   else:
     return reduceTailRec1(Fnc, In[1:], Fnc(Result, In[0]))
#
#
# (Tail Recursive) List Comprehension implementation
#
@tail_call_optimized
def reduceLCompr(func, In, neutral=0):
   if len(In) == 1:
     return In[0]
   if len(In) % 2 != 0:
     In = In + [neutral]
   funcPairs = [func(In[i],In[i+1]) for i in range(0,len(In)-1,2)]
   return reduceLCompr(func, funcPairs, neutral)
#
# Recursive (Functional) implementations
#
@tail_call_optimized
def reduceRec2(Fnc, In, neutral=0):
 def mapHelper(Fnc, In):
   if In == []:
     return []
   else:
     return [Fnc(In[0][0], In[0][1])] + mapHelper(Fnc, In[1:])
 if len(In) == 1:
   return In[0]
 if len(In) % 2 != 0:
   In = In + [neutral]
 # newIn = mapHelper(Fnc, list(zip(In[0:len(In):2], In[1:len(In):2])))
 newIn = mapHelper(Fnc, list(zip(In[0:len(In):2], In[1:len(In):2])))
 return reduceRec2(Fnc, newIn, neutral)
#
@tail_call_optimized
def reduceRec3(Fnc, In, neutral=0):
 def mapHelper(Fnc, In, Result=[]):
   if In == []:
     return Result
   else:
     return mapHelper(Fnc, In[1:], Result + [Fnc(In[0][0], In[0][1])])
 if len(In) == 1:
   return In[0]
 if len(In) % 2 != 0:
   In = In + [neutral]
 newIn = mapHelper(Fnc, list(zip(In[0:len(In):2], In[1:len(In):2])))
 return reduceRec3(Fnc, newIn, neutral)
#
#==========================================================
