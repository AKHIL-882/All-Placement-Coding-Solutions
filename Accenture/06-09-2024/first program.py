class UserMainCode(object):
    @classmethod
    def evensum(cls, input1, input2):
        input1 = input1[::-1]
        return sum(input1[i] for i in range(0, input2, 2))
        
    
    

input1 = [10,20,30,40,50,60]
input2 = 6
print(UserMainCode.evensum(input1, input2))

input1 = [21,24,67,13,24,27]
input2 = 6
print(UserMainCode.evensum(input1, input2))