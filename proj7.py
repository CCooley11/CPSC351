#Connor Cooley and Donovan Farar
#proj7.py
#python version 3.7.1
#class DFA code pulled from http://pythonfiddle.com/dfa-simple-implementation/


class DFA:
    current_state = None;
    def __init__(self, states, alphabet, transition_function, start_state, accept_states): # define DFA
        self.states = states; #"self represents instants of the Class DFA, assigning each attribute of a DFA to class DFA"
        self.alphabet = alphabet;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()): #checls to assure that input is valid
            self.current_state = None;
            return;
        self.current_state = self.transition_function[(self.current_state, input_value)];
        return;
    
    def in_accept_state(self):
        return self.current_state in accept_states;
    
    def go_to_initial_state(self):
        self.current_state = self.start_state;
        return;
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list:
            self.transition_to_state_with_input(inp);
            continue;
        return self.in_accept_state();
    pass;



states = {0, 1, 2, 3}; #0 is q0, 1 is q1 (accept state), and 2 is F, 3 is q4(also accept to account for "11")
alphabet = {'0', '1'}; 

tf = dict(); 
tf[(0, '0')] = 2; 
tf[(0, '1')] = 1;
tf[(1, '0')] = 3; 
tf[(1, '1')] = 3; 
tf[(2, '0')] = 2;
tf[(2, '1')] = 2;
tf[(3, '0')] = 0;
tf[(3, '1')] = 1;
  
start_state = 0; 
accept_states = {1, 3}; 

d = DFA(states, alphabet, tf, start_state, accept_states);

moreInput = 1;


while (moreInput == 1):
    myString = str(raw_input("Enter your string: "))
    if not myString:
        print("Accept")
    else:
        inp_program = list(myString); # should be false... input test string with parentheses 
        print(d.run_with_input_list(inp_program))

    moreInput = input("Would you like to test another string? Enter '1' for yes and '0' for no: ")