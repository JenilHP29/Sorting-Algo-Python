from turtle import clear


def counting_sort(a,k):
    c=[0]*k
    b=[0]*len(a)
    for i in range(len(a)):
        c[a[i]]=c[a[i]]+1
    for j in range(1,k):
        c[j]+=c[j-1]
    for i in range(len(a)-1,-1,-1):
        c[a[i]]=c[a[i]]-1
        b[c[a[i]]]=a[i]
    return b

ls=[23,34,29,10,309,38,193,4858,103,3,193,1]
print(counting_sort(ls,max(ls)+1))    