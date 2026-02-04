sqr = lambda a: a*a

def main():
    Numbers = [2,4,6,8,10]
    x = list(map(sqr, Numbers))

    print(x)  #[4, 16, 36, 64, 100]

if __name__ == "__main__":
    main()