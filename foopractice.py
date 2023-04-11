def foo(x, y, z=0):
    return 100*x + 10*y + 1*z
print(foo(1,2,3))
print(foo(x = 1, y = 2, z = 3))
print(foo(y = 2, x=1, z = 3))

def bar(*args):         #adding * will make object iterable
    for arg in args:
        print("bar arg = ", arg)
print(bar([1,2,3]))
print(bar(["Jelly", "Fish"]))       #will return as a list

def bar(*args, named_parameter = "bar"):         #adding * will make object iterable
    for arg in args:
        print(named_parameter, "bar arg = ", arg)
#print(bar([1,2,3]))
print(bar("Jelly", "Fish"))
print(bar("list", "of", "strings"))