CheckOdd = lambda No : (No % 2 != 0)

def main():
    N = int(input("Enter the number: "))

    Ret = CheckOdd(N)

    if(Ret == True):
        print("It is Odd")
    else:
        print("It is Even")
    
if __name__ == "__main__":
    main()