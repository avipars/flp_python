
def q5abcd(inputL):
   Laout = []
   Ldout = []
   Tbout = ()
   Tcout = ()
   for item in inputL:
       if isinstance(item, tuple):
           Laout.extend(item)
       elif isinstance(item,list):
           Tbout = Tbout + tuple(item)
       elif isinstance(item, (int, float)):
           Tcout += (item,)
       elif isinstance(item, str):
           Ldout.append(item)
       else:
           pass
   return Laout, Tbout, Tcout, Ldout

if __name__ == "__main__":
  L = eval(input("enter a list of any length and items of any type: "))
  if isinstance(L, list):
      A,B,C,D = q5abcd(L)
      print(A, '\n', B, '\n', C, '\n', D)
  else:
      print ("ERROR: you must enter a list")
