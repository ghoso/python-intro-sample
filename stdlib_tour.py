import sys
import os
import glob

print("Command Arguments: ", sys.argv)
print("Current Directory: ", os.getcwd())
print("Python Files: ", glob.glob('*.py'))