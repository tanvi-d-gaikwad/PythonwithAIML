def ChkGreater(No1, No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    N1 = int(input("Enter first no.: "))
    N2 = int(input("Enter second no.: "))
    Greater = ChkGreater(N1, N2)

    print(Greater,"is greater")

if __name__ == "__main__":
    main()