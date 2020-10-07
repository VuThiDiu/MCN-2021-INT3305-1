# phân phối nhị thức.
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


def prob(n, p, N):
    number = binomial(N, n) * 1.0
    q = 1 - p
    return number * pow(p,n) * pow(q,N - n);

def infoMeasure(n, p, N) :
    pr = prob(n, p, N)
    info = -math.log2(pr)
    return info


def sumProb(N, p):
    sum = 0.0
    for i in range(0, N + 1):
        sum += prob(i, p, N)
    return sum

def approxEntropy(N, p):
    entropy = 0
    for i in range(0, N + 1):
        entropy += prob(i, p, N) * infoMeasure(i, p, N)
    return entropy