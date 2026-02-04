def MarkstoGrade(No):
    if(No >= 75):
        Grade = "Distinction"
    elif(No >= 60):
        Grade = "First Class"
    elif(No >= 50):
        Grade = "Second Class"
    else:
        Grade = "Fail"

    return Grade

def main():
    N = int(input("Enter the martks of the student: "))

    G = MarkstoGrade(N)
    print("The grade is ",G)

if __name__ == "__main__":
    main()