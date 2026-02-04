def Cube(No):
    return No*No*No

def main():
    N = int(input("Enter number: "))
    C = Cube(N)
    print("The cube is: ",C)

if __name__ == "__main__":
    main()