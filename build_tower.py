# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. 
# A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ",  1-1 2-3 3-5 4-7 = n + (n-1) = 2n - 1
#   "  *******  ", 
#   " ********* ", 
#   "***********"
#    *****************
#    *******************
# ]

from math import floor


def tower_builder(n_floors):
    # build here
    base_num = 2 * n_floors - 1
    tower = []
    
    for i in range(n_floors):
        #print(' ' * (floor(base_num/2) - i) + '*' * (2*i + 1)) 
        tower.append(' ' * (floor(base_num/2) - i) + '*' * (2*i + 1) + ' ' * (floor(base_num/2) - i))
    
    
tower_builder(10)