def Check(No):
    if (No % 5 == 0) and (No % 3 == 0):
        return True
    return False

def main():
    N = int(input("Enter the number: "))
    B = Check(N)
    if (B == True):
        print(N," is divisible by 5 and 3")
    else:
        print(N, "is not divisible by 5 and 3")

if __name__ == "__main__":
    main()