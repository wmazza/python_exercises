# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

import re

def order(sentence):
  if len(sentence) == 0:
    return ''
  x = sentence.split(' ')

  temp = []
  dict_ = {}
  
  numbers = []
  for e in x:
    for i in e:       
        if i.isdigit():
            temp.append(i)
            break
    numbers.append(temp)
    temp = []
    dict_[int(i)] = e
  
  a = [0]*len(x)
  for l in range(1, len(x) + 1):
    a[l - 1] = dict_[l]
      
  return ' '.join(a)


print(order('is2 Thi1s T4est 3a'))