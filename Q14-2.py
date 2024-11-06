import time

# start_time = time.time()

num = int(input('number?'))
i=1
sum1=0
start_time = time.time()
while i<=num:
     sum1 = sum1+i
     i=i+1

print(sum1)
end_time = time.time()
t=end_time-start_time
print("time : %f " %t)


