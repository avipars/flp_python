def g1(N):
    yielded_N = N
    while N > 0:
        yielded_N = N
        N -= 1
        yield yielded_N
    print ("after the while loop")
    yielded_N = -1
    yield yielded_N

def g2(N):
    yielded_N = N
    while N > 0:
        yielded_N = N
        N -= 1
        yield yielded_N
    print ("after the while loop")
    yielded_N = -1
    return yielded_N

def g2b(N):
    yielded_N = N
    while N > 0:
        yielded_N = N
        N -= 1
        yield yielded_N
    print ("after the while loop")
    #yielded_N = -1
    #return yielded_N

def g3(N):
    yielded_N = N
    while N > 0:
        yielded_N = N
        N -= 1
        if N == 5:
            print ("N == 5")
            yield yielded_N
        else:
          print ("N != 5")
          yield yielded_N
    print ("after the while loop")
    yielded_N = -1
    yield yielded_N

def g4(N):
    yielded_N = N
    while N > 0:
        yielded_N = N
        N -= 1
        if N == 5:
            print ("N == 5")
            return yielded_N
        else:
            print ("N != 5")
            yield yielded_N
    print ("after the while loop")
    yielded_N = -1
    return yielded_N
    
def g4b(N):
    yielded_N = N
    while N > 0:
        yielded_N = N
        N -= 1
        if N == 5:
            print ("N == 5")
            #return yielded_N
        else:
            print ("N != 5")
            yield yielded_N
    print ("after the while loop")
    yielded_N = -1
    return yielded_N
