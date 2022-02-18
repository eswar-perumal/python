# variable scope
# local scope
'''a=1
def local():
    print(a)    #this variable “a” refers to the below “a” so it will throw error
    a=2
    print(a)
local()'''

#output : UnboundLocalError: local variable 'a' referenced before assignment

def local(a=1):
    print(a)    #this works fine as variable “a” defined in function definition
    a=2
    print(a)
local()

# non local scope (enclosing scope)
def red():
    a=1             # --> non local
    def blue():
        b=2         # --> local
        print(a)    # non local variable accessed here but can't edit this. to edit declare as nonlocal
        print(b)
    blue()
    print(a)
red()

def red():
    a=1
    def blue():
        nonlocal a
        a=2
        b=2
        print(a)
        print(b)
    blue()
    print(a)
red()

# global scope
a=1
def counter():
    a=2
    print(a) #this refers local variable "a" to affect this -> declare variable "a" as global
counter()
print(a)

a=1
def counter():
    global a
    a=2
    print(a) 
counter()
print(a)

# built-in scope
print(id(2))
identity = id       #here we associate the name identity with built-in function id()
print(identity(2))

def sayhello(): print("Hello")
hi=sayhello()
print(hi)
print(type(hi))

def sayhello():
    print("Hello")
    return 21
hi=sayhello()
print(hi)
print(type(hi))