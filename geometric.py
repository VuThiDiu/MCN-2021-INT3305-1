import math

def prob(n: int, p: float) ->float:
    return p * pow((1-p),(n-1));

def infoMeasure(n, p):
    return -(math.log(prob(n,p))/math.log(2))

def sumProb(N, p):
    '''
    Tổng phân bố 
    '''
    total=  0;
    for item in range(1,N+1):
        total+=prob(item,p);
    return total;

def approxEntropy(N, p):
    '''
    Entropy = E(p(x)*l(x)) = -E(p(x)*log(px))
    Mà: approxEntropy = E(prob(x)*infoMeasure(x))
                      = -E(p(x)*log(px))
    '''
    sum = 0;
    for  i  in range(1, N+1):
        sum +=prob(i,p) * infoMeasure(i,p);
    return sum;

print(approxEntropy(100, 0.5));


