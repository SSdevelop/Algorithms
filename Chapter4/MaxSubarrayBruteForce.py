import sys
import time
def maxSubarray(arr, n):
    max_sum = float('-inf')
    low = 0
    high = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum > max_sum:
                max_sum = sum
                low = i
                high = j
    return (low + 1, high + 1, int(max_sum))

if __name__ == '__main__':
    start = time.time()
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    n = len(arr)
    print(maxSubarray(arr, n))
