def selection_sort(a):
    for i in range(len(a)-1):
        min=i
        for j in range(i+1,len(a)):
            if(a[j]<a[min]):
                min=j
                j+=1
        temp=a[i]

        a[i]=a[min]
        a[min]=temp

ls=[23,34,29,10,309,38,193,4858,103,3,193,1]
selection_sort(ls)
print(ls)