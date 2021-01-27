#!/usr/bin/env python
# -*- coding:utf-8 -*-
print('11')

coffee = 10;
while True:
	money = int(input("돈을 넣어주세요"))
	if money == 300:
		print("커피를 드립니다.")
		coffee = coffee-1
	elif money < 300:
		print("돈이 모자랍니다")
	elif money > 300:
		print("거스름돈은 %d이만큼" %(money-300))
		coffee = coffee-1

	if coffee == 0:
		print("이제 커피가 없습니다. ")
		break
	else: 
		print("커피재고는 %d개 입니다" %coffee)

