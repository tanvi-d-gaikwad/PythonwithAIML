def AreaOfRec(L,W):
    return L*W

def main():
    len = int(input("Enter the length of the rectangle: "))
    wid = int(input("Enter the width of the rectangle: "))

    Area = AreaOfRec(len,wid)

    print(Area," is the area of the rectangle with length ",len,"and width ",wid)

if __name__ == "__main__":
    main()