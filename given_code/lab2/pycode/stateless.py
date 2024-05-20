#
# don't update
# - create the value to be returned
#
# String example
def fullName1(firstName, lastName):
   # functional (stateless) style
   return firstName + ", " + lastName

def fullName2(firstName, lastName):
   # functional (once-only assignment) style
   Name = firstName + ", " + lastName
   return Name
#
# List example
def yearsList1 (From, To):
   # functional (stateless) style
   return list(range(From, To+1))

def yearsList2 (From, To):
   # functional (once-only assignment) style
   years = list(range(From, To+1))
   return years
#
# Dict example
def popAges1(names, ages):
   # functional (stateless) style
   return dict(zip(names, ages))

def popAges2(names, ages):
   # functional (once-only assignment) style
   pairsLst = zip(names, ages)
   return dict(pairsLst)
