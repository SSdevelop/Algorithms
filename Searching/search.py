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
    
    def interpolation_search(self, val):
        l = 0
        h = self.n - 1
        while l <= h and val >= self.arr[l] and val <= self.arr[h]:
            pos = l + ((h - l) // (self.arr[h] - self.arr[l]) * (val - self.arr[l]))

            if self.arr[pos] == val:
                return pos
            
            elif self.arr[pos] < val:
                l = pos + 1
            
            else:
                h = pos - 1
        
        return -1
    
    def exponential_search(self, val):
        if self.arr[0] == val:
            return 0
        
        i = 1
        while i < self.n and self.arr[i] < val:
            i = i * 2
        
        return self.__binary_search_rec(val, i // 2, min(i, self.n-1))
    
    def ternary_search(self, val):
        # does more comparisions than binary search
        l = 0
        h = self.n - 1
        while h >= l:
            mid1 = l + (h - l) // 3
            mid2 = mid1 + (h - l) // 3
            
            if self.arr[mid1] == val:
                return mid1
            elif self.arr[mid2] == val:
                return mid2
            elif self.arr[mid1] > val:
                h = mid1 - 1
            elif self.arr[mid2] < val:
                l = mid2 + 1
            else:
                l = mid1 + 1
                h = mid2 - 1
        return -1


