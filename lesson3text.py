text1 = '영광이 바보 똥꼬야'
text2 = str('hello')
text3 = " "

print(text1,text2,text3)
#양수 인덱스
print(text1[0])
print(text1[1])
print(text1[2])
print(text1[3])
print(text1[4])
#음수
print(text1[-5])
print(text1[-4])
print(text1[-3])
print(text1[-2])
print(text1[-1])

#문자열 슬라이스

print(text1[2:5]) # 5번 전까지  (5번 미포함)
print(text1[1:8])
print(text1[-5:-1])

print(text1[0:8:2])
