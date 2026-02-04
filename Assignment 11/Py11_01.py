def ChkPrime(No):
    for i in range(2,No):
        if (No % i == 0):
            return False
    return True

def main():
    N = int(input("Enter the number: "))
    B = ChkPrime(N)
    if (B == True):
        print(N,"is a prime number")
    else:
        print(N,"is not a prime number")

if __name__ == "__main__":
    main()