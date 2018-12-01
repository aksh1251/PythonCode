x= True
print("The initial state of x: ",x)
print("The type of x: ",type(x))
x= not x
print ("after not op: ",x)

y = True
print("The initial state of x: ", y)
print("The type of y: ", type(y))
y = y or y
print("after not op: ", y)

z = True
print("The initial state of z: ", z)
print("The type of z: ", type(z))
z = z and z
print("after not op: ", z)
