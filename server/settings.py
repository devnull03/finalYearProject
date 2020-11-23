import os
# ------Code used while development------
# cwd = os.getcwd()
# if not cwd.endswith('\\server'):
#     os.chdir(f"{cwd}\\server")
# ---------------------------------------
# 
# EXAMPLE_FILE : 
#     Path to the file that will be 
#     sent to the players as a reference program
#     ( Should be named example.py )
# 
# SOLUTION_FILE :
#     Path to the file that contains a working solution,
#     which will be used to test player's functions
#     ( Should be named check.py )
#
# TEST_CASES :
#      Path to the file that contains all the testcases.
#      If the input is input is in the form of a list/tuple/dictionary, 
#      enclose it inside a list or a tuple
#      ( Should be named test_cases.py )
# 

presets_folder = os.getcwd() + "\\presets" # do not change
presets = {         # Format for adding new presets:-
                    # 'ChallengeName': f"{presets_folder}\\ChallengeFileName",
    'CardTiming': f"{presets_folder}\\CardTiming",
    'Treasure': f"{presets_folder}\\Treasure"
}
PRESET = 'Treasure' # Choose from the presets dictionary

# Server files ------------------------------------
folder = "" # Change folder location to the one containing your files

if PRESET:
    folder = presets[PRESET]

EXAMPLE_FILE = f"{folder}\\example.py"
SOLUTION_FILE = f"{folder}\\check.py"
TEST_CASES = f"{folder}\\test_cases.py"

#--------------------------------------------------
# 
# MODE :
#     There are currently only two options, i.e. Shortest, Fastest.
#     Shortest sorts by file size and Fastest sorts by time taken
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
#     imported according to the preset, you can leave those blank, i.e. None, or as is,
#     just without any syntax error
#
# Challenge Info ----------------------------------

# the spelling should be correct, case doesnt matter
MODE = "fastest" # "Shortest" / "Fastest"
TIME = 10

# Use similar format for writing the task
TASK = """test task
"""*10

# If input is a list or tuple or dictionry or 
# in case of multiple inouts, make it a string
EXAMPLES = {    
    1: 1,
    2: 4,
    3: 9
}

# -----------Do not change------------
if PRESET:
    from presets import info  # ClashOfCode\\server\\presets\\info.py
    TASK = info.INFO[PRESET]['TASK']
    EXAMPLES = info.INFO[PRESET]['EXAMPLES']
# ------------------------------------

#--------------------------------------------------
