def count_sort(arr):
    if not arr:
        return []

    n = len(arr)
    maxval = max(arr)

    cntArr = [0] * (maxval + 1)

    for v in arr:
        cntArr[v] += 1

    for i in range(1, maxval + 1):
        cntArr[i] += cntArr[i - 1]

    ans = [0] * n

    for i in range(n - 1, -1, -1):
        v = arr[i]
        ans[cntArr[v] - 1] = v
        cntArr[v] -= 1

    return ans

if __name__ == "__main__":
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    ans = count_sort(arr)
    print(ans)