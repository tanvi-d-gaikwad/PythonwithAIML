from functools import reduce

Minimum = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    Numbers = [43,345,23,5,34,12,43,54]
    print("The numbers are: ",Numbers)

    Min = reduce(Minimum, Numbers)
    print("The minimum is ",Min)

if __name__ == "__main__":
    main()