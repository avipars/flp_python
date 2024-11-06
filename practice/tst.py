from functools import reduce

set_num = set((1,2,3))

print(set_num)

set_num.add(4)
print(set_num)
v = set_num.pop()
print(v)
print(set_num)

tst = [1,2,3,4,5,6,7,8,9,10]

print(tst[0:5])
print(tst[::-1])

def calc():
    def add(x,y):
        return x + y
    def sub(x,y):
        return x - y
    def dispatch(op):
        opNames = ('add','sub')
        ops = (add, sub)
        if op not in opNames:
            print("Invalid operation")
            return None
        else:
            return ops[opNames.index(op)]
    return dispatch
    
c1 = calc()
c2 = calc()
print(c1)
print(c1('add'))
print(c1('add')(2,3))
print(c2('sub')(5,3))

print(list(filter(lambda x: x % 2 == 0, range(10))))

print(list(range(10)))
print(reduce(lambda x,y: x + y, range(10)))
