def power(base, exponent):
    result = 1  
    for _ in range(abs(exponent)):  
        result *= base
    if exponent < 0:  
        result = 1 / result
    return result
base,exponent=map(int,input('Write two numbers: ').split())
print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")