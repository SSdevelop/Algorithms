import math


class Search:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
    
    def linear_search(self, val):
        for i in range(self.n):
            if self.arr[i] == val:
                return i
        return -1
    
    def binary_search_iterative(self, val):
        l = 0
        h = self.n - 1

        while l <= h:
            mid = l + (h - l) // 2
            if self.arr[mid] == val:
                return mid
            elif val > self.arr[mid]:
                l = mid + 1
            else:
                h = mid - 1
        
        return -1
    
    def __binary_search_rec(self, val, l, h):
        if h >= l:
            mid = l + (h - l) // 2
            if self.arr[mid] == val:
                return mid
            elif val > self.arr[mid]:
                return self.__binary_search_rec(val, mid + 1, h)
            else:
                return self.__binary_search_rec(val, l, mid + 1)
        else:
            return -1
    
    def binary_search_recurssive(self, val):
        return self.__binary_search_rec(val, 0, self.n - 1)
    
    def jump_search(self, val):
        step = math.sqrt(self.n)
        prev = 0
        while self.arr[int(min(step, self.n))] < val:
            prev = step
            step += math.sqrt(self.n)
            if prev >= self.n:
                return -1
        
        while self.arr[int(prev)] < val:
            prev += 1
            if prev == min(step, self.n):
                return -1
        
        if self.arr[int(prev)] == val:
            return int(prev)
        
        return -1

