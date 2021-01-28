#!/usr/bin/env python
# -*- encoding:utf-8 -*-

a =1 
def add(a,b) :
	a = a+b
	return a

print("덧셈전 a는 지금 %d 입니다" %a)
a = add(3,5)
print("덧셈후 a는 지금 %d입니다." %a)


mul = 10
def multiplication(a,b):
	mul = a*b
	return mul

print("곱셈을 하기 전 mul의 값은 %d" % mul)
mul = multiplication(3,5)
print("곱셈후 mul의 값은 %d" % mul)

# 이 실습의 교훈 : 글자를 출력하고자 할때에는
# 자바와 달라서 + mul해서는 글자가 나오지 않고
# 오류가 출력되니 유의하여 사용하도록 !


