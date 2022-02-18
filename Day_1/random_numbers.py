# generate 4 digits random number without using random function
import imp
import time
for _ in range(4):
    time.sleep(0.2)
    print(int((time.time()*1000)%10),end='')
print()

# generate random value using random module
# random() - generates a floating-point number between 0 and 1
from random import random
print(random())

# randint() - generates an integer number between the given range Ex: (0-9)
from random import randint
print(randint(0,9))

#randrange() - generates a random number from the given range
from random import randrange
print(randrange(1,10,2))
#syntax: randrange(start, stop, step)

# sample() - generates unique random numbers within the given range of numbers
from random import sample
print(sample(range(1,51),15))

# choice() – picks a random value from our own custom list
from random import choice
lst=['hi','hello','bye']
print(choice(lst))

# choices() – picks multiple random value from our own custom list
from random import choices
lst=['hi','hello','welcome','bye']
print(choices(lst,k=3)) #k=3, choose 3 randomw values from list nut not unique values(may duplciate occurs)

# shuffle() – shuffling a list randomly
from random import shuffle
lst=['hi','hello','welcome','bye']
shuffle(lst)
print(lst) #print list after shuffle

# seed()- It helps to generate the same random value again and again.
from random import seed, randint
seed(21)
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9))

# rand() – Generate random number using NumPy
from numpy.random import rand
print(rand(3))