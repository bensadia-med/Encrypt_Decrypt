
#Get The P and G:
print(" The Shared Prime Must be greater than Shared Base ")
print("  Enter Publicly Shared Prime: ")
sharedPrime=int(input())
print("  Enter Publicly Shared Base:  ")
sharedBase=int(input())
while (sharedPrime<=sharedBase):
    print("  Enter Publicly Shared Prime: ")
    sharedPrime = int(input())
    print("  Enter Publicly Shared Base:  ")
    sharedBase = int(input())

print("Publicly Shared Variables:")
print("    Publicly Shared Prime: ", sharedPrime)
print("    Publicly Shared Base:  ", sharedBase)

#Get The Number of Users:
print("Enter the Number of Users: ")
numberUsers=int(input())

#Get The Secret Numbers:
SecretNumbertab=[]
print("Enter the Number of User's Secret Number: ")
for i in range(numberUsers):
    print("Secret Number, n° ",i)
    SecretNumber=int(input())
    SecretNumbertab.append(SecretNumber)
#print(SecretNumbertab)

#Shift Tab Function:
def shift(l, n):
    return l[n:] + l[:n]


#Get The First Tab
def DiffieHellmanEncryption(SecretNumbertab):
    SecretNumbertab1=[]
    for j in range(len(SecretNumbertab)):
        if j == 0:
            for i in range(len(SecretNumbertab)):
                SecretNumbertab1.append((sharedBase**SecretNumbertab[i])%sharedPrime)
        if j > 0:
            SecretNumbertab2=shift(SecretNumbertab1,-1)
            SecretNumbertab1.clear()
            for i in range(len(SecretNumbertab)):
                SecretNumbertab1.append((SecretNumbertab2[i] ** SecretNumbertab[i]) % sharedPrime)
    return SecretNumbertab1
print("All The Keys is equals to each other :")
print(DiffieHellmanEncryption(SecretNumbertab))