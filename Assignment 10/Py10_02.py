def SumOfFirstNNaturnalNo(No):
    S = 0
    for i in range(1,No+1):
        S = S + i
    return S

def main():
    N = int(input("Enter the number: "))
    Sum = SumOfFirstNNaturnalNo(N)
    print("The sum of first", N,"naturnal numbers is: ",Sum)

if __name__ == "__main__":
    main()