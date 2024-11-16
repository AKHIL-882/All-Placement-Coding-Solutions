def getResult(A, B, N):
    if A > B:
        A, B = B, A

    result = 0
    while max(A,B) <=N:
        A , B = B , A + B
        result+=1
        
    return result
    

userInput = [int(n) for n in input().split()]
result = getResult(userInput[0], userInput[1], userInput[2])
print(result)

