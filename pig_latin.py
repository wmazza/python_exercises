# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

import string 

def pig_it(text):
    words = text.split(' ')
    result = []
    for word in words:
        if word in string.punctuation:
            result.append(word)
        else:
            temp_word_list = list(word)
            temp_latin_word = ''
            
            temp_latin_word = ''.join(temp_word_list[1:]) + str(temp_word_list[0]) + 'ay'
            result.append(temp_latin_word)
        
    print(' '.join(result))
    
pig_it('Pig latin is cool !')