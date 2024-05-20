#
# ComposeFuncs.py
#
#***********************************************************
#          "symbolic" composition of two functions          
#***********************************************************
def compose(f, g) :
   return lambda x : f(g(x))

#***********************************************************
#          "symbolic" composition of several functions          
#***********************************************************
def fullCompose(*funcs):
   if len(funcs) > 1:
     composedF = funcs[-1]
     for func in funcs[-2:0:-1] :
        composedF = compose(func, composedF)
     return compose(funcs[0], composedF)
   else:
     return funcs[0]

#***********************************************************
#         computing the composition of two functions        
#***********************************************************
def composeCompute(f, g, x) :
   return f(g(x))

