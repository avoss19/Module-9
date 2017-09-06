# This is calculator programss
# Commented lines were orginally in the code
# Engineering 9.3.3
# Created by Andrew Voss

#Spacer for easier terminal reading
sp = "-"*40


#remainder of a number (More complex Math Problem, not really tho)
#func = function
questionForFunction = "What would you like your first number to be?: "
questionForFunction2 = "What would you like your second number to be?: "
print sp
func = raw_input("What fuction do you want to preform?\n1. Additon\n2. Subtration\n3. Multiplication\n4. Division\nChoose: ") #Input Doesn't matter exept for division with remainder
print sp
if func == "1":
    firstNumber = int(raw_input(questionForFunction))
    secNumber = int(raw_input(questionForFunction2))
    functionAnswer = firstNumber + secNumber
    print sp
    print "Answer: %s" % functionAnswer
    exit(1)
if func == "2":
    firstNumber = int(raw_input(questionForFunction))
    secNumber = int(raw_input(questionForFunction2))
    functionAnswer = firstNumber - secNumber
    print sp
    print "Answer: %s" % functionAnswer
    exit(1)
if func == "3":
    firstNumber = int(raw_input(questionForFunction))
    secNumber = int(raw_input(questionForFunction2))
    functionAnswer = firstNumber * secNumber
    print sp
    print "Answer: %s" % functionAnswer
    exit(1)
if func == "4":
    divisionForm = raw_input("What form do you want your division in?\n1. Whole number Without remainder\n2. Whole number with remainder\n3. Deciamal\nChoose: ")
    print sp
    if divisionForm == "1":
        firstNumber = int(raw_input(questionForFunction))
        secNumber = int(raw_input(questionForFunction2))
        functionAnswer = firstNumber / secNumber
        print sp
        print "Answer: %s" % functionAnswer
        exit(1)
    if divisionForm == "2":
        firstNumber = int(raw_input(questionForFunction))
        secNumber = int(raw_input(questionForFunction2))
        functionAnswer = firstNumber / secNumber
        functionRemainder = firstNumber % secNumber
        print sp
        print "Answer: %d r %d" % (functionAnswer, functionRemainder)
        exit(1)
    if divisionForm == "3":
        firstNumber = float(raw_input(questionForFunction))
        secNumber = float(raw_input(questionForFunction2))
        functionAnswer = firstNumber / secNumber
        print sp
        print "Answer: %f" % functionAnswer
        exit(1)
    else:
        print "Error: You did not enter a number 1-3"
else:
    print "Error: You did not enter a number 1-4"
