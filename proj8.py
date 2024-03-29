#Connor Cooley and Donovan Farar
#proj8.py
#python version 3.7.1


def simulatePDA(myString):
    # val = input("Enter your value: ") 
    # print(val) 
    # stackString = ""
    
    # Q = {1, 2, 3, 4}
    # Sigma = {'0', '1'}
    # Stackabet = {'$', 'Z'} #Z fpr zero
    # AcceptStates = {'1', '4'}
    # startState = {'1'}
    currentState = '1'
    stack_list = []
    item = ''
    i = 0 # keep track of what current character we are looking at in myString
	
    while(i != len(myString)):
        if(currentState == '3' and myString[i] == '0'): # make sure to pop after this executes
            return "false"
        if(currentState == '1'):
            item = '$'
            stack_list.append(item); # concat $ onto stack string
            currentState = '2'
        elif(currentState == '2' and myString[i] == '0'):
            item = '0'
            stack_list.append(item)
            currentState = '2'
            i = i + 1
        elif(currentState == '2' and myString[i] == '1' and stack_list[len(stack_list) - 1] == '0'): # make sure to pop after this executes
            stack_list.pop()
            currentState = '3'
            i = i + 1
        elif(currentState == '2' and myString[i] == '1' and not stack_list[len(stack_list) - 1] == '0'): # make sure to pop after this executes
            return "false"
        elif(currentState == '3' and myString[i] == '1' and stack_list[len(stack_list) - 1] == '0'):
            stack_list.pop()
            currentState = '3'
            i = i + 1
        if(currentState == '3' and stack_list[len(stack_list) - 1] == '$'): # make sure to pop after this executes
            stack_list.pop()
            currentState = '4'
              
    stuff = "false"
    if(currentState == '1' or currentState == '4'):
        stuff = "true"
  
    return stuff   
  

stringToTest = 1
while (stringToTest == 1):
    myString = str(raw_input("Enter your string: "))  
    if not myString:
        print("true")
    else:
        result = simulatePDA(myString)
        print(result)

    stringToTest = int(input("Would you like to test another string? Enter '1' for yes and '0' fo no: "))