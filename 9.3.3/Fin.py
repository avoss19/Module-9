# Engineering 2 9.3.3
# Imports python projects (calc, Euler1, Euler6, Euler17)
# Created by Andrew Voss

# spacer
sp = "-" * 40

# choose project
print sp
x = raw_input("""What task do you want to preform?
1. Calculator
2. Euler 1
3. Euler 6
4. Euler 17
5. What is a Euler?
%s
> """ % sp)

# Import and run chosen project
if x == "1":
    import Calc
    dir(Calc)
    exit()

if x == "2":
    import Euler1
    dir(Euler1)
    exit()

if x == "3":
    import Euler6
    dir(Euler6)
    exit()

if x == "4":
    import Euler17
    dir(Euler17)
    exit()

if x == "5":
    print sp
    print """To find out about Euler go to:
https://projecteuler.net/about"""

else:
    print "Error: a number 1-4 was not entered"
