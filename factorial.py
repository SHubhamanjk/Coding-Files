# using non recursive fucntion


# n=int(input("Enter the number :- "))
# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)    


# using recursive fucntion

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))    