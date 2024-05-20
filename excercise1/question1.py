#%%
# made by avi parshan

'''
Question 1 - triangle lengths
'''
def triangle(a,b,c):
    if a + b > c and a + c > b and c + b > a:
        print("they are correct triangle sides’ lengths")
    else: 
        print("they are in error")


a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
triangle(a,b,c)


# %%
