from difflib import diff_bytes


name = input('이름을 써 넣으세요 :')
gender = input('성별을 입력하세요(male or female):')
DateofBirth = input('생년월일(dd/mm/yyyy):')

English = int(input('영어점수를 입력하세요 :'))
Math = int(input('수학점수를 입력하세요 :'))
Language = int(input('국어점수를 입력하세요 :'))
Total = English+Math+Language
Average = Total/3
Epoint = 'F'
Mpoint = 'F'
Lpoint = 'F'


if English > 89:
     Epoint ='A'
elif English > 79:
     Epoint = 'B'
elif English >69:
     Epoint = 'C'
elif English > 59:
     Epoint = 'D'
else :
     Epoint = 'F'

if Math > 89:
     Mpoint ='A'
elif Math > 79:
     Mpoint = 'B'
elif Math >69:
     Mpoint = 'C'
elif Math > 59:
     Mpoint = 'D'
else :
     Mpoint = 'F'

if Language > 89:
     Lpoint ='A'
elif Language > 79:
     Lpoint = 'B'
elif Language >69:
     Lpoint = 'C'
elif Language > 59:
     Lpoint = 'D'
else :
     Lpoint = 'F'


print('=====================================================================')
print('Name : ', name,'    gender: ',gender,'   Date of Birth: ',DateofBirth)
print('=====================================================================')
print('English :  ',English, '    Point:    ',Epoint)
print('Math    :  ',Math,    '    Point:    ',Mpoint)
print('Language:  ',Language,'    Point:    ',Lpoint)
print('======================================================================')
print('Total   : ',Total,   '    Ave  : %.2f '%Average)
print('======================================================================')
