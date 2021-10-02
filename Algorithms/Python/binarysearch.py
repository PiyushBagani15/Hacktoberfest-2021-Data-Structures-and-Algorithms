#binary search with position
position = -1
def search(arr,n):
    l=0
    u=len(arr)-1
    while l<=u:
        mid=(l+u)//2
        if arr[mid] == n:
            globals()['position']=mid
            return  True
        else:
            if arr[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return  False
arr = [1,2,5,6,7,9]
n=12
if search(arr,n):
    print("found",position)
else:
    print("not found")
