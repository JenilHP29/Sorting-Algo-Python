def insertion_sort(a):
    for i in range(1,len(a)):
        temp=a[i]
        j=i-1
        while(j>=0 and a[j]>=temp):
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp

ls=[23,34,29,10,309,38,193,4858,103,3,193,1]
insertion_sort(ls)        
print(ls)   