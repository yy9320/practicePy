#!/usr/bin/env python 
# -*- coding:utf-8 -*-


marks = [90, 25, 67, 45, 80]

for i in marks:
	if i>60:
		print("합격")
		print("이사람 점수는 %d 점 입니다" %i)
	else:
		print("불합격")
		print("이사람 점수는 %d점 입니다." %i)
