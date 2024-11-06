def binary_search(element, some_list):
    # 코드를 작성하세요.
    first = 0
    last = len(some_list)
    count = 0
    while(first != last):
        count+=1
        standard = (first + last)//2   
        if some_list[standard] == element:
          #  print("Count:",count)
            return standard
        elif some_list[standard] < element: #찾는 값이 중간값보다 더 큼
            first = standard
        else:   #찾는 값이 중간값보다 더 작음
            last = standard
    #print("Count:",count)
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))