from index import n,coefficientmatrix,rhscolumn,listdifference,backsubstitution

def partialpivotion(coefficientatrix):
    global bvector
    for k in range(n):
        reqcoeff=coefficientatrix[k][k]
        rowswitchindex=k

        for (comparedrow,l) in enumerate([coefficientmatrix[f][k] for f in range(k+1,n)]):
            if abs(l)>abs(reqcoeff):rowswitchindex=comparedrow+k+1;reqcoeff=l;continue
        
        coefficientatrix[k],coefficientatrix[rowswitchindex]=coefficientatrix[rowswitchindex],coefficientatrix[k]
        bvector[rowswitchindex],bvector[k]=bvector[k],bvector[rowswitchindex]
        pivotrow=coefficientmatrix[k];pivotelement=pivotrow[k]

        #There is very little prospect that after the partialpivotion above, the pivot element is still 0.
        if pivotelement==0:
            print(k)
            coefficientatrix[k],coefficientatrix[k+1]=coefficientatrix[k+1],coefficientatrix[k]
            pivotrow=coefficientatrix[k];pivotelement;pivotrow[k];
            bvector[k],bvector[k+1]=bvector[k+1],bvector[k];continue


        #Normalization via pivot elements, Subtraction of matrices' rows
        for m in range(k+1,n):
            rtc=coefficientatrix[m]
            smpivotrow=[((a*rtc[k])/pivotelement) for a in pivotrow]
            
            coefficientatrix[m]=listdifference(rtc,smpivotrow);bvector[m]-=((bvector[k]*rtc[k])/pivotelement) 
    
    print(f"The result of partially pivoted dynamic triangularization is: \n{coefficientatrix} with the new B-vector being: {bvector}")
    return coefficientatrix



        
bvector=rhscolumn;U=partialpivotion(coefficientmatrix);solutionsdictionary=backsubstitution(U)
print(solutionsdictionary)