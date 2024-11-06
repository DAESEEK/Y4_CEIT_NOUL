text = input('파일에 저장할 내용을 입력하세요: ')
f = open('mydata.txt', 'w')
f.write(text)
f.close()

# 저장한 파일 내용 확인하기
h = open('mydata.txt', 'r')
text = h.read()
print(text)
h.close()
