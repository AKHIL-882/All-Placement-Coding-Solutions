def getDistance(word):
    keyword = [
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", " "],
                [" ", "Z", "X", "C", "V", "B", "N", "M", " ", " "]
    ]
    set_ = {}
    for i, j in enumerate(keyword):
        for l, k in enumerate(j):
            set_[k] = (i, l)
    
    ini = set_["Q"]
    result = 0
    for i in word:
        j = set_[i]
        result += abs(ini[0] - j[0]) + abs(ini[1] - j[1])
        ini = j 
    
    return result

print(getDistance("QZ"))
print(getDistance("QA"))
print(getDistance("HELLO"))