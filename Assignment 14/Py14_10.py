MaxOfThree = lambda No1, No2, No3: No1 if No1 >= No2 and No1 >= No3 else (No2 if No2 >= No3 else No3)

def main():
    N1 = int(input("Enter the first number: "))
    N2 = int(input("Enter the second number: "))
    N3 = int(input("Enter the third number: "))

    Ret = MaxOfThree(N1, N2, N3)

    print(Ret," is the maximum.")
    
if __name__ == "__main__":
    main()