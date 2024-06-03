#
# eratosthenes.py
# The Eratosthenes' algorithm
#
def napa(N):
    rishoni = [True]*N
    rishoni[0] = False
    # make rishoni to be an array of True values for prime numbers
    for i in range(2,N):
        if rishoni[i]:
            for mlt in range(i*2,N,i):
               rishoni[mlt]=False
    res = []
    for i, item in enumerate(rishoni):
       if item:
         res.append(i)
    return res
