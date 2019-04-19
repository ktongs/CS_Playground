def bisectional_search(list,number):
    if len(list) is 0:
        return False
    end = len(list)-1
    start = 0
    mid = (end-start)//2
    while list[mid] != number:
        if end-start == 0:
            return False
        if list[mid] < number:
            start = mid+1

        elif list[mid] > number:
            end = mid

        mid = (end+start)//2
    return mid

print(bisectional_search([1,2,4,5,6,7,8],4))
print(bisectional_search([],1))
print(bisectional_search([-1,0,4,6],1))
print(bisectional_search([-1,0,4,5,6,7],7))