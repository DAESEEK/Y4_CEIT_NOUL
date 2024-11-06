def fahrenheit_to_celsius(fahrenheit):
     return round((fahrenheit-32)*5/9,1)


temperature_list =[40,15,32,64,-4,11]
print("Fahreheit list: {}".format(temperature_list))

i= 0
cnt = len(temperature_list)
cel=[]

while i < cnt:
     temp=temperature_list[i]
     cel.append((fahrenheit_to_celsius(temp)))
     i +=1
     
print("celsius list : {}".format(cel))
