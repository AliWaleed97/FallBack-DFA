import argparse
class DFA:
    def __init__(self):
        self.states = []
        self.lang = []
        self.initialState = ""
        self.finalStates = []
        self.transitions = []
        self.stateExpression = {}
        self.expressionAction = {}

    def display(self):
        print ("states: ", self.states)
        print ("lang: ", self.lang)
        print ("start state: ", self.initialState)
        print ("final states: ", self.finalStates)
        print ("transitions: ", self.transitions)
        print ("stateExpression: ", self.stateExpression)
        print ("expressionAction: ", self.expressionAction)

def readInput(pathDFA,pathInput):
    dfa = DFA()
    inputDFA = open(pathDFA,'r')
    inputDFA = inputDFA.read().splitlines()
    dfa.states = inputDFA[0].split(', ')
    dfa.lang = inputDFA[1].split(', ')
    dfa.initialState = inputDFA[2].strip()
    dfa.finalStates = inputDFA[3].split(', ')
    transitions = inputDFA[4].replace(", ,",",e,")
    transitions = transitions.replace(" ","")
    transitions = transitions.replace("e"," ")
    transitions = transitions.replace("),(",")-(")
    transitions = transitions.replace("(","")
    transitions = transitions.replace(")","")
    transitions = transitions.split("-")
    for transition in transitions:
        transition = transition.split(',')
        dfa.transitions.append((transition[0],transition[1],transition[2]))

    transitions = inputDFA[5]
    transitions = transitions.replace("), (",")-(")
    transitions = transitions.replace("(","")
    transitions = transitions.replace(")","")
    transitions = transitions.split("-")
    new_transitions = []
    for transition in transitions:
        transition = transition.split(", ")
        dfa.stateExpression[transition[0]] = transition[1]

    transitions = inputDFA[6]
    transitions = transitions.replace("), (",")-(")
    transitions = transitions.replace("(","")
    transitions = transitions.replace(")","")
    transitions = transitions.split("-")

    new_transitions = []
    for transition in transitions:
        transition = transition.split(", ")
        dfa.expressionAction[transition[0]] = transition[1]
    
    dfa.display()
    inputString = open(pathInput,'r').readline()
    return dfa,inputString

def fallbackDFA(pathDFA,pathInput):
    dfa,inputString = readInput(pathDFA,pathInput)
    print(inputString)
    currentString = ''
    acceptString = ''
    currentState = dfa.initialState
    for char in inputString:
        for transition in dfa.transitions:
            if (transition[0] == currentState) and (transition[1] == char):
                if(transition[2] != 'DEAD'):
                    currentString += char
                    currentState = transition[2]
                    if(transition[2] in dfa.finalStates):
                        acceptString = currentString
                else:
                    if(len(acceptString) > 0):
                        print(acceptString)
                        inputString = inputString[len(acceptString):]
                    else:
                        return
                
                    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')
    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="+",metavar="file")
    args = parser.parse_args()
    fallbackDFA(args.file[0],args.file[1])


