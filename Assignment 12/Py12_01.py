def ChkVowel(Ch):
    if (Ch == 'a') or (Ch == 'e') or (Ch == 'i') or (Ch == 'o') or (Ch == 'u'):
        return True

    if (Ch == 'A') or (Ch == 'E') or (Ch == 'I') or (Ch == 'O') or (Ch == 'U'):
        return True
    return False

def main():
    N = input("Enter the character: ")
    B = ChkVowel(N)

    if(B == True):
        print(N," is a vowel")

    else:
        print(N," is a consonant")

if __name__ == "__main__":
    main()