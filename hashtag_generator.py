# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


def generate_hashtag(s):
    if not s:
        return False
    else:
        result = '#'
        words = [x for x in s.strip().split(' ') if x != '']
        
        for word in words:
            result = result + word[0].upper() + word[1:].lower()
        
        if len(result) <= 140:
            return result
        else:
            return False


print(generate_hashtag('Hello           World!'))
print(generate_hashtag(' Hello there thanks for trying my Kata'))