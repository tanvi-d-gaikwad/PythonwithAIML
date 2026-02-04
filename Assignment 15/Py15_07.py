Checklength = lambda Ch : len(Ch) > 5

def main():
    Words = ["Shreement", "Dagdushet" , ":" , "Jay" , "Ganesh"]
    print("The words  are: ",Words)

    EvenNumbers = list(filter(Checklength, Words))
    print("The words with more than 5 letters are",EvenNumbers)

if __name__ == "__main__":
    main()