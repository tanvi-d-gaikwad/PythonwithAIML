Min = lambda No1, No2 : (No1 < No2)

def main():
    N1 = int(input("Enter the first number: "))
    N2 = int(input("Enter the second number: "))
    Ret = Min(N1,N2)
    if(Ret == True):
        print(N1," is less than ",N2)
    else:
        print(N2," is less that ",N1)

if __name__ == "__main__":
    main()