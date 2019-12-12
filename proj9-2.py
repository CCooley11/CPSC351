# Names: Connor Cooley, Donovan Farar, Timothy Rodriguez
# File Name: proj9-2.py
# Language and Version: python version 3.7.1
# Instructions for execution: 
#     1. Assure that encoding.txt and proj9-2 are in the same folder
#     2. python proj9-2.py

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


states = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}; #12 is fail state, 10 is accept state
alphabet = {'0', '1'}; 

tf = dict(); 
tf[(0, '0')] = 1; 
tf[(0, '1')] = 12;
tf[(1, '0')] = 2; 
tf[(1, '1')] = 12; 
tf[(2, '0')] = 3;
tf[(2, '1')] = 12;
tf[(3, '0')] = 12;
tf[(3, '1')] = 4;
tf[(4, '0')] = 5; 
tf[(4, '1')] = 6;
tf[(5, '0')] = 11; 
tf[(5, '1')] = 6; 
tf[(6, '0')] = 5;
tf[(6, '1')] = 7;
tf[(7, '0')] = 8;
tf[(7, '1')] = 7;
tf[(8, '0')] = 9; 
tf[(8, '1')] = 7;
tf[(9, '0')] = 10; 
tf[(9, '1')] = 7; 
tf[(10, '0')] = 12;
tf[(10, '1')] = 12;
tf[(11, '0')] = 10;
tf[(11, '1')] = 4;
tf[(12, '0')] = 12;
tf[(12, '1')] = 12;
  
start_state = 0; 
accept_states = {10}; 

d = DFA(states, alphabet, tf, start_state, accept_states);

moreInput = 1;

f = open("proj9-2.txt", "r")
myString = f.read()
inp_program = list(myString); 

if((d.run_with_input_list(inp_program)) == True):
    print("Accept")
else:
    print("Reject")
