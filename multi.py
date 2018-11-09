import sys

# argv is your commandline arguments, argv[0] is your program name, so skip it
for n in sys.argv[1:]:
    print(n) #print out the filename we are currently processing
    input = open(n, "r")
    output = open(n + ".out", "w")
    # do some processing
    
    input.close()
    output.close()