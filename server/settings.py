import os
# cwd = os.getcwd()
# if not cwd.endswith('\\server'):
#     os.chdir(f"{cwd}\\server")

# # EXAMPLE_FILE : 
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
PRESET = 'Treasure'

# Server files ------------------------------------
folder = os.getcwd().rstrip('\\server') + "\\test_files"
if PRESET:
    folder = presets[PRESET]

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
#     how to solve the challenge.
# EXAMPLES :
#     examples to be shown on player's screen in the format
#     " solution(<input>)-> <output> ", which have to be in a 
#     dictionary, i.e. { <input>: <output>, <input>: <output> }
#
#     If you choose a preset, TASK and EXAMPLES will automatically be 
#     imported according to the preset
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

if PRESET:
    from presets import info
    TASK = info.INFO[PRESET]['TASK']
    EXAMPLES = info.INFO[PRESET]['EXAMPLES']

#--------------------------------------------------
