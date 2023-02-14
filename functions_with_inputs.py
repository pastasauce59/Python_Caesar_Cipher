# PYTHON FUNCTIONS WITH INPUTS / ARGUMENTS / PARAMETERS

# def my_function(a, b , c):
    # DO THIS WITH a
    # THEN DO THIS WITH b
    # FINALLY DO THIS WITH c


#POSITIONAL ARGUMENTS VS. KEYWORD ARGUMENTS

#POSITIONAL ARGUMENTS WILL CALLED IN THE ORDER THEY ARE PLACED WHILE KEYWORD ARGUMENTS ARE PARAMETERS
#ADDED WITH THE ARGUMENT KEYWORD AND CAN BE CALLED IN ANY ORDER.

#EXAMPLE

def my_function(a, b, c):
    print(f"This is {a}")
    print(f"Then this is {b}")
    print(f"Finally this is {c}")

my_function(c=2, a=1, b=3)
#The parameters are out of the order they are originally placed in the function but are specified what each parameter should equal.

print(73 % 4)