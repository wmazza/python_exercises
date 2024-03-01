# <!-- Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.

# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False -->


def valid_braces(string):
  list_p = []
  for p in string:
    match p:
      case '{' | '(' | '[':
        list_p.append(p)
      case '}':
        if list_p and list_p[-1] == '{':
          #list_p.remove('{')
          list_p.pop()
        else:
          return False
      case ')':
        if list_p and list_p[-1] == '(':
          #list_p.remove('(')
          list_p.pop()
        else:
          return False
      case ']':
        if list_p and list_p[-1] == '[':
          #list_p.remove('[')
          list_p.pop()
        else:
          return False
  
  if len(list_p) == 0:
    return True
  else:
    return False
        
          
      
  

print(valid_braces(''))