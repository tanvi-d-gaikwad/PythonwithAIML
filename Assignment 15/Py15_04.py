from functools import reduce

Addition = lambda No1,No2 : No1+No2

def main():
    Numbers = [43,345,23,5,34,12,43,54]
    print("The numbers are: ",Numbers)

    Add = reduce(Addition, Numbers)
    print("The addition is ",Add)

if __name__ == "__main__":
    main()