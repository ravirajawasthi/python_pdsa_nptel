from random import randint
lst = []
for i in range(20):
    lst.append(randint(-100,200))
def selectionSort(lst):
    minpos = 0
    for i in range(len(lst)):
        minpos = i
        for j in range(i,len(lst)):
            if lst[j] < lst[minpos]:
                minpos = j
        (lst[j],lst[minpos]) = (lst[minpos],lst[j])
selectionSort(lst)
print(lst)