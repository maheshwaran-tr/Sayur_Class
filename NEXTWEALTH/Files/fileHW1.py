# Homework problem ; Open input file, print the number of lines and the repeated word counts into an output file


with open("Files\sample.txt","r") as inputFile , open("D:/GITHUB_MAHES/Sayur_Mahesh-2/Files/result.txt","w") as outputfile:
    
    # to print how many lines
    flist = inputFile.readlines()
    noOfLines = len(flist)
    outputfile.write(f"The file contains {noOfLines} lines \n")

    # to print words per line
    for line,str in enumerate(flist,1):
        outputfile.write(f"Line {line} has {len(str.split())} words \n")
    
    # frequency of each word
    dic = {}
    for str in flist:
        for words in str.split():
            dic[words] = dic.get(words,0) + 1
    
    for i in dic:
        outputfile.write(f" \n{i} : {dic[i]}")