def PerfectNumber(No):
    Sum = 0
    for i in range(1,No):
        if (No % i == 0):
            Sum = Sum + i

    if (Sum == No):
        return True
    else:
        return False

def main():
    N = int(input("Enter the number: "))
    B = PerfectNumber(N)
    if(B == True):
        print(N," is a perfect number")
    else:
        print(N," is not a perfect number")

if __name__ == "__main__":
    main()