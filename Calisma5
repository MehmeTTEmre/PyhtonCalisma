liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

def binarySearch(arr,x):
    if len(arr) == 1:
        return arr[0] == x
    
    if arr[len(arr)//2] == x:
        return True
        
    if arr[len(arr)//2] > x:
        return binarySearch(arr[:len(arr)//2],x)
    else:
        return binarySearch(arr[len(arr)//2:],x)
        
print(binarySearch(liste,17))        
