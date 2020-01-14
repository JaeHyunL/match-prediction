coffee = 10
money = int(input("자판기에 동전을 넣어주세요 : "))
while True:
   if money == 300 :
        print("주문하신 밀크커피 제작중입니다")
        coffee = coffee-1
   elif money > 300 :
        print('밀크커피')
      #print("거스름돈은 %d 입니다 맛있게드세여" %money-300)
        coffee = coffee -1
   else:
      print("금액이 부족합니다 더 넣어주세요 : ")
      break