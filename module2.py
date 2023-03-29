# When importing using the from keyword, 
# do not use the module name when referring to elements in the module. 
# Example: info["age"], not mymodule.info["age"]

from module_demo3 import info

print(info["age"])