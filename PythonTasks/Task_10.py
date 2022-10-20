#Create an anonymous function that prints out "Hello World"

#Invoke/call the function

greet = lambda : print("Hello World")

greet()

def invoke(cb):
    cb("Hello world")

hello = lambda : print("Hello world")
hello()

invoke(lambda x: print(x))