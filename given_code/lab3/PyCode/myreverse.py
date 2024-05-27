#
# Home work 3.3 and 3.4
#
def myreverse(n):
    def treverse(n, nLength):
        if nLength == 0:
          return n
        else:
          return n%10 * 10**nLength + treverse(n//10,nLength-1)
    nLength = len(str(n))
    return treverse(n,nLength-1)
#
def myreverse2(n):
   def treverse(strN):
    if strN == "":
        return strN
    else:
        return strN[-1] + myreverse2(strN[:-1])
   return int(treverse(str(n)))
#
def myreverse3(n):
    def prodCalc(L,result=0):
        if L == []:
            return result
        else:
            return prodCalc(L[1:],result*10+L[0])
    def treverse(n):
        if 0 <= n < 10:
          return [n]
        else:
          return [n%10] + treverse(n//10)
    return prodCalc(treverse(n))
#
def isPalindrome(n):
    if n == myreverse3(n):
        print("It is a palindrome !!")
    else:
        print("It is not a palindrome")
#

