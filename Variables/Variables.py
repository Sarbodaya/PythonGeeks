# Global Variable
# Global variables are those who are declared
# outside the function we need to use inside the function
def f():
    s = 'Me Too'
    print(s)


s = "I want to Become Data Scientist"
f()
print(s)

# If a variable with the same name is defined inside the scope of
# function as well then it will print the value given inside the
# function only and not the global value.

# The question is, what will happen if we change the value of s
# inside of the function f()? Will it affect the global s as well? We test it in the following piece of code:
# filter_none

def f():
    global s  # we have to use the keyword “global”, as can be seen in the following example:
    print(s)
    s = "Python is great"
    print(s)

# Global Scope
s = "I Love Geeks for Geeks"
f()
print(s)



