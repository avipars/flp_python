def my_gen():    
     n = 1    
     print('This is printed first')    
     # A Generator function contains yield statements    
     yield n    
     n += 1    
     print('This is printed second')    
     yield n    
     n += 1    
     print('This is printed at last')    
     yield n

def rev_str(my_str):
    for i in range(len(my_str)-1, -1, -1):
        yield my_str[i]



def f(a):
    return a*a

def f():
    return 5*5  ## ==>  10


##f(3+2) ==>  f(5)
##
##def f(x,y,z):             def f'(y,z):              def f''(z):               def f'''():
##    return sum([x,y,z])       return sum([5,y,z])       return sum([5,13,z])     return sum([5,13,6])  ==>  24   
##
##n = 7
##f(2+3, 6+n, 3*2) => f(5,6+7, 6) => f(5,13,6)

