def Factorial(No):
    F = 1
    for i in range(1,No+1):
        F = F*i 
    return F

def main():
    N = int(input("Enter the number: "))
    Fact = Factorial(N)
    print("The factorial of" ,N, "is" ,Fact)

if __name__ == "__main__":
    main()