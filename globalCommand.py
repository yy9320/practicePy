#!/usr/bin/env python
# -*- encoding:utf-8 -*-


# 글로벌 명령어 써보기 
# 글로벌 명령어는 안에서 한번 더 선언해주어야하나봄

a = 1
def vartest():
	global a
	a = a+1

vartest()
print(a)


# 람다 써보기 

add = lambda a,b :a+b
multiplication = lambda a,b :a*b

result1 = add(2,3)
result2 = multiplication(2,3)

print("result1 = a+b : %d " %result1)
print("result2 = a*b : %d " %result2) 
