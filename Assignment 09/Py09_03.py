def Sqr(No):
    return No*No

def main():
    N = int(input("Enter number: "))
    Square = Sqr(N)
    print("The square is: ",Square)

if __name__ == "__main__":
    main()