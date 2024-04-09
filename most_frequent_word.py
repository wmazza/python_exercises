# Write a function that, given a string of text (possibly with punctuation and line-breaks), 
# returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
# Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
# Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, 
# or an empty array if a text contains no words.
# Examples:
# "In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income."

# --> ["a", "of", "on"]


# "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

# --> ["e", "ddd", "aa"]


# "  //wont won't won't"

# --> ["won't", "wont"]
# Bonus points (not really, but just for fun):
# Avoid creating an array whose memory footprint is roughly as big as the input text.
# Avoid sorting the entire array of unique words.


import re

def top_3_words(text):
    if not text:
        return []
    
    #exp = ''
    exp = "(?<!\w)'(?!\w)|[^\s\w\d']"
    #words = [word.lower() for word in re.sub(exp, '', text).split(' ') if word not in ['', '\'']]
    words = [word for word in re.sub(exp, '', text.lower()).split(' ') if word != '']
             
    res = {}
    for word in words:
        if word not in  res:
            res[word] = 1
        else:
            res[word] += 1
    print(res)
    
    i = 0
    max_3 = []
    while i != 3:
        if res:
            max_temp = max(res, key=res.get)
        # print(max_temp)
        # if not max_temp:
        else:
            break
        max_3.append(max_temp)
        res.pop(max_temp)
        
        i += 1
    
    return max_3


print(top_3_words(" %    '   //wont Won't won't"))
print(top_3_words("qEre/_/;qEre .:.Ogp'qXWBS-_--:Ogp'qXWBS:-!/Ogp'qXWBS/,;,VzkfE-qEre!.;Ogp'qXWBS/.;Ogp'qXWBS:: qEre_Ogp'qXWBS-Ogp'qXWBS_!!!VzkfE-:!;Ogp'qXWBS_?Ogp'qXWBS_:!Ogp'qXWBS;Ogp'qXWBS/Ogp'qXWBS?.Ogp'qXWBS?.;Ogp'qXWBS/;!,qEre Ogp'qXWBS_/.Ogp'qXWBS._ Ogp'qXWBS?__,Ogp'qXWBS?,--:Ogp'qXWBS!--/Ogp'qXWBS;!Ogp'qXWBS;-"))