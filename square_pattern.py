'''1  2   3  4  5
   16 17 18 19  6
   15 24 25 20  7
   14 23 22 21  8
   13 12 11 10  9'''
n=int(input())
n_list=[[0 for x in range(n)] for y in range(n)]

n1=1
low=0
high=n-1
count=int((n+1)/2)
for i in range(count):
    for j in range(low,high+1):
        n_list[i][j]=n1
        n1+=1
    for j in range(low+1,high+1):
        n_list[j][high]=n1
        n1+=1
    for j in range(high-1,low-1,-1):
        n_list[high][j]=n1
        n1+=1

    for j in range(high-1,low,-1):
        n_list[j][low]=n1
        n1+=1

    low=low+1
    high=high-1



for i in range(n):
    for j in range(n):
        print(n_list[i][j],end="\t")
    print()
