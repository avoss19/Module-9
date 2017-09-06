# Project Euler
# Problem 6 - Sum square difference
# https://projecteuler.net/problem=6
# Engineering 2 9.3.2
# Created by Andrew Voss

# Create list with numbers 1-10
a = []

i = 1

while i <= 10:
    a.append(i)
    i += 1

# Create second list with numbers 1-10
b = a

# sum of "a" and square it
# The square of the sum of the first ten natural numbers
a = sum(a) ** 2

# square each number then add
# The sum of the squares of the first ten natural numbers
b = [ int(x**2) for x in b ]
b = sum(b)

print "The sum of the squares of the first 100 natural numbers is,", b
print "The square of the sum of the first 100 natural numbers is,", a
print "The difference between then is:", [a-b]
