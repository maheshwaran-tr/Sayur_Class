'''5.Write the function mostFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated the same), 
returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be atwcdekn'''


def removedup(str):
    s = ""
    for i in str:
        if not i in s:
            s = s+i
    print(s)


msginput = 'We Attack at Dawn'      #op -> atwcdekn
msginput = msginput.lower()
msginput = msginput.replace(" ","")
msg_alpha = sorted(msginput)
#['a', 'a', 'a', 'a', 'c', 'd', 'e', 'k', 'n', 't', 't', 't', 'w', 'w']
print(msg_alpha)
sorted_list = sorted(msg_alpha, key=lambda n: msg_alpha.count(n),reverse=True)  
#['a', 'a', 'a', 'a', 't', 't', 't', 'w', 'w', 'c', 'd', 'e', 'k', 'n']
final_msg = sorted(set(sorted_list))
final_msg = "".join(sorted_list)
removedup(final_msg)