# Quick Sorting #
def partitioning(a,first,last):
    pivot = random.randint(first,last)
    a[first],a[pivot]=a[pivot],a[first]
    swap=first
    for i in range(first+1,last+1):
        if(a[i]<a[first]):
            swap=swap+1
            a[swap],a[i]=a[i],a[swap]
    a[first],a[swap]=a[swap],a[first]
    return swap

def quicksort(a,first,last):
   if first < last:
        x = partitioning(a,first,last)
        quicksort(a, first, x-1)
        quicksort(a, x+1, last)

# Find the smallest kth element
def find_element(a,k,first,last):
    if k>0 and k<= (last-first) +1:
        x=partitioning(a,first,last)
        if (x-first) > (k-1):
            return find_element(a,k,first,x-1)
        if (x-first) < (k-1):
            return find_element(a,(k-x)-1,x+1,last)
        else:
            return a[x]
# Selection Sorting #
def selection(a):
    length=len(a)
    p=0
    while p<length:   # get the minimum value #
        min=p         # To get the minimum starting from the point pointed by the pointer #
        for i in range(p+1,length):
            if a[min]>a[i]:
                min=i
        a[p],a[min]=a[min],a[p]
        p=p+1         # increment the pointer by 1 so that we could get the minimum starting from next point #

# Insertion Sorting #
def insertion(a):
    length=len(a)
    for i in range(1,length):
        p=i-1         # save the index of the item right before the item selected #
        j=i-1         # save the index of the item right before the item selected #
        while j>=0 and j<=p and a[j+1]<a[j]:  #loop from 0 till the item right before the selected one if and only if the selected item is smaller than the item right before it #
            a[j],a[j+1]=a[j+1],a[j]           # exchange #
            j=j-1     # decrement the pointer by 1 as the index of the selected item has already changed #

# Merge Sorting #
def merge(a,first,middle,last):
    n1=middle-first+1  # define the length of the left array #
    n2=last-middle     # define the length of the right array #
    Left = [0]*(n1)    # set zeros to all values of the left array #
    Right = [0]*(n2)   # set zeros to all values of the right array #
    for i in range(0,n1):    # copy the left part to the left array #
        Left[i]=a[first+i]
    for j in range (0,n2):   # copy the right part to the right array #
        Right[j]=a[middle+1+j]
    i=j=0
    k=first
    while i<len(Left) and j<len(Right): # MERGING #
       if Left[i]<Right[j]:
           a[k]=Left[i]
           i= i+1
       else:
           a[k]=Right[j]
           j=j+1
       k=k+1
    while j<len(Right):
       a[k]=Right[j]
       j=j+1
       k=k+1
    while i<len(Left):
       a[k]=Left[i]
       i=i+1
       k=k+1

def mergesort(a,first,last):
    if first<last:
        middle = (first + last) // 2
        mergesort(a,first,middle)
        mergesort(a,middle+1,last)
        merge(a, first, middle, last)

# Hybrid Merge and Selection #
def hybrid(a,first,last,threshold):
    middle = (first + last) // 2
    if first<last:
        if (last-first)+1 > threshold:
            hybrid(a, first, middle, threshold)
            hybrid(a, middle + 1, last, threshold)
            merge(a, first, middle, last)


        else:
            selection(a)

# create array of random numbers #
import random
randomArray=[]
n=30
for i in range(n):
    randomArray.append(random.randint(1,99))
print(randomArray)
def copy(a,size):
    new=[0]*size
    for i in range(size):
        new[i]=a[i]
    return new
a1=copy(randomArray,len(randomArray))
a2=copy(randomArray,len(randomArray))
a3=copy(randomArray,len(randomArray))
a4=copy(randomArray,len(randomArray))
a5=copy(randomArray,len(randomArray))
a6=copy(randomArray,len(randomArray))
import time
begin1=time.time()
insertion(a1)
time.sleep(1)
end1=time.time()
begin2=time.time()
mergesort(a2,0,len(a2)-1)
time.sleep(1)
end2=time.time()
begin3=time.time()
selection(a3)
time.sleep(1)
end3=time.time()
begin4=time.time()
hybrid(a4,0,len(a4)-1,6)
time.sleep(1)
end4=time.time()
begin5=time.time()
quicksort(a5,0,len(a5)-1)
time.sleep(1)
end5=time.time()
print(a1,f"Total runtime of insertion = {end1-begin1}")
print(a2,f"Total runtime of merge = {end2-begin2}")
print(a3,f"Total runtime of selection = {end3-begin3}")
print(a4,f"Total runtime of hybrid = {end4-begin4}")
print(a5,f"Total runtime of quick = {end5-begin5}")
key=find_element(a6,7,0,len(a6)-1)
print(key)



