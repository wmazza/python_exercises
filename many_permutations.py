# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

# Create as many "shufflings" as you can!

# Examples:

# With input 'a':
# Your function should return: ['a']

# With input 'ab':
# Your function should return ['ab', 'ba']

# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']

# With input 'aabb':
# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# Note: The order of the permutations doesn't matter.

def permutations(s):
    if len(s) == 1:
        return s
    
    list_combinations = [s]
    
    for i in range(len(s)):
        s2 = s[i:] + s[0:i]
        if s2 not in list_combinations:
            list_combinations.append(s2)
        for k in range(len(s)):
            if k == i:
                pass
            new_s = list(s)
            temp = new_s[k]
            new_s[k] = new_s[i]
            new_s[i] = temp
            
            new_s_str = ''.join(new_s)
            if new_s_str not in list_combinations:
                print('i, k :', i, k, 'Appending: ', new_s_str)
                list_combinations.append(new_s_str)
            #print(list_combinations)
               
    return list_combinations

print(permutations('aabb'))