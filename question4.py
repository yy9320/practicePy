#!/usr/bin/env python 
# -*- encoding:utf-8 -*-
import os
# 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수를 작성하라
def is_odd(a):
	if a%2 == 0:
		print("짝수");
	else :
		print("홀수");
is_odd(4);

#람다로
is_odd2 = lambda x: print("홀수") if x % 2 == 1  else print("짝수") 
is_odd2(2);
is_odd2(3);


# 2. 입력으로 들어오는 모든 수의 평균 값을 계산해주는 함수를 작성해 보자.
sum = 0;

def sum_numbers(*args):
	sum = 0;
	for i in args:	
		print(i, end=' ')	
		sum += i
	print("평균은 %d 입니다" %(sum/len(args)))
	return sum/len(args)

sum_numbers(1,2,3,4,5)
sum_numbers(2,3,4,5,6.7)

# 6. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해보자 
# 단프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한
# 내용을 추가해야한다. 
inputData = input("저장할 내용을 입력하세요");
f = open("test.txt","a"); # 추가적으로 입력하려면 a
f.write(inputData);
f.write("\n");
f.close();

# 7.다음과 같은 내용을 지닌 파일 test.txt가 있다.
# 이 파일의 내용 중 "java" 라는 문자열을 "python"으로 바꾸어서 저장해보자
#file = './test2.txt';

#if os.path.isfile(file):
#	os.remove(file)

f7 = open("test2.txt", "w");
f7.write("Life is too short");
f7.write("\n you need java");
f7.close();

after = open("test2.txt", "r");
body = after.read();
print(body);
after.close();

after_file = open("test2.txt", "w");
body = body.replace("java", "python");
print(body);
after_file.write(body);
after_file.close();
