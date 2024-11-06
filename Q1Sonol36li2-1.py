print("Enter the number(under 100)")
n = int(input())

li =[100, n]
i=1



while li[i]>=0:
    li.append(li[i-1]-li[i])
    i+=1


print(*li)
