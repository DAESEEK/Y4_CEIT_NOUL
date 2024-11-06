#if + if
age = int(input('나이입력:'))

if age <=7:
     print('유아입니다')
elif age<=19:
     print('청소년입니다')
     if age< 13:
          print('초등학생')
     elif age <16:
          print('중학생')
     else :
          print('고등학생')
else:
     print('성인입니다')

