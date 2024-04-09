# Given the string representations of two integers, return the string representation of the sum of those integers.

# For example:

# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

# I have removed the use of BigInteger and BigDecimal in java

# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.


def sum_strings(x, y):
    if not x and not y:
        return '0'
    elif not x:
        return y
    elif not y:
        return x
        
    max_len = max([len(x), len(y)])
    offset_x = max_len - len(x)
    offset_y = max_len - len(y)
    res = ['0' for x in range(max_len)]
    print (max_len, x, y)
    
    leftover = 0
    for i in range(max_len - 1, -1, -1):
        if (i - offset_x) >= 0 and (i - offset_y) >= 0:
            temp_res = int(x[i - offset_x]) + int(y[i - offset_y]) + leftover
            leftover = 0
            print('iter: ' + str(i), 'x value: ' + x[i - offset_x], 'y value: ' + y[i - offset_y], 'sum: ' + str(temp_res))
            if temp_res <= 9:
                res[i] = str(temp_res)
            else:
                res[i] = str(temp_res)[1]
                leftover = 1
        else: 
            print('in else', (i - offset_x), (i - offset_y), leftover)
            if (i - offset_x) > (i - offset_y):
                print('x', i - offset_x, x[0:i - offset_x + 1])
                res[0:i - offset_x + 1] = x[0:i - offset_x + 1]
            elif (i - offset_x) < (i - offset_y):
                print('y', y[0:i - offset_y])
                res[0:i - offset_y + 1] = y[0:i - offset_y + 1]
            
            if leftover == 1:
                temp_res = int(res[i - min(offset_x, offset_y)]) + 1
                print('temp_res', temp_res)
                
                if temp_res <= 9:
                    res[i - min(offset_x, offset_y)] = str(temp_res)
                    leftover = 0
                elif temp_res > 9:
                    res[i - min(offset_x, offset_y)] = '0'
                    for l in range(i - min(offset_x, offset_y) - 1, -1, -1):
                        print('new for', res[l])
                        if res[l] == '9':
                            print('keep going', res)
                            res[l] = '0'
                        else:
                            print('res[l]', res[l])
                            res[l] = str(int(res[l]) + 1)
                            leftover = 0
                            break
                            
                else:
                    leftover = 0
            break        
             
    if leftover == 1:   
        return '1' + ''.join(res) #(max_len, offset_x, offset_y)   
    else:
        if len(res) > 1:
            return ''.join(res).lstrip('0') #(max_len, offset_x, offset_y)   
        else:
            return ''.join(res)  

print(sum_strings('',''))
#print(sum_strings("123", "45655555"))
#print(sum_strings('2999', '302')) 
#print(sum_strings('00103', '08567'))
#print(sum_strings('9999999999999999', '1'))
