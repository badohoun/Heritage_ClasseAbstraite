import sys
print(sys.path)
sys.path.insert(0,"/Users/espoirbadohoun/trainingclassabstraite/Heritage_ClasseAbstraite")
from PACKAGING.my_other_file import CONSTANT as CONSTANT2 # not use this relative import 
# in this case we are trying to import something from a file higher in the file hierarchy into the file more deeply in the file hierarchy

CONSTANT = "hello"
print(CONSTANT2)