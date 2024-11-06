from datetime import datetime

start = datetime.now()
print('Add from one to a million. ເພີ່ມຈາກ 1 ເປັນລ້ານ.')
ret =0
for i in range(1000000):
     ret+=i
print(' Result to add 1 to 1,000,000: %d'%ret)
end=datetime.now()
elapsed=end-start
print(start,'  ',end)
print('total processing time:',end='');print(elapsed)
elapsed_ms=int(elapsed.total_seconds()*1000)
print('total processing time:%dms'%elapsed_ms)