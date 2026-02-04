DivisibilityCheck = lambda No : (No % 5 == 0) and (No % 3 == 0)

def main():
    Numbers = [15, 30, 45, 3, 6, 9, 21, 5, 10, 20, 25, 1, 7, 8, 11, 14]
    print("The numbers are: ",Numbers)

    Filtered = list(filter(DivisibilityCheck, Numbers))
    print("The numbers which are divisible by both 5 and 3 are",Filtered)

if __name__ == "__main__":
    main()