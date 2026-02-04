CheckEven = lambda No: No % 2 == 0

def main():
    
    Numbers = [43,345,23,5,34,12,43,54]
    print("The numbers are: ",Numbers)

    EvenNumbers = list(filter(CheckEven, Numbers))
    print("The amount of even numbers are",len(EvenNumbers))

if __name__ == "__main__":
    main()