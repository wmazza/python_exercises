# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 
# which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

def in_array(array1, array2):
    list_ret = []
    for word in array1:
        for word2 in array2:            
            if word in word2:
                list_ret.append(word)
                break
    return list_ret.sort()

a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))

print('live' in 'lively')