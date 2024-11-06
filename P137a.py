# ໂຄງ​ການ​ນີ້​ແມ່ນ​ໂຄງ​ການ​ທີ່​ອ່ານ​ໄຟລ​໌​ອື່ນໆ​.
f =open('a.txt','r')
lines= f.readlines()
for line_num, line in enumerate(lines):
     print('%d %s' %(line_num+1,line),end='')
f.close()
