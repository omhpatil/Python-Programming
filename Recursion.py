# Recursion : function calling itself

def function(k):
  if(k > 0):
    result = k + function(k - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results")
function(5)
