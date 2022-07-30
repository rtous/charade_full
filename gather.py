from os import listdir
from os.path import isfile, join, splitext
#import pathlib
import traceback
from shutil import copyfile

OUTPUTPATH = "img"
MOVIE = "charade"

#pathlib.Path(OUTPUTPATH).mkdir(parents=True, exist_ok=True) 

i = 0

def gather(dir, prefix):
	global i
	files = [f for f in listdir(dir) if isfile(join(dir, f))]
	for filename in files:
		copyfile(join(dir, filename), join(OUTPUTPATH, str(i)+"_"+prefix+"_"+MOVIE+".png"))
		i+=1

gather("1_MFS","MFS")
gather("2_MS", "MS")
gather("3_MCU", "MCU")
gather("4_CU", "CU")
gather("5_ECU", "ECU")



