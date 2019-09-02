import sys

print(sys.version)
print(sys.executable)


def greet(who):
    greeting = 'Hello, {}'.format(who)
    return greeting


print(greet('World'))
print(greet('Ryan'))

name = input("Your Name?")
print("Hello,", name)
