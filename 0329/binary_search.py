def binary_search(element, some_list):
    # 코드를 작성하세요.
    middle = len(some_list)//2
    start = 0
    end = len(some_list)-1
    for i in range(len(some_list)):
        if element == some_list[middle]: return middle
        elif element < some_list[middle]: 
            end = middle-1
        elif element > some_list[middle]:
            start = middle+1
        middle = (start + end)//2

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))