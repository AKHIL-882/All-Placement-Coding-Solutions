class UserMainCode(object):
    @classmethod
    def specialFibonacci(cls, input1):
        MOD = 47
        if input1 == 0 or input1 == 1:
            return 1
        userArray = [1,1]
        for i in range(2, input1 + 1):
            mapValue = (userArray[i-1] ** 2 + userArray[i-2] ** 2) % MOD
            userArray.append(mapValue)
            
        return userArray[input1]
    
input1 = 5
print(UserMainCode.specialFibonacci(input1))

input1 = 2
print(UserMainCode.specialFibonacci(input1))