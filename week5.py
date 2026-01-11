
a =1
b=2
sum = a+b
minus = a * b
mulltipy = a * b
divide = b / a 

#OOP

def SUM(a,b):
    sum = int(a) + int(b)
    return sum

def MINUS(a, b):
    sum = int(a) -int(b)
    return sum

def MULTIPLY(a, b):
    sum = int(a) *int(b) 
    return sum

def DIVDE(a, b):
    sum =int(a) /int(b)
    return sum

operate = input("1 = Sum, 2 = Minus, 3 = Muitiply, 4 =Di")

if(operate == "1"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    #inp3 = input("C : ")
    print(SUM(inp1, inp2))
elif(operate == "2"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    print(MINUS(inp1, inp2))
elif(operate == "3"):
    inp1 = input("A : ")
    inp2 = input("B :")
    print(MULTIPLY(inp1, inp2))        
elif (operate == "4"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    print(DIVDE(inp1, inp2))   
else:
    print("Not Found")  
'''   
inp1 = input("A : ")
inp2 = input("B : ")
inp3 = input("C : ")
print("SUM = ",(inp1, inp2, inp3))
'''





