l = [8, 45, 96, 3, 78, 26, 34, 89, 69, 4, 5, 21, 19]
sl = []

def find_min(l):
    mn=l[0]
    for i in range(0,len(l)):
        if mn>l[i]:
            mn=l[i]
        else:
            pass
    return mn    
def remove_element(lst, value):
    new_lst = []
    for i in range(0,len(l)):
        if lst[i] != value:
            new_lst.append(lst[i])
    return new_lst
for i in range(0,len(l)):
    a=find_min(l)
    sl.append(a)    
    l=remove_element(l,a)
        

print(sl)