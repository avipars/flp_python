#
# PainterPlan.py
#
def paintPlan(*Colors) :
      return lambda color : color in Colors
#
clients = ('MrsCohen','MrsLevi','MrsKeshet')
plans   = (paintPlan('white', 'light blue', 'yellow'),\
           paintPlan('black', 'red', 'blue', 'white'),\
           paintPlan('gray','brown','dark blue', 'white'))
paints = dict(zip(clients, plans))
#
print (paints['MrsCohen']('white'))
print (paints['MrsCohen']('red'))
#
