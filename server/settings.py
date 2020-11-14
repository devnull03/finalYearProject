import os
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
presets_folder = os.getcwd() + "\\presets"
presets = {
    'CardTiming': f"{presets_folder}\\CardTiming",
    'Treasure': f"{presets_folder}\\Treasure"
}

# Server files ------------------------------------
folder = f"{os.getcwd().rstrip('\\server')}\\test_files"

EXAMPLE_FILE = f"{folder}\\example.py"
SOLUTION_FILE = f"{folder}\\check.py"
TEST_CASES = f"{folder}\\test_cases.py"

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

EXAMPLES = {
    1: 1,
    2: 4,
    3: 9
}

#--------------------------------------------------
