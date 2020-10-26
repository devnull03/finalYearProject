# 
# EXAMPLE_FILE : 
#     Path to the file that will be 
#     sent to the players as a reference program
# 
# SOLUTION_FILE :
#     Path to the file that contains a working solution,
#     which will be used to test player's functions
# 
# TEST_CASES :
#      Path to the file that contains all the testcases
# 

# Server files ------------------------------------

EXAMPLE_FILE = "C:\\Users\\Dell\\OneDrive\\Desktop\\test_files\\example.py"
SOLUTION_FILE = "C:\\Users\\Dell\\OneDrive\\Desktop\\test_files\\check.py"
TEST_CASES = "C:\\Users\\Dell\\OneDrive\\Desktop\\test_files\\test_cases.py"

#--------------------------------------------------

# 
# MODE :
#     There is currently only one option, i.e. Shortest
# TIME :
#     The amount of time availabe for players to write their code
# TASK :
#     Description of the challenge, i.e. explanation the players 
#     how to solve the challenge
# EXAMPLES :
#     examples to be shown on player's screen in the format
#     " solution(<input>)-> <output> ", which have to be in a 
#     dictionary, i.e. { <input>: <output>, <input>: <output> }
#

# Challenge Info ----------------------------------

MODE = "Shortest"
TIME = 10
TASK = "test task"*10

# Maximum 3 examples 
EXAMPLES = {
    1: 1,
    2: 4,
    3: 9
}

#--------------------------------------------------
