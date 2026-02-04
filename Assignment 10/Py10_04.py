def PrintEven(No):
    for i in range(1,No+1):
        if(i % 2 == 0):
            print(i)

def main():
    N = int(input("Enter the number: "))
    PrintEven(N)

if __name__ == "__main__":
    main()