from main import main
import os
import time

in_txt = [ val for val in os.listdir( "./" ) if (val[-3:] == "txt") and (val[:2] == "in") ]
in_txt = sorted(in_txt)

for (i, in_file) in enumerate(in_txt):
    print("\n_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
    cmd = "python main.py < {0}".format(in_file)
    print(cmd)
    st = time.time()
    os.system( cmd )
    print( "laptime: {0:.3f} sec".format( time.time() - st ) )
