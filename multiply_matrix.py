def create_matrix(m,n):
    mat=[]
    for i in range(m):
        temp1=[]
        for j in range(n):
            temp2=float(input(f"Enter the {i+1,j+1}th position element : "))
            temp1.append(temp2)
        mat.append(temp1)
    return mat

def multiply_two_matrix():
    m1=int(input("Enter the number of rows in first matrix :- "))
    n1=int(input("Enter the number of columns in first matrix :- "))
    m2=int(input("Enter the number of rows in second matrix :- "))
    n2=int(int(input("Enter the number of columns of second matrix :- ")))
    if n2!=m1:
        print("Please Enter Valid Dimension")
    else:
        mat_1=create_matrix(m1,n1)
        mat_2=create_matrix(m2,n2)  
        res=[]  
        
        for i in range(m1):  # row of first matrix 
            temp1=[]
            for j in range(n2): # column of second matrix
                sum=0
                for k in range(m2):   # row of second matrix
                    sum += mat_1[i][k] * mat_2[k][j]   # mat_1[i(for first row)][k(var) for first column of second row] * mat_2[k(var)][j]
                    # sum+=temp2
                temp1.append(sum) 
            res.append(temp1)
        return res
               
print(multiply_two_matrix())            
                
                
    
            
    