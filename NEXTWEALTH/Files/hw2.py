with open("NEXTWEALTH\Files\inpfile.txt","r") as inputFile, open("alphabet.txt","w") as outputfile:
    line = inputFile.readline()
    lineNo = 1
    while line:
        line = line.replace(" ","")
        line = line.replace("\n","")
        
        dic = {}
        for letters in line:
            dic[letters] = dic.get(letters,0) + 1
        
        outputfile.write(f"Character Frequency in line number {lineNo} : \n")
        for i in dic:
            outputfile.write(f" {i} : {dic[i]}\n")
        outputfile.write("\n")

        line = inputFile.readline()
        lineNo += 1