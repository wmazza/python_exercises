# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a 
# combination of years, days, hours, 
# minutes and seconds.

# It is much easier to understand with an example:

# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of 
# time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it 
# would be written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 
# year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
# Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

def separator(flags, index_flag):
    prev = flags[0:index_flag]
    foll = flags[index_flag + 1:]
    
    print(prev, foll)
    
    if 1 in prev and 1 in foll:
        return ', '
    elif 1 in prev and 1 not in foll:
        return ' and '
    elif 1 not in prev and 1 not in foll:
        return ''
    elif 1 not in prev and 1 in foll:
        return ''


    
def plural(value):
    if value > 1:
        return 's'
    else:
        return ''

def format_duration(seconds):
    result = ''
    flags = [0, 0, 0, 0, 0]
    days = 0
    years = 0
    hours = 0
    minutes = 0
    updated_seconds = seconds
    
    # Years
    if updated_seconds >= 31536000:
        years = int(updated_seconds / 31536000)
        updated_seconds = updated_seconds - years * 31536000
        flags[0] = 1
        
    # Days
    if updated_seconds >= 86400:
        days = int(updated_seconds / 86400)
        updated_seconds = updated_seconds - days * 86400
        flags[1] = 1
    
    # Hours
    if updated_seconds >= 3600:
        hours = int(updated_seconds / 3600)
        updated_seconds = updated_seconds - hours * 3600
        flags[2] = 1
    
    # Minutes
    if updated_seconds >= 60:
        minutes = int(updated_seconds / 60)
        updated_seconds = updated_seconds - minutes * 60
        flags[3] = 1
        
    # Seconds
    if updated_seconds > 0:
        flags[4] = 1
    
    result += flags[0] * (str(years) + ' year' + plural(years))
    result += flags[1] * (separator(flags, 1) + str(days) + ' day' + plural(days))
    result += flags[2] * (separator(flags, 2) + str(hours) + ' hour' + plural(hours))
    result += flags[3] * (separator(flags, 3) + str(minutes) + ' minute' + plural(minutes))
    result += flags[4] * (separator(flags, 4) + str(updated_seconds) + ' second' + plural(updated_seconds))


    return result 

print(format_duration(3609999990))

