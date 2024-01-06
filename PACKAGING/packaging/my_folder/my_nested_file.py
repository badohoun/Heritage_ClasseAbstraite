from packaging.my_other_file import CONSTANT as CONSTANT2 # not use this relative import 
# in this case we are trying to import something from a file higher in the file hierarchy into the file more deeply in the file hierarchy

CONSTANT = "hello"
print(CONSTANT2)