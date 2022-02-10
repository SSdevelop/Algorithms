def maxSubarray(arr, n):
    max_sum = float('-inf')
    sum = float('-inf')
    low = 0
    high = 0
    currHigh = currLow = 0
    for i in range(n):
        currHigh = i
        if sum > 0:
            sum = sum + arr[i]
        else:
            currLow = i
            sum = arr[i]
        if sum > max_sum:
            max_sum = sum
            low = currLow
            high = currHigh
    
    return (low+1, high+1, int(max_sum))

if __name__ == '__main__':
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    n = len(arr)
    print(maxSubarray(arr, n))
