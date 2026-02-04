def PrintFactors(No):
    for i in range(1,No+1):
        if(No % i == 0):
            print(i)

def main():
    N = int(input("Enter the number: "))
    PrintFactors(N)

if __name__ == "__main__":
    main()