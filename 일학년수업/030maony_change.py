# This program is a program that refunds the difference in money paid.

def calculate_payment(payment,cost):
     change = payment - cost #거스름돈 총액
     
     hundred_thousand_count = change // 100000
     fifty_thousand_count = (change%100000)//50000
     ten_thousand_count = (change%50000)//10000
     five_thousand_count = (change%10000)//5000
     two_thousand_count = (change%5000)//2000
     one_thousand_count = (change%2000)//1000
     
     print("100000kip : {}".format(hundred_thousand_count))
     print(" 50000kip : {}".format(fifty_thousand_count))
     print(" 10000kip : {}".format(ten_thousand_count))
     print("  5000kip : {}".format(five_thousand_count))
     print("  2000kip : {}".format(two_thousand_count))
     print("  1000kip : {}".format(one_thousand_count))
     
     
calculate_payment(1177000,750000)