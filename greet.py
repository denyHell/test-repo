import sys




def greet(who):
    greeting = 'Hello, {}'.format(who)
    return greeting


print(greet('World'))
print(greet('Ryan'))

name = input("Your Name?")
print("Hello,", name)
