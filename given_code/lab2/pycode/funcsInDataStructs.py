#
# funcsInDataStructs.py
#
import statistics as stat
import random
#
def callF(fobj, data):
   return fobj(data)
# main
avg    = stat.mean
fNames = ['minimum', 'maximum', 'sum', 'average', 'stdev']
fObjs  = [min, max, sum, avg, stat.stdev]
fLst   = list(zip(fNames, fObjs))
for i in range(2):
  data   = random.choices(list(range(0,1000)), k=10)
  print ('\nStatistics will be calculated over', data)
  for i in range(len(fLst)):
    fname = fLst[i][0]
    print ('The ' + fname, 'of the data is', end=' ')
    print (callF(fLst[i][1], data))
#

