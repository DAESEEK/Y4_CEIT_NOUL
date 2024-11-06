#File manager (remove)
import imp
from os import remove

target_file = 'test.log'

k = input(' Would you like to remove[%s]? '%target_file)
if k =='y':
     remove(target_file)
     print('Success to remove [%s]'%target_file)

