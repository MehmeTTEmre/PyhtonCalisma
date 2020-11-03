liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

def controlEleman(arr,eleman):
    for i in arr:
        if i == eleman:
            return True
    return False
    
print(controlEleman(liste,12))
