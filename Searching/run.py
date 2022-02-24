from search import Search

if __name__ == '__main__':
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    obj = Search(arr)
    # print(obj.arr)
    print(obj.linear_search(55))
    print(obj.binary_search_iterative(55))
    print(obj.binary_search_recurssive(55))
    print(obj.jump_search(55))
    print(obj.interpolation_search(55))
    print(obj.exponential_search(55))
    print(obj.exponential_search(55))
