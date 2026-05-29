a = 10
b = 20
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)  o/p :a=20 b=10

#2
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
a,b=b,a
print("a =", a)
print("b =", b)

#3 method
a=int(input("Enter the value of a:",a))
b=int(input("Enter the value of b:",b))
a=a+b
b=a-b
a=a-b
print("a =", a)
print("b =", b)

#4
a = 10
b = 20
a = a ^ b
b = a ^ b
a = a ^ b
print("a =", a)
print("b =", b)
