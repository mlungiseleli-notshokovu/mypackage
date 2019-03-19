
def bubble_sort(items):
    
    '''Return array of items, sorted in ascending order'''
    
    n = len(items) - 1
    
    for i in range(n):
        for k in range(n-i):
            if items[k] > items[k+1]:
                items[k], items[k+1] = items[k+1], items[k]
    return items

print(bubble_sort([19, 3, 2, 7, 4,45,9]))
def merge_sort(items):
    
    '''Return array of items, sorted in ascending order'''
    def merge(a, b):     
        index_a = 0     
        index_b = 0     
        c = []     
        while index_a < len(a) and index_b < len(b):         
            if a[index_a] <= b[index_b]:             
                c.append(a[index_a])             
                index_a = index_a + 1         
            else:             
                c.append(b[index_b])             
                index_b = index_b + 1     
        c.extend(a[index_a:])         
        c.extend(b[index_b:])     
        return c
    
    if len(items) == 0 or len(items) == 1: # base case         
        return items[:len(items)] # copy the input      # recursive case     
    
    halfway  = len(items) // 2     
    list1   = items[0:halfway]     
    list2   = items[halfway:len(items)]     
    newlist1 = merge_sort(list1) # recursively sort left half     
    newlist2 = merge_sort(list2) # recursively sort right half     
    newlist  = merge(newlist1, newlist2)     
    return newlist


def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    if not items:
        return []

    pivots = [x for x in items if x == items[0]]
    lesser = quick_sort([x for x in items if x < items[0]])
    greater = quick_sort([x for x in items if x > items[0]])

    return lesser + pivots + greater
