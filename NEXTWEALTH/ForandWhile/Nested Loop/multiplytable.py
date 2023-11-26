######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.


start , end = 7 , 16
rows = 12

for i in range(start,end+1):
    for j in range(1,rows+1):
        print(f"{i} * {j} = {i*j}")
    print("-------------------")