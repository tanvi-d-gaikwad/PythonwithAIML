def Palimdrome(No):
    original = No
    reverse = 0

    while No > 0:
        digit = No % 10
        reverse = reverse * 10 + digit
        No //= 10

    return original == reverse

def main():
    N = int(input("Enter the number to see if it is palimdrome or not: "))

    B = Palimdrome(N)
    if(B== True):
        print(N," is a palimdrome number")
    else:
        print(N," is not a palimdrone number")

if __name__ == "__main__":
    main()