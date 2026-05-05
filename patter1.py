for i in range(5):
    print("*",end=" ")   # o/p: * * * * *

# program 2 
for i in range(1,5):         #here 1,2,3,4
    print()                  #moves to next line instead of this line print on same line
    for j in range(1,i+1):   #(1,1+1)->(1) as per that finally(1,4+1)->(1,5)
        print(j,end=" ")     #print in same line
output:
1
12
123
1234
