# Python implementation to compute number of characters, words, spaces and lines in a file
# In this approach, we will use os.linesep() to seperate the lines on the current plateform.

import os


def counter(fname):
    words = 0
    lines = 0
    charc = 0
    spaces = 0

    with open(fname, 'r') as f:
        for line in f:
            # separating a line from \n character and storing again in line variable for further operations.
            line = line.strip(os.linesep)
            # splitting the line to make a list of all the words present in that line and storing that list in wordslist variable.
            wordslist = line.split()
            lines += 1

            words = words + len(wordslist)

            charc = charc + sum(1 for c in line if c not in (os.linesep, " "))

            spaces = spaces + sum(1 for s in line if s in (os.linesep, ' '))

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
