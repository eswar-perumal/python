a=5
b=9
result = a if a>b else b
print(result)

# other way to achieve ternary operator
a=5
b=9
res = (b,a)[a>b]
print(res)

# nested ternary operator
from random import random
a=random()
print("less than 0" if a<0 else "between 0 and 1" if a>=0 and a<=1 else "greater than 1")