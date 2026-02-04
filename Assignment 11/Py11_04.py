def ReverseNumber(No):
    S = str(No)
    Sum = 0
    for i in range(len(S)-1,-1,-1):
        print(int(S[i]),end="")

def main():
    N = int(input("Enter the number: "))

    Summation = ReverseNumber(N)

if __name__ == "__main__":
    main()