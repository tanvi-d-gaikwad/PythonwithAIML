CheckOdd = lambda No: No % 2 != 0

def main():
    Numbers = [43,345,23,5,34,12,43,54]
    print("The numbers are: ",Numbers)

    OddNumbers = list(filter(CheckOdd, Numbers))
    print("The odd numbers are",OddNumbers)

if __name__ == "__main__":
    main()