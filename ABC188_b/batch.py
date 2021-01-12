from main import main
import os

in_txt = [ val for val in os.listdir( "./" ) if val[-3:] == "txt" ]
in_txt = sorted(in_txt)

for (i, in_file) in enumerate(in_txt):
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
    cmd = "python main.py < {0}".format(in_file)
    print(cmd)
    os.system( cmd )
