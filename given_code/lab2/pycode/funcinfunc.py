#
# funcinfunc.py
#
def foo (x,y) :
    def bar (z) :
        return z * 2
    return bar(x) + y
