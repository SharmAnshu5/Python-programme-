a = int(input( "Enter first side : "))

b = int(input("Enter second side : "))

c = int(input("Enter third side : "))

s= (a+b+c)/2

Area = (s*(s-a)*(s-b)*(s-c))**0.5

print(Area)
