#ມັນເປັນໂຄງການທີ່ກ່ຽວຂ້ອງກັບເວລາ. It is a time-related program.
from time import localtime,strftime

logfile = 'test.log'
def writelog(logfile,log):
     time_stamp =strftime('%Y-%m-%d %X\t',localtime())
     log = time_stamp+log+ '\n'

     with open(logfile,'a') as f:
          f.writelines(log)

writelog(logfile,'The 5 login setance')

a =strftime('%Y-%m-%d %H:%M:%S',localtime())
b =strftime('%x %X',localtime())
print(a)
print(b)
c = localtime()

d = c.tm_wday
print(d)
#tm_year tm_mon tm_hour tm_mday
#tm_hour
#tm_min
#tm_sec



