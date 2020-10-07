#phân phối nhị thức âm

import math
def binomial(n, k):
    if(k >= 0 and k <= n):
        if(k == 0 or k == n):
            return 1
        else:
            result = 1
            for i in range(1, k+1):
                result *= (n-k+i) * 1.0 / i * 1.0;
            return int(result);
    else:
        return 0;


def prob(n, p, r):
    number = binomial(n, n-r+1) * 1.0
    return number * pow(p,r) * pow(1-p,n-r+1);

def infoMeasure(n, p, r) :
    number = prob(n, p, r)
    info = -math.log2(number)
    return info


def sumProb(N, p, r):
    sum = 0.0
    for i in range(r, N + 1):
        sum += prob(i, p, r)
    return sum

def approxEntropy(N, p, r):
    entropy = 0
    for i in range(r, N + 1):
        entropy += prob(i, p, r) * infoMeasure(i, p, r)
    return entropy

