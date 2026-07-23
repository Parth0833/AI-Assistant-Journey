a=int(input("Enter ur First Number:"))
b=int(input("Enter ur Second Number:"))
op=(input("Enter the operator:"))
if (op=="+"):
    print("Addition:",a+b)
elif (op=="-"):
    print("Substraction:",a-b)
elif(op=="*"):
    print("Multiplication:",a*b)
elif(op=="/"):
    print("Division:",a/b)
elif(op=="%"):
    print("Modulus:",a%b)
elif(op=="**"):
    print("Power:",a**b)
else:
    print("Invalid Input")