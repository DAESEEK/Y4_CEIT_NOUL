#import math

def soultion(scores):

    answer = (sum(scores)-min(scores)-max(scores))/(len(scores)-2)

    return answer


scores1 =[35,47,62,44,98,2,55]
ret1=soultion(scores1)


print(ret1)


    
