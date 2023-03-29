# consider a module same as the library
# a file containing set of functions you want to include in your application

# To create module 
# here we rename module (module_demo as md1) and (module_demo2 as md2)
import module_demo as md1
import module_demo2 as md2

md1.demo1("Om Patil") # When using a function from a module, use the syntax: module_name.function_name
a = md2.demo2["name"]
print(a)



