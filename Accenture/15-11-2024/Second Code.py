def getResult(n, arr):
    sum_ = 0
    count = {0:1}
    result = 0
    for i in arr:
        sum_+=i
        if sum_ in count:
            result+=1
            sum_ = 0
            count = {0:1}
        else:
            count[sum_] = 1
        
    return result
    
    
n = int(input())
userInput = [int(n) for n in input().split()]
print(getResult(n ,userInput))