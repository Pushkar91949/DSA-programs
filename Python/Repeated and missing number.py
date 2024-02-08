def repeatedNumber(A):
    n = len(A)
    uniqueEle = set()
    tsum = (n*(n+1))//2
        
    sumA = 0
    repeat = 0
    missing = 0
        
    for num in A:
        if num in uniqueEle:
            repeat = num
        uniqueEle.add(num)
        sumA += num
    uniqueSum = sumA - repeat
    missing = tsum - uniqueSum
    return repeat, missing
            
A = (3,1,2,5,3)

print(repeatedNumber(A))