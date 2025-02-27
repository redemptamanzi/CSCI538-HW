# Author: Redempta Manzi & Brian Schumitz

# Question: 

# Write a program to solve instances of the Post Correspondence Problem.  
# Your program should take as input a text file where each line specifies a new domino type,
# as well as a command-line argument n, the maximum domino limit (so your program doesn’t run forever).  
# Here is an example input file:
# ab abab
# b a
# aba b
# aa a

# Solution

import sys
from itertools import product 
    
def load_input_dominoes(inputfilename):
    """
    - Load input dominos,
    - Make sure that all dominoes have the correct format: contains exactly two strings.
    """
    dominoes = []
    with open(inputfilename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            parts = line.strip().split()
            if len(parts) != 2:
                # Chech the format of the input dominos
                print(f"Error: Check your domino format {line_number}: '{line.strip()}'")
                sys.exit(1)
            dominoes.append(tuple(parts))
    return dominoes

def valid_pcp_solution_check(dominoes, sequence): # valid_pcp_solution_check within a given sequence of dominos
    top = "".join(dominoes[i][0] for i in sequence)
    bottom = "".join(dominoes[i][1] for i in sequence)
    return top == bottom

def find_pcp_solution(dominoes, maximum_domino_limit): #Find the pcp solution given input dominos and maximum_domino_limit
    num_dominoes = len(dominoes)
    for length in range(1, maximum_domino_limit + 1):
        for sequence in product(range(num_dominoes), repeat=length):
            if valid_pcp_solution_check(dominoes, sequence):
                return [dominoes[i] for i in sequence]
    
    return None

if len(sys.argv) != 3: # Ensures the lenght of the commad to run the script (script file name, input file and maximum_domino_limit)
    print("Plese use the correct command to run the script!")
    sys.exit(1)

inputfilename, maximum_domino_limit = sys.argv[1], int(sys.argv[2])
dominoes = load_input_dominoes(inputfilename)
solution = find_pcp_solution(dominoes, maximum_domino_limit)

if solution:
    for top, bottom in solution:
        print(f"{top} {bottom}")
    
else:
    print("No solution found within the given dominos.")

