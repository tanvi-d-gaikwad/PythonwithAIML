def Length(No):
    return len(str(No))

def main():
    N = int(input("Enter the number: "))

    length = Length(N)
    print("The number of digits in ",N,"are ",length)

if __name__ == "__main__":
    main()