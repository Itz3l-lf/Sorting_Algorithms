def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def printArray(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    printArray(arr)
    
    selectionSort(arr)
    
    print("Sorted array: ", end="")
    printArray(arr)