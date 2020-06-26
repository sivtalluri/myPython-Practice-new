# This program explains Args and Kwargs functionality

def myPrint(requiedParam, *args, **kwargs):   # *args we can pass varialbe like number or string, list , tuple.
                                              # *kwargs  we have to pass key value pair. like dictionary
    print(requiedParam)
    new_args = args + ('Extra', 4, 5)
    kwargs['Gender'] ='Male'
    if args:
        print(new_args)

    if kwargs:
        print(kwargs)
    print()

myPrint('Hello')
myPrint('Hello', 1, 'two', 3)
myPrint(1, name = 'Prasad', age = 43)


