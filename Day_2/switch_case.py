def week(i):
    switcher={
        0:'sunday',
        1:'monday',
        2:'tuesday',
        3:'wednesday',
        4:'thursday',
        5:'friday',
        6:'saturday'
    }
    return switcher.get(i,"Invalid day of week")
print(week(4))

def zero():
    return 'zero'
def one():
    return 'one'
def indirect(i):
    switcher={
        0:zero,
        1:one,
        2:lambda:'two'
    }
    func=switcher.get(i,lambda:'Invalid')
    return func()
print(indirect(2))
print(indirect(5))