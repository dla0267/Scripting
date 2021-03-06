
import sys
from collections import defaultdict

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


    # for key in dict2.keys():
    #     print(key + ": " + str(dict1[key]))
    # for the first question
    # need a dictionary for all the segments as keys
    # and a values as set of cookies or list of cookies

    # 2nd Requirement
    # I may just do it in the other way
    

    segments = defaultdict(set)
    missingSegments = defaultdict(set)
    
    cookieWithExtra = defaultdict(set)
    cookieWithLess = defaultdict(set)

    cookkieeeee = []
    totalSegment = set()
    for key in dict1.keys():
        if key not in dict2.keys():
            cookkieeeee.append(key)
        else:
            for segment in dict1[key]:
                totalSegment.add(segment)
                if segment not in dict2[key]:
                    segments[segment].add(key)
                    cookieWithExtra[key].add(segment)
            for segment2 in dict2[key]:
                totalSegment.add(segment)

                if segment2 not in dict1[key]:
                    missingSegments[segment2].add(key)
                    cookieWithLess[key].add(segment2)

    print('Segments with added cookies: ' + str(len(segments.keys())) + " / " + str(len(dict1.keys())))
    lineNum = 0
    sortedKey = list(segments.keys())
    sortedKey.sort()
    for seg in sortedKey:
        a = list(segments[seg])
        print(str(lineNum) + "\t" + seg + "\t" + str(len(segments[seg])) + "\t" + str(a))
        lineNum += 1 

    print("")
    print('Segments with missing cookies: ' + str(len(missingSegments.keys())) + " / " + str(len(dict1.keys())))

    lineNum = 0
    sortedMissingSeg = list(missingSegments.keys())
    sortedMissingSeg.sort()
    for seg in sortedMissingSeg:
        values = list(missingSegments[seg])
        print(str(lineNum) + "\t" + seg + "\t" + str(len(missingSegments[seg])) + "\t" + str(values))
        lineNum += 1 



    print("")
    print('Cookies with extra segments: ' + str(len(cookieWithExtra.keys())) + " / " + str(len(totalSegment)))

    lineNum = 0
    sortedCookie = list(cookieWithExtra.keys())
    sortedCookie.sort()
    for cookie in sortedCookie:
        segments_ = list(cookieWithExtra[cookie])
        print(str(lineNum) + "\t" + cookie + "\t" + str(len(cookieWithExtra[cookie])) + "\t" + str(segments_))
        lineNum += 1 
    

    print("")
    print('Cookies with omitted segments: ' + str(len(cookieWithLess.keys())) + " / " + str(len(totalSegment)))

    lineNum = 0
    sortedCookie2 = list(cookieWithLess.keys())
    sortedCookie2.sort()
    for cookie in sortedCookie2:
        segments_ = list(cookieWithLess[cookie])
        print(str(lineNum) + "\t" + cookie + "\t" + str(len(cookieWithLess[cookie])) + "\t" + str(segments_))
        lineNum += 1 


# processedLines = manipulateData(lines)

    # with open(outFile,'w') as o:
    #     for line in processedLines:
    #         o.write(line)


if __name__ == "__main__":
    main()