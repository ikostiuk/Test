def substr(string: str, begin: int, end: int) -> str:
    
    string = str(string)
    
    if type(begin) != int or type(end) != int:
        return None

    begin, end = int(begin), int(end)
    
    if begin < 1:
        begin = 1
        
    if end < 1:
        end = 1
        
    if begin > end:
        return None
        
     
    result = string[begin-1 : end]
    
    print(result) 
    return result
    
    
    
assert substr('test', 1, 4) == 'test'

assert substr('test', 2, 3) == 'es'

assert substr('test', 1, 10) == 'test'

assert substr('test', 0, 2) == 'te'

assert substr('test', 0, 0) == 't'

assert substr('', 1, 5) == ''

assert substr('test', 'te', 11) == None

assert substr('test', 2, 1) == None
