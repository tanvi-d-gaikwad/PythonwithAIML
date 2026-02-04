def Multiplication(j, No):
#    for i in range(1,11):
#        print(No," * ", i, " = ", No*i) can be done in this way too when single parameter is passed
    return j*No

def main():
    N = int(input("Enter the number: "))
    for i in range(1,11):
        Number = Multiplication(i,N)
        print(N," * ", i, " = ", Number)

if __name__ == "__main__":
    main()