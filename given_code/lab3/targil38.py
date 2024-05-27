
def ezerfunc1(d1, d2, d3, m, dictRes = dict([])):
    if m == []:
        return dictRes
    else:
        dictRes[m[0]] = tuple(set([d1[m[0]], d2[m[0]], d3[m[0]]]))
        return ezerfunc1(d1, d2, d3, m[1:], dictRes)
def ezerfunc2(d1, d2, d3, lm, dOut):
    def lookforall(mafteah):
        return tuple([d[mafteah]  for d in [d1, d2, d3]  if mafteah in d])
    if lm == []:
        return dOut
    dOut[lm[0]] = lookforall(lm[0])
    return ezerfunc2(d1, d2, d3, lm[1:], dOut)

def add3dicts(d1, d2, d3):
    meshutafim = set(d1.keys()) & set(d2.keys()) & set(d3.keys())
    lomeshutaf = (set(d1.keys()) | set(d2.keys()) | set(d3.keys())) - meshutafim
    dOut = ezerfunc1(d1, d2, d3, list(meshutafim))
    dOut = ezerfunc2(d1, d2, d3, list(lomeshutaf), dOut)
    return dOut
##
##>>> d1 = dict([(1,'a'),(3,'d'),(5,'e')])
##>>> d2 = dict([(1,'b'), (3,(11,22)), (7,'f'), (4,'q')])
##>>> d3 = dict([(2,'c'), (3,'x'), (4,'t'), (8,'g')])
##>>> add3dicts(d1,d2,d3)
##{3: ('x', (11, 22), 'd'), 1: ('a', 'b'), 2: ('c',), 4: ('q', 't'), 5: ('e',), 7: ('f',), 8: ('g',)}
##>>>
##
