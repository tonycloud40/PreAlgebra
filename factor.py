import math
import numpy as np
import sympy


"""
The goal of this function is return the middle point to iterate 
over a set of number to calculate the factors and Prime numbers and Composite numbers
Once the quotient is smaller than the divisor then stop the process
For smaller numbers no big deal but for huge numbers it will save a lot of time
This is a limitation to the number of recursive level which around 952 levels
"""
def getMiddle(dividend, d, previous, bottom):
    if dividend==1:
        return dividend
    if d==0:
        previous = dividend
        divisor = math.ceil(dividend / 2)
    else:
        previous = d
        if bottom:
            divisor = math.ceil(d + 1)
        else:
            divisor = math.ceil(d / 2)

    if divisor==1:
        result=dividend
    else:
        #print("dividend {} / divisor {}".format(dividend, divisor))
        quotient = dividend/divisor
        if quotient>=divisor:
            result=getMiddle(dividend, divisor, previous, True)
        else:
            if bottom==False:
                result=getMiddle(dividend, divisor, previous, False)
            else:
                result=previous+1
    return result

def getFactors(nIt):
    maxIteration = getMiddle(nIt, 0, 0, False)
    nl=[]
    for divisor in range(1,maxIteration):
        remainder = math.fmod(nIt,divisor)
        #numbers that are not divisible 
        #print(divisor)
        if remainder==0:
            quotient = nIt/divisor
            if quotient<divisor:
                break
            nl.append([divisor,quotient])

    return nl


if __name__=='__main__':
    print('Get All Factors till #>:')
    n = int(input())
    
    for nvs in range(2, n+1):
        nlist = np.array([])
        #return a [[a,b],[m,n]]
        nl = getFactors(nvs)

        #create a new array [a,b,m,n]
        #convent to integer
        na = np.concatenate((nlist,np.array(nl)),axis=None).astype(int)

        #eliminate repeatble values
        nu = np.unique(na)
    
        #convert to a ist
        nm = (nu).tolist()

        #if you need test the results, uncomment the line
        #print(sympy.isprime(nvs))
        #if sympy.isprime(nvs)==False: 
        print("#{} factors -> {} {}".format(nvs,\
                                    ','.join(str(e) for e in nm),\
                                    'Prime' if nu.size==2 else 'Composite'))
