# Recursion : function calling itself
# if we call function for using code inside it we use recursion

def function(k):
  if(k > 0):
    result = k + function(k - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results")
function(5)
