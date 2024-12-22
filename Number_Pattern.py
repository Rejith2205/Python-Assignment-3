rows=int(input("enter number of rows: "))
for i in range(rows):
        for j in range (rows-i-1,-1,-1): ## reverse the index of column (row-(0,the value of j)-1,-1(index till zero),-1-step)
            print (j+1,end ='')          #these kinds of pattern we need to reverse the index
        print('')
