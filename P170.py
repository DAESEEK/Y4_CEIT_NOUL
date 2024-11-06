from urllib.request import urlopen

url = 'http://lkclaos.org/department-of-korean-language/'
with urlopen(url) as f:
     doc = f.read().decode()
     print(doc)