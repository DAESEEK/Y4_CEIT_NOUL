numstr = input('enter the number:')
try:
     num = int(numstr)
     print('your num is <%d>' %num)

except:
     try:
          num = float(numstr)
          print('your number is <%f>'%num)
     except:
          print('+enter the number')