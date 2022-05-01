
def listdifference(list2,list1):
    difference=[]
    for (index,value) in enumerate(list2):difference+=[list2[index]-list1[index]]
    return difference



def backsubstitution(U):
    '''
    Docstring for backpropagation of variables: 
    x(k) = (b(k)-sigma(a([k][k+1 to n])*x(k+1 to n)))/a([k][k]) 
    As derived from 1-dimensional equation obtained via substition of x(k+1 to n) in the coeffs., a
    '''
    def sigma_coeffs(list1,list2):
        summation=0
        for (i,v) in enumerate(list1):product=v*list2[i];summation+=product
        return summation

    global rhscolumn;cres_x=[]
    for l in range(n-1,-1,-1):
        cres_a=U[l][(l+1):]
        x=(rhscolumn[l]-sigma_coeffs(cres_a,cres_x))/U[l][l]
        cres_x=[x]+cres_x
    return cres_x



#Input the equations and structure them into suitable variables
n=int(input("Enter the number of linear equations(equal unknowns) in your system: "))

coefficientmatrix,rhscolumn=[],[]
for i in range(n):
    sample_str,row_='',[]
    row_string=input("Enter the co-efficients of unknowns in order: ")
    rhscolumn+=[int(input("Enter the RHS element for the coefficients aforementioned:"))]
    for j in row_string:
        if j==",": row_.append(eval(sample_str));sample_str=''
        else: sample_str+=j;continue

    row_.append(eval(sample_str));coefficientmatrix.append(row_)

