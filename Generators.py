# fill in this function
def fib():
    a = 1
    yield a
    b = 1
    while True:
    	a, b = b, a+b
        yield a

# testing code
import types
if type(fib()) == types.GeneratorType:
    print "Good, The fib function is a generator."

    counter = 0
    for n in fib():
        print n
        counter += 1
        if counter == 10:
            break