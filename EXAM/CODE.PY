def shift(S,N):
    if 0<N<len(S):
        return S[-N:]+S[:-N]
    else:
        return S
    
print(shift('abcde',2))

# def f(l,x):
#     def s(l):
#         return lambda x: x>sum(l)/len(l)
#     return s(l)(x)

# def f(l,x):
#     return (lambda x: x>sum(l)/len(l))(x)

def f(l,x):
    def s(l):
        return lambda x: x>sum(l)/len(l)
    return s

# return closure used to check if specific number is greater than average of list


# print(f([1,2,3,4,5],3))
# # check function with 3
# print(f([1,2,3,4,5],3)(7))

# my_list = [1, 3, 5, 7, 9]
# is_greater_than_avg = f(my_list,4)
# print(is_greater_than_avg(4))  # False
# print(is_greater_than_avg(4))  # False
# print(is_greater_than_avg(6))  # True


# f returns a closure, so now utilize it
