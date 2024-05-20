#
# funcasparam.py
#
def foo(f, L) :
    # this function is not stateless, but it is functional:
    # 1) the output depends only on the input
    # 2) there are no side-effects:
    #   - the input is not changed
    #   - any non local data is not used or changed
    L1 = list(L[:])
    for i in range(len(L)):
        L1[i] = f(L[i])
    return L1

def bar(x) :
    return x * x



