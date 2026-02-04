def DecimalToBinary(No):
    if No == 0:
        return "0"
    binary = ""
    while No > 0:
        remainder = No % 2
        binary = str(remainder) + binary
        No = No // 2
    return binary
    
def main():
    N = int(input("Enter the number: "))
    Binary = DecimalToBinary(N)

    print(Binary)

if __name__ == "__main__":
    main()
'''
1000

    8
    8%2 = 0
    8/2 = 4
    4%2 = 0
    4/2 = 2
    2%2 = 0
    2/2 = 1
    1/2 = 1
    '''
