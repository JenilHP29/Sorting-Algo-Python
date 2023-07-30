def partion(a,low,high):
    pivot=a[low]
    i=low
    j=high
    while(i<=j):
        while(a[i]<=pivot):
            i+=1
        while(a[j]>pivot):
            j-=1
        if(i<j):
            (a[i],a[j])=(a[j],a[i])
    (a[j],a[low])=(a[low],a[j])
    return j
    print(a)

def quick_sort(a,low,high):
    if(low<high):
        m=partion(a,low,high)
        quick_sort(a,low,m-1)
        quick_sort(a,m+1,high)

ls=[23,34,29,10,309,38,193,4858,103,3,193,1]
quick_sort(ls,0,len(ls)-1)
print(ls)