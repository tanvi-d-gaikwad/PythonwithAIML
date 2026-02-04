Multiplication = lambda No1, No2 : No1*No2

def main():
    N1 = int(input("Enter the first number: "))
    N2 = int(input("Enter the second number: "))

    Ret = Multiplication(N1, N2)

    print(Ret," is the multiplication.")
    
if __name__ == "__main__":
    main()