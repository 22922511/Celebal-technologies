
# Assignment week 1
#Problem : Create lower triangular, upper triangular and pyramid containing the "*" character

# taking input
n = int(input("Enter length of triangle: "))
print()
print()

print("Lower triangular\n")
#Lower triangular
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="") 
    print()  
    
    
print()  
print("Upper triangular\n")

#Upper triangular
for i in range(1, n + 1):
    for j in range(1, n-i+2):
         print("*", end="")  
    print()  
    

print()
print("Pyriamid\n")
#Pyriamid
for i in range(0, n ):
    for j in range(0, n-i-1):
        print(" ",end="")
    for k in range(0,i+i+1):
         print("*", end="")  
    print()  

