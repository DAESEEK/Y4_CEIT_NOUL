from urllib.request import urlopen

imgurl = 'https://cphoto.asiae.co.kr/listimglink/6/2018060715520673255_1528354326.jpg'
imgname = imgurl.split('/')[-1]
print(imgname)
try:
     with urlopen(imgurl) as f:
          with open(imgname,'wb') as h:
               img = f.read()
               h.write(img)
except Exception as e:
     print(e)
