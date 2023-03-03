l = [1,2,3,4,5,6,7,8,9,10]

def search(l, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return search(l, target, low, mid-1)
    else:
        return search(l, target, mid+1, high)
    
print(search(l, 100, 0, len(l)-1))
