Cube = lambda No : No*No*No

def main():
    N = int(input("Enter the number: "))
    Ret = Cube(N)
    # Ret = 11*11*11 = 1331

    print("Cube is : ",Ret)

if __name__ == "__main__":
    main()