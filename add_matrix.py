
# Rough Work # 

# m1=int(input("Enter the number of rows in first matrix : "))
# n1=int(input("Enter the number of columns in first matrix : "))
# # row2_m1=[]
# m=[]
# for i in range(m1):
#     row=[]
#     for j in range(n1):
#         n=int(input(f"Enter the {i+1,j+1} position element :  "))
#         row.append(n)
#     m.append(row)    
# print(m)        
# print(len(m))
 
                
def create_matrix(row,column):
    name=[]
    for i in range(row):
        temp=[]
        for j in range(column):
            temp2=float(input(f"Enter the {i+1,j+1}th position element :- "))
            temp.append(temp2)
        name.append(temp)    
    return name    
def add_two_matrix():
    m1=int(input("Enter the number of rows in first matrix :- "))
    n1=int(input("Enter the number of columns in first matrix :- "))
    m2=int(input("Enter the number of rows in second matrix :- "))
    n2=int(int(input("Enter the number of columns of second matrix :- ")))
    if m1!=m2 or n1!=n2:
        print("For addition dimension of matrix should be the same")
    else:
        sum=[]
        mat_1=create_matrix(m1,n1)
        print()
        print("Matrix 1 is : ")
        print(mat_1)
        print()
        mat_2=create_matrix(m2,n2) 
        print() 
        print("Matrix 2 is : ")  
        print(mat_2)
        print()
        for i in range(m1):
            temp1=[]
            for j in range(n1):
                temp2=mat_1[i][j]+mat_2[i][j]
                temp1.append(temp2)
            sum.append(temp1)
        return sum   

print(f"Sum of Matrix 1 and Matrix 2 is : {add_two_matrix()}")            
            
             
