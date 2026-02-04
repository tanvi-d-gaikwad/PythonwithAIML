def DisplayNTo1(No):
    for i in range(No,0,-1):
        print(i)

def main():
    N = int(input("Enter the number: "))

    DisplayNTo1(N)

if __name__ == "__main__":
    main()