def liner_search(element,some_list):
   for i in range(len(some_list)):
        if element in some_list:  # if some_list[i]==element:
             return some_list.index(element) # return i
        else:
             return None
     
     
print(liner_search(2,[2,3,5,7,11]))
print(liner_search(0,[2,3,5,7,11]))
print(liner_search(5,[2,3,5,7,11]))
print(liner_search(3,[2,3,5,7,11]))
print(liner_search(11,[2,3,5,7,11]))


