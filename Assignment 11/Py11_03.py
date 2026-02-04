def SumOfDigits(No):
    S = str(No)
    Sum = 0
    for i in range(len(S)):
        Sum = Sum + int(S[i])
    return Sum

def main():
    N = int(input("Enter the number: "))

    Summation = SumOfDigits(N)
    print("The summation of digits of ",N, "is ",Summation)

if __name__ == "__main__":
    main()