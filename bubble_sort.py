def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if(a[j]>a[j+1]):
                temp=a[j+1]
                a[j+1]=a[j]
                a[j]=temp

ls=[2,8,4,3,5,1]
bubble_sort(ls)  
print(ls)