#
#
#
import sys
#
def pentaNumRange(n1, n2):
    return list(map(lambda n : n*(3*n-1)/2, range(n1, n2)))

def get2nums():
    n1 = eval(input("enter the value of n1: "))
    n2 = eval(input("enter the value of n2: "))
    if isinstance(n1,int) and n1 > 0 and isinstance(n2, int) and n1 < n2:
      return n1, n2
    return False

def myprint(line):
    print(line)
    return None

def pentaprt(L):
    return map(myprint, list(map(lambda i : L[i:i+10], range(0,len(L),10))))

def main():
    inValues = get2nums()
    if not inValues:
      print ("ERROR: the input is incorrect!")
      sys.exit()
    n1, n2 = inValues
    list(pentaprt(pentaNumRange(n1, n2)))
    print ("Bye")

main()    
      
