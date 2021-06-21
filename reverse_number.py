
def reverse(x: int) -> int:
    if x > 0:
        negative = False
    else:
        negative = True    
    rev = int(str(abs(x))[::-1])
    if -2**31 <= rev <= (2**31) - 1:
        if negative:
            return -1*rev
        else:
            return rev
    else:
        return 0
        
        

def reverse_another(x: int) -> int:
    if x > 0:
        prefix = ''
    else:
        prefix = '-'
    x= abs(x)
    rev_num = []
    if x ==0:
        return 0
    while x>=1:
        rev_num.append(str(x%10))
        x = x//10
    result = int(prefix+''.join(rev_num))    
    if -2**31 <= result <= (2**31) - 1:
        return result
    else:
        return 0
    
print(reverse(134))
print(reverse_another(134))


print(reverse(-134))
print(reverse_another(-134))

print(reverse(-120))
print(reverse_another(-1200))
