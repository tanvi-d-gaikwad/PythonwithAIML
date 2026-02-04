def Arithmatic(No1, No2):
    Addition = No1 + No2
    Substraction = No1 - No2
    Multiplication = No1 * No2
    
    try: 
        Division = No1 / No2

    except:
        Division = 0

    return Addition, Substraction, Multiplication, Division

def main():
    N1 = int(input("Enter first number: "))
    N2 = int(input("Enter second numer: "))

    A, S, M, D = Arithmatic(N1, N2)

    print(A," is the addition")
    print(S," is the substraction")
    print(M," is the multiplication")
    if (D != 0):
        print(D," is the division")
    else:
        print("Division is not possible")

if __name__ == "__main__":
    main()