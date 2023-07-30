def merge_sort(a):
    if(len(a)>1):
        mid=len(a)//2
        l=a[:mid]
        r=a[mid:]
        merge_sort(l)
        merge_sort(r)
        i,j,k=0,0,0
        while(i<len(l) and j<len(r)):
            if(l[i] < r[j]):
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while(i<len(l)):
            a[k]=l[i]
            i+=1
            k+=1
        while(j<len(r)):
            a[k]=r[j]
            j+=1
            k+=1

ls=[23,34,29,10,309,38,193,4858,103,3,193,1]
merge_sort(ls)
print(ls)