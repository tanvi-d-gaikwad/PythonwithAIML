def AreaOfCircle(R):
    return 3.14*R*R

def main():
    radius = int(input("Enter the radius of the circle: "))

    Area = AreaOfCircle(radius)

    print(Area," is the area of the circle with",radius," as it's radius.")

if __name__ == "__main__":
    main()