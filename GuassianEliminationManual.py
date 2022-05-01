from index import listdifference,backsubstitution,rhscolumn,n,coefficientmatrix

def triangularizer(coefficientmatrix):
    try:
        global rhscolumn
        for k in range(n):
        
            pivotrow=coefficientmatrix[k]
            if pivotrow[k]==0:
                #Failure
                coefficientmatrix[k],coefficientmatrix[k+1]=coefficientmatrix[k+1],coefficientmatrix[k];pivotrow=coefficientmatrix[k]
                rhscolumn[k],rhscolumn[k+1]=rhscolumn[k+1],rhscolumn[k];continue
                
            for l in range(k+1,n):
                rtc=coefficientmatrix[l]

                #Normalization of pivotrow, Coeff. Equalizer
                smpivotrow=[(a*rtc[k])/pivotrow[k] for a in pivotrow]

                #Subtraction of equation to cancel the kth unknown
                coefficientmatrix[l]=listdifference(rtc,smpivotrow);rhscolumn[l]-=((rhscolumn[k]*rtc[k])/pivotrow[k])


        print(f"Result of triangularizaion:{coefficientmatrix}");print(f"New RHS Column: {rhscolumn}") 
        return coefficientmatrix    

    except ZeroDivisionError or Exception:return coefficientmatrix

        
U=triangularizer(coefficientmatrix);solutionsdictionary=backsubstitution(U)


