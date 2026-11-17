def cycleSort(arr):
    
    n = len(arr)
    i = 0

    while i < n:
        
        correct = arr[i] - 1
        
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            
            i += 1

if __name__ == "__main__":
    arr = [3, 2, 4, 5, 1]
    n = len(arr)

    cycleSort(arr)

    for i in range(n):
        print(arr[i], end=" ")