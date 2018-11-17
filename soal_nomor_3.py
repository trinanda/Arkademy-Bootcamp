line = 8
print((line) * "* ")
for i in range(line-1, 1, -1):
    print((line-i-1)* " " +  "*" + (2*i -1)*" " + "* ")
print((line-1) * " " + "* ")