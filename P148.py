from hashlib import new
from os import rename

target_file='bbb.txt'

newname = input('[%s] enter new file name:'%target_file)
rename(target_file,newname)

print('[%s]--[%s] File namw was changed'%(target_file,newname))
