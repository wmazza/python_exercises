# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

# Test examples:

# "EBG13 rknzcyr." -> "ROT13 example."

# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

import re

input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'


def rot13(message):
    list_message = list(message)
    new_message = ''
    
    for c in list_message:
        if re.match('[a-z]|[A-Z]', c):
            i = input.index(c)
            new_message += output[i]
        else:
            new_message += c
            
    return new_message

print(rot13("This is my first ROT13 excercise!"))