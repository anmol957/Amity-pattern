
str="AMITY"
n=len(str)

for i in range(1, n+1):
    print(str[0:i])
        
i=1
while i<=n:
    j=1
    while j<=i:
        print(str[j-1], end=" ")
        j=j+1
    print()
    i=i+1
    
