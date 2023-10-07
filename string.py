ip = "134.67.158.49"

var = ip.split(".")

first = var[0]
last = var[-1]

var[0] = last
var[-1] = first
# or
# var[0],var[-1] = var[-1],var[0]

var2 = '.'.join(var)
print(var2)