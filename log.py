
import sys


def main():
    inFile = sys.argv[1]
    inFile2 = sys.argv[2]

    with open(inFile,'r') as i:
        f1 = i.readlines()

    # f = open("sampleInteg.txt", "r")
    # f1 = f.readlines()


    dict1 = {}

    for line in f1:
        # if line[0] == '0' or line[0] == '1' or line[0] == '2':
        integers = []
        for i in range(10):
            integers.append(str(i))
        # if line[0] == '0' or line[0] == '1' or line[0] == '2':
        if line[0] in integers:

            parsed_line = line.split(' ')
            if len(parsed_line) == 3 and len(parsed_line[2]) != 3:
                cookie = parsed_line[0]
                segment = parsed_line[2]
                segment = segment[1:-2]

                if cookie not in dict1.keys():
                    dict1[cookie] = [segment,]
                else:
                    dict1[cookie].append(segment)

            elif len(parsed_line) > 3:
                cookie = parsed_line[0]
                segment = parsed_line[2]
                segment = segment[1:-1]
                if cookie not in dict1.keys():
                    dict1[cookie] = [segment,]
                else:
                    dict1[cookie].append(segment)

                for i in range(3, len(parsed_line)):
                    segment = parsed_line[i].strip()
                    segment = segment[:-1]
                    if cookie not in dict1.keys():
                        dict1[cookie] = [segment,]
                    else:
                        dict1[cookie].append(segment)
            else:
                cookie = parsed_line[0]
                if cookie not in dict1.keys():
                    dict1[cookie] = []

    # for key in dict1.keys():
    #     print(key + ": " + str(dict1[key]))


    with open(inFile,'r') as i:
        f1 = i.readlines()

    # f = open("sampleInteg.txt", "r")
    # f1 = f.readlines()

    with open(inFile2,'r') as i:
        f2 = i.readlines()
    dict2 = {}

    for line in f2:
        
        integers = []
        for i in range(10):
            integers.append(str(i))
        # if line[0] == '0' or line[0] == '1' or line[0] == '2':
        if line[0] in integers:
            parsed_line = line.split(' ')
            if len(parsed_line) == 3 and len(parsed_line[2]) != 3:
                cookie = parsed_line[0]
                segment = parsed_line[2]
                segment = segment[1:-2]

                if cookie not in dict2.keys():
                    dict2[cookie] = [segment,]
                else:
                    dict2[cookie].append(segment)

            elif len(parsed_line) > 3:
                cookie = parsed_line[0]
                segment = parsed_line[2]
                segment = segment[1:-1]
                if cookie not in dict2.keys():
                    dict2[cookie] = [segment,]
                else:
                    dict2[cookie].append(segment)

                for i in range(3, len(parsed_line)):
                    segment = parsed_line[i].strip()
                    segment = segment[:-1]
                    if cookie not in dict2.keys():
                        dict2[cookie] = [segment,]
                    else:
                        dict2[cookie].append(segment)
            else:
                cookie = parsed_line[0]
                if cookie not in dict2.keys():
                    dict2[cookie] = []

    print("\n\nsecond File-------\n\n")

    # for key in dict2.keys():
    #     print(key + ": " + str(dict1[key]))
    # for the first question
    # need a dictionary for all the segments as keys
    # and a values as set of cookies or list of cookies

    # 2nd Requirement
    # I may just do it in the other way
    


    cookkieeeee = []
    extraSeg = []
    for key in dict1.keys():
        if key not in dict2.keys():
            cookkieeeee.append(key)
        else:
            for segment in dict1[key]:
                if segment not in dict2[key]:
                    extraSeg.append([key, segment])
    
    print(extraSeg)
# processedLines = manipulateData(lines)

    # with open(outFile,'w') as o:
    #     for line in processedLines:
    #         o.write(line)


if __name__ == "__main__":
    main()