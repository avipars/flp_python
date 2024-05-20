#
# funcreturnfunc.py
#
def foo (x = 0) :
    def bar(y) :
        return x + y
    return bar
# main
print (foo(1)(3))
f = foo(3)
print (f)
print (f(2))

