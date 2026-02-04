from functools import reduce

Multiplication = lambda No1,No2 : No1*No2

def main():
    Numbers = [43,345,23,5,34,12,43,54]
    print("The numbers are: ",Numbers)

    Multi = reduce(Multiplication, Numbers)
    print("The multiplication is ",Multi)

if __name__ == "__main__":
    main()