#++************************************************************************************************
#+ Assigning a function to a variable:
#++************************************************************************************************
#: 1.- Because functions are also variables, you can assign a function to a variable

def add(x,y):
    return x + y

sumar = add
#: This is the same as calling add
print(sumar(1,2))


#++************************************************************************************************
#+ Wrapper function:
#++************************************************************************************************
#: Since we can pass functions as parameters, then we can build a wrapper that accepts a function
#: as a parameter and returns a function
def wrapper(f):
    return f(2,3)

print(wrapper(sumar))
print(wrapper(add))
print(type(wrapper))
print('\n\n\n\n\n')


#++************************************************************************************************
#+ Functions that define functions:
#++************************************************************************************************
#: A function can define another function
def wrapper2():
    x = 2
    def add2(x,y):
        return x+y
    return add2

segundo = wrapper2()
print(f'memory address for segundo is [{segundo}]')
print(f'memory address for wrapper2 is [{wrapper2}]')
