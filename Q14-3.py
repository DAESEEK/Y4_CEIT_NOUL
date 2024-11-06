import time
num= int(input('number?'))
start_time = time.time()
while num !=0:
     print('positive integer' if num >0 else 'negative number')
     num= int(input('number?'))

end_time = time.time()
#t = end_time-start_time
print("time : ", end_time-start_time)
     