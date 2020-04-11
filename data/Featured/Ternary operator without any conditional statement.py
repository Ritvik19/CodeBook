def ternaryOperator( a, b, c): 
    
    # If a is true, we return  
    # (1 * b) + (!1 * c) i.e. b 
    # If a is false, we return  
    # (!1 * b) + (1 * c) i.e. c 
    return ((not not a) * b + (not a) * c) 

if __name__ == "__main__": 
    b = 10
    c = 20
    
    a = 1
    print(ternaryOperator(a, b, c)) 

    a = 0
    print(ternaryOperator(a, b, c)) 