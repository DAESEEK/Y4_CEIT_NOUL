# 짝수 홀수
#num = int(intput("숫자를 입력하시요 : "))

#if num % 2==0 :
 #    print("짝수입니다.")
#else :
 #   print("홀수입니다.")

# 나이를 입력하세요.....
age = int(input("Enter your age : "))

if age < 9:
     print( " kids")
elif age < 18:
     print (" teenager")
else :
     print (" adult ")

text = input("Enter some letter:")

if text==text.upper():
     print(text.lower())
elif text==text.lower():
     print(text.upper())
else :
     print("It is impossible")

msg = input('Enter the sentence: ')

if 'is' in msg:
     print('msg has is')
else:
     print('msg has not is')

