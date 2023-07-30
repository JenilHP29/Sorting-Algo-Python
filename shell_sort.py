def shell_sort(a):
    k = len(a)//2
    while k > 0:
        for i in range(k,len(a)):
            temp = a[i]
            j=i
            while j>=k and a[j-k]>temp:
                a[j]=a[j-k]
                j-=k
            a[j]=temp
        k//=2

ls=[23,34,29,10,309,38,193,4858,103,3,193,1]
shell_sort(ls)
print(ls)