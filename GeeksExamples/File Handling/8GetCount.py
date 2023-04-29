# Python – Get number of characters, words, spaces and lines in a file
# Given a text file fname, the task is to count the total number of
# characters, words, spaces and lines in the file.

# Naive approach
def counter(fname):
    words = 0
    lines = 0
    charc = 0
    spaces = 0

    with open(fname, 'r') as f:
        # Loop to iterate file line by line.
        for line in f:
            lines += 1

            # declaring a variable let and assigning its value as Y
            # because every file is supposed to start with a word or a letter.
            let = 'Y'

            # loop to iterate every line letter by letter.
            for letter in line:
                # condition to check that the encountered character is not white space and a word.
                if (letter != ' ' and let == 'Y'):
                    words += 1

                    # assigning value N to variable let because until
                    # space will not encounter a word can not be completed.
                    let = "N"

                # condition to check that the encountered letter is a white space
                elif (letter == ' '):
                    spaces += 1

                    # Assigning value Y to variable let because after white space a word is supposed to occur.
                    let = 'Y'

                # loop to iterate every letter character by character.
                for i in letter:
                    # condition to check that the encountered character is not white space and not a newline character
                    if (i != " " and i != '\n'):
                        charc += 1

    print(f"Words= {words}")
    print(f"Lines= {lines}")
    print(f'Characters={charc}')
    print(f'Spaces= {spaces}')


# Driver code:
if __name__ == '__main__':
    fname = 'file1.txt'
    try:
        counter(fname)
    except:
        print(f'{fname} not found.')
