# The goal of this question is to write a software library that accepts 2 version
#  string as input and returns whether one is greater than, equal, or less than
#  the other. As an example: “1.2” is greater than “1.1”.
#  Please provide all test cases you could think of.
def compareNums(a,b):
    if a==b:
        return '=='
    elif a>b: return '>'
    else: return '<'

def versionCompare(v1, v2):
    if len(v1)==0 or len(v2)==0: return 'Invalid version'
    v1Arr = v1.split('.')
    v2Arr = v2.split('.')
    
    v2Len = len(v2Arr)
    v1Len = len(v1Arr)
    minLen = min(v1Len, v2Len)
    
    for i in range(minLen):
        if(int(v1Arr[i])>int(v2Arr[i])):
            return '>'
        elif(int(v1Arr[i])<int(v2Arr[i])):
            return '<'
        if i == minLen - 1 and int(v1Arr[i])==int(v2Arr[i]):
            return compareNums(v1Len, v2Len)

def compareToString(v1, v2):
    return v1 + ' ' + versionCompare(v1, v2) + ' ' + v2

print(compareToString("", ""))
print(compareToString("0", "1"))
print(compareToString("0.1", "0"))
print(compareToString("0.1", "0.1.1"))
print(compareToString("1.2", "0.1"))
print(compareToString("1.2.3", "1.2.3.1"))
print(compareToString("0.0.1", "0.0.0"))
# still works for negative numbers, even though they aren't exactly valid version numbers
print(compareToString("-1.2", "-3.4"))
print(compareToString("18.200.99999999", "18.200.99999999"))
print(compareToString("18.200.99999998", "18.200.99999999"))
print(compareToString("18.200.99999998", "18.200.999996"))

print(-1>-3)
