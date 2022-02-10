import sys
import time

def maxCrossSubarray(arr, low, mid, high):
    left_sum = float('-inf')
    max_left = -1
    sum = 0
    for i in range(mid, low, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    right_sum = float('-inf')
    max_right = -1
    sum = 0
    for i in range(mid+1, high+1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    
    return (max_left, max_right, left_sum + right_sum)
    
    

def maxSubarray(arr, low, high):
    if high == low:
        return (low, high, arr[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = maxSubarray(arr, low, mid)
        (right_low, right_high, right_sum) = maxSubarray(arr, mid+1, high)
        (cross_low, cross_high, cross_sum) = maxCrossSubarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low+1, left_high+1, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low+1, right_high+1, right_sum)
        else:
            return (cross_low+1, cross_high+1, cross_sum)

if __name__ == '__main__':
    start = time.time()
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    n = len(arr)
    print(maxSubarray(arr, 0, n-1))
