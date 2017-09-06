def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#can rewrite (*args with this)
def print_two_agian(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#with one argument
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_agian("Zed", "Shaw")
print_one("First!")
print_none()
