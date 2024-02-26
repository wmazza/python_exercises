def to_camel_case(text):
    z = split_and_upper('-', text)
    w = split_and_upper('_', z)
    
    print(w)
    return w
    
def split_and_upper(char_to_split, string_word):
    
    x = string_word.split(char_to_split)   
    
    
    for i in range(1, len(x)):
        x_list = list(x[i])
        
        x_list[0] = x_list[0].upper()
        x[i] = ''.join(x_list)
    
    y = ''.join(x)
    
    return y


to_camel_case('ci-a_o')

