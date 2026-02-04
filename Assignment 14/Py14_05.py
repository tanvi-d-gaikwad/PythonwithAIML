CheckEven = lambda No : (No % 2 == 0)

def main():
    N = int(input("Enter the number: "))

    Ret = CheckEven(N)

    if(Ret == True):
        print("It is Even")
    else:
        print("It is Odd")
    
if __name__ == "__main__":
    main()