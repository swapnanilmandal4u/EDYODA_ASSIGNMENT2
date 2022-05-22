#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

a= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(1,len(a)):
    for j in range(len(a)-i):
        if a[j][1]>a[j+1][1]:
            temp=a[j]
a[j]=a[j+1]
a[j+1]=temp
for j in range(len(a)):
    print(a[j])

 


