def InsertionSort(alist):
    for i in range(len(alist)):
        num = alist[i]
        pos = i 
        while pos > 0 and alist[pos - 1] > num:
            alist[pos] = alist[pos-1]
            pos = pos - 1
        alist[pos] = num 
    return alist

print(InsertionSort([8,6,5,4,3,1,9,10,2,7]))

