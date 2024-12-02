#++************************************************************************************************
#+ Functions as variables:
#++************************************************************************************************
#: 1.- Python decorators can extend the code to a function.
#: 2.- In Python, functions are object also, just like an integer.  To pass a function, as a
#:     variable you need to exclude the parenthesis.
#: The following example shows how you can pass a function as a variable

def addOne(x):
    print("Executing code inside addOne() function")
    return x + 1

#: The first parameter is a function
def whatToAdd(func, x):
    print("Executing code inside whatToAdd() function")
    print("--- Before triggering addOne()")
    result = func(x)
    print("--- After triggering addOne()")
    return result


#: I am going to call function whatToAdd and pass it a function called addOne without parenthesis
result = whatToAdd(addOne, 3)
print(result)

#++************************************************************************************************
#+ end of "Functions as variables"
#++************************************************************************************************

