import fileinput

with fileinput.input(files=('a.txt', 'd.txt')) as f:
    for line in f:
        print(line)


        