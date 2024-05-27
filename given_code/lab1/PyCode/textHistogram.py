#
# textHistogram.py - Working with files
#

# the function histogram(L) gets a list of words and returns
# a dictionary with pairs: word and the frequency of this word in the list

def histogram(L):
    d = dict()
    for word in L:
        if word not in d:
            d[word] = 1
        else:
            d[word] = d[word] + 1
    return d
#--------------------

f=open('text1.txt','r')
first = f.read().split() 
f.close()

f=open('text2.txt','r')
second = f.read().split()
f.close()

d1 = histogram(first)
d2 = histogram(second)

print( 'a:','\nfirst file: ', d1, '\n\n\nsecond file: ', d2)

print( '\nNumber of words in file1', len(first) )
print( '\nNumber of words in file2', len(second) )
print( '-'*25 )

f = set(first)
s = set(second)

print( '\nb1 (common words - intersection): ','\n',f&s )
print( '-'*25 )
print( '\nb2 (unique words - xor): ','\n',f^s )


