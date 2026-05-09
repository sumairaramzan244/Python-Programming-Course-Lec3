#   variaables

year = int(2447)
month = str("June")
day = float(24.0)

print(year)
print(month)
print(day)

# find types of variables 

print(type(year))
print(type(month))
print(type(day))


# camel case is a naming convention in which the first letter of each word in a compound word is capitalized, except for the first word. For example, "myVariableName" is an example of camel case. It is commonly used in programming languages to improve readability and distinguish variable names from other types of identifiers.
myVariableName = "Name"
print(myVariableName)



# pascal case is a naming convention in which the first letter of each word in a compound word is capitalized, including the first word. For example, "MyVariableName" is an example of pascal case. It is also commonly used in programming languages, especially for naming classes and types.
pascal_Var= "  Remember this is pascal case"
print(pascal_Var)


#  snake case is a naming convention in which words are separated by underscores (_) and all letters are typically lowercase. For example, "my_variable_name" is an example of snake case. It is commonly used in programming languages, especially for naming variables and functions.
six_class= " GA 6 class is the best class"
print(six_class)


# data types are the classification of data that tells the computer how to interpret and manipulate the data. In programming, there are several common data types, including:

# 1. Integer: A whole number without a decimal point. For example, 42, -5, and 0 are integers.

x,y,z = "cat", "dog", "bird"
# print all the variables in one print statement by separating them with commas. The print function will automatically add a space between the values when printing them. 

print(x,y,z)

# print line by line by using multiple print statements for each variable. This will print each variable on a new line.
print(x)
print(y)
print(z)


# unpacking is a feature in Python that allows you to assign values from a collection (like a list or tuple) to multiple variables in a single line of code. This can make your code more concise and easier to read. For example, if you have a list of three items, you can unpack them into three separate variables like this:


# list is with big brackets [] and tuple is with small brackets () and set is with curly brackets {} and dictionary is with curly brackets {} but it has key value pairs

flowers = ["rose", "lily", "tulip" ,"sunflower"]

a,b,c ,d= flowers

print(a)
print(b)
print(c)
print(d)



# output variables are the variables that store the result of a computation or a function. They are used to hold the output of a program or a specific operation, which can then be used for further processing or displayed to the user. For example, if you have a function that calculates the sum of two numbers, the result can be stored in an output variable for later use.

x1= 5
y1= 10
sum = x1 + y1
print("The sum of", x1, "and", y1, "is", sum)

# + operator is used for concatenation of strings and addition of numbers. When used with strings, it combines them together. When used with numbers, it adds them together.

x2="she is"
y2="a good student"
z3="in her class"

print(x2 + " " + y2 + " " + z3)


#  global variables are variables that are defined outside of any function and can be accessed and modified from anywhere in the program. They have a global scope, meaning they can be used throughout the entire program, including inside functions. Global variables are typically declared at the top of a program and can be accessed by any function or block of code within the program.

globalsVar="This is a global variable"
def my_func():
    globalsVar= "This is a local variable"         
    #  it is not a global variable because it is defined inside the function and it can only be accessed within that function. It is a local variable because it is defined within the scope of the function and cannot be accessed outside of it.
    print(globalsVar) 
    #  print the local var not global 
my_func() 


globalsVar1="This is a global variable"
def my_func():
    globalsVar= "This is a local variable"         
    print(globalsVar) 
my_func() 
print(globalsVar1)


#  global method is a built-in function in Python that allows you to access and modify global variables from within a function. It is used to declare that a variable inside a function is global, meaning it can be accessed and modified outside of the function as well.

def secoind_func():
    global globalsVar2
    globalsVar2 = "This is a modified global variable"
    # print(globalsVar2)

secoind_func()
print(globalsVar2)



