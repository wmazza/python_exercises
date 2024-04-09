# Create a function that takes a positive integer and returns the next bigger number that can be formed 
# by rearranging its digits. For example:

#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

#   9 ==> -1
# 111 ==> -1
# 531 ==> -1


def next_bigger(n):
    digits = list(str(n))
    l = []
    #print(digits[len(digits) - 1])
    
    for i in range(len(digits) - 1, 0, -1):
        current_digit = digits[i]
        print('i ' + str(i), current_digit)
        
        for k in range(0, i):
            print('k ' + str(k), digits[k])
            new_digits = digits[:]
            new_digits[i] = digits[k]
            new_digits[k] = digits[i]          
                        
            new_n = int(''.join(new_digits))
            print(n, new_n)
            if new_n > n:
                l.append(new_n)
    
    if l:
        return min([x - n for x in l]) + n
    else:
        return -1

print(next_bigger(144))
print(next_bigger(12))
#print(next_bigger(531))
#print(next_bigger(2017))