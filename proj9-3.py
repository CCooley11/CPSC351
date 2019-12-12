# Names: Connor Cooley, Donovan Farar, Timothy Rodriguez
# File name: proj9-3.py
# Language and Version: python version 3.7.1
# To run: python proj9-3.py
# Make sure to surround input with quotes

def function_q1(string, index, currentState):
    if index >= len(string):
        currentState = 7
        finish(currentState)
    elif (string[index] == '0'):
        string[index] = ' '
        index = index + 1
        function_q2(string, index, currentState)
    else:
        index = index + 1
        currentState = 7 # 7 is reject
        finish(currentState)
    return
    
def function_q2(string, index, currentState):
    currentState = 2
    if index >= len(string):
        currentState = 7
        finish(currentState)
    elif(string[index] == '0'):
        string[index] = 'x'
        index = index + 1
        function_q3(string, index, currentState)
    elif string[index] == 'x':
        index = index + 1
        function_q2(string, index, currentState)
    elif string[index] == ' ':
        index = index + 1
        currentState = 6
        finish(currentState)
    else:
        currentState = 7
        finish(currentState)
    return
    
def function_q3(string, index, currentState):
    currentState = 3
    if index >= len(string):
        currentState = 7
        finish(currentState)
    elif string[index] == '0':
        index = index + 1
        function_q4(string, index, currentState)
    elif string[index] == 'x':
        index = index + 1
        function_q3(string, index, currentState)
    elif string[index] == ' ':
        index = index - 1
        function_q5(string, index, currentState)
    else:
        currentState = 7
        finish(currentState)
    return
    
def function_q4(string, index, currentState):
    currentState = 4
    if index >= len(string):
        currentState = 7
        finish(currentState)
    elif string[index] == '0':
        string[index] = 'x'
        index = index + 1
        function_q3(string, index, currentState)
    elif string[index] == 'x':
        index = index + 1
        function_q4(string, index, currentState)
    elif string[index] == ' ':
        index = index + 1
        currentState = 7
        finish(currentState)
    else:
        currentState = 7
        finish(currentState)
    return

def function_q5(string, index, currentState):
    currentState = 5
    if index >= len(string):
        currentState = 7
        finish(currentState)
    elif string[index] == '0' or string[index] == 'x':
        index = index - 1
        function_q5(string, index, currentState)
    elif string[index] == ' ':
        index = index + 1
        function_q2(string, index, currentState)
    else:
        currentState = 7
        finish(currentState)
    return  
             
def finish(currentState):
    if currentState == 6:
        print("Accept")
    else:
        print("Reject")
    return

def main():
    currentState = '1'
    index = 0
    inputString = input("Enter your string surrounded by quotes: ")
    if inputString == "quit":
        exit()
    else:
        string = list(inputString)
        string.append(" ")
        function_q1(string, index, currentState)
        main()

main()