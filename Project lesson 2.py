base=3
exponent=3

result=1

for exponent in range(exponent, 0, -1):
    result *= base
    exponent-=1

print("Answer = " +str(result))