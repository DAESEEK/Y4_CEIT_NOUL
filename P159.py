from time import localtime

weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

t=localtime()
today ='%d-%d-%d' %(t.tm_year,t.tm_mon,t.tm_mday)
week = weekdays[t.tm_wday]

print('[%s] It is [%s].'%(today,week))