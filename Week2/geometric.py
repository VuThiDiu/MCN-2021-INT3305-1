import math

def prob(n: int, p: float) ->float:
    return p * pow((1-p),(n-1));

def infoMeasure(n, p):
    return -(math.log(prob(n,p))/math.log(2))

def sumProb(N, p):
    '''
    sumProb có thể kiểm chứng tổng xác suất của phân bố geometric bằng 1.

    '''
    total=  0;
    for item in range(1,N+1):
        total+=prob(item,p);
    return total;

def approxEntropy(N, p):
    '''
    Hàm approxEntropy  tính xấp xỉ  Entropy của nguồn tin geometric.
    Ta có : 
    '''
    sum = 0;
    for  i  in range(1, N+1):
        sum +=prob(i,p) * infoMeasure(i,p);
    return sum;

print(approxEntropy(100, 0.5));


