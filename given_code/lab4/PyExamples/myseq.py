#
# myseq.py  -- data structures creation using reduce
#
from functools import *

def mylist(seq):
   return reduce(lambda outdata, currentitem : outdata + [currentitem], seq, [])

def mytuple(seq):
   return reduce(lambda outdata, currentitem : outdata + (currentitem,), seq, ())

def myset(seq):
   return reduce(lambda outdata, currentitem : outdata | {currentitem}, seq, set([]))

def myzip(seq1, seq2):
   if len(seq1) <= len(seq2):
     s1 = seq1
     s2 = seq2
   else:
     s1 = seq2
     s2 = seq1
   return reduce(lambda output, current : output + [(current, s2[s1.index(current)])], s1,[])

def mydict1(seq1, seq2):
   return dict(myzip(seq1, seq2))

def mydict2(seq1, seq2):
   def updtDict(D,pair):
      D[pair[0]] = pair[1]
      return D
   return reduce(lambda output, current : updtDict(output, current) , myzip(seq1, seq2), {})
