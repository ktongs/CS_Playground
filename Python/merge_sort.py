def sort(arr):
    if arr[0] <= arr[1]:
        return arr
    else:
        return arr[::-1]

def merge(a,b):
    a_length = len(a)
    b_length = len(b)
    c = []
    i=j=0
    while(i < a_length) and (j < b_length):
        if a[i] <= b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while (i<a_length):
        c.append(a[i])
        i += 1
    while (j<b_length):
        c.append(b[j])
        j+=1
    return c
def merge_sort(unsorted_list):
    if len(unsorted_list) == 2:
        return sort(unsorted_list)
    elif len(unsorted_list) <= 1:
        return unsorted_list
    else:
        length = len(unsorted_list)
        return merge(merge_sort(unsorted_list[0:length//2]),merge_sort(unsorted_list[length//2:]))

print(merge_sort([1,3,2,8,4,7]))
print(merge_sort([]))
print(merge_sort([1,2,3]))
print(merge_sort([3,2,1]))
print(merge_sort([2,2,3]))
print(merge_sort([1,-3,2,0,4,7]))

