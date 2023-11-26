
def revstr(str):
    str = str.split()
    print(str)
    new =[]
    print(new)
    for word in str:
        newword = word[len(word)-1] + word[1:len(word)-1] + word[0]      # word[1:] -> starts from 2nd letter to end of the string
        new.append(newword) 
        print(new)
    print(new)
    return " ".join(new)
    

str = input("Enter the string : ")
print(revstr(str))