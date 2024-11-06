def flip(some_list):
     middle_index = len(some_list)//2
     if len(some_list)==1:
          return some_list
     return flip(some_list[middle_index])+flip(some_list[:middle_index])


some_list =[1,2,3,4,5,6,7,8,9]
some_list = flip(some_list)
print(some_list)
