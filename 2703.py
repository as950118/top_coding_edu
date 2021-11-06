'''
문제정의
암호화된 메시지와 문자사이의 규칙이 주어졌을때
원본 메시지를 구하는 프로그램
'''
'''
문제해결방법
암호규칙을 딕셔너리로 저장해서 치환하기
'''
import string
alpha = string.ascii_uppercase
T = int(input())
for i in range(T):
	msg = input() # 암호화된 메시지
	rule = input()
	dic_rule = dict()
	for idx, i in enumerate(rule):
		dic_rule[alpha[idx]] = i

	ret = '' # 원본 메시지
	for i in msg:
		if i == ' ':
			ret += ' '
		else:
			ret += dic_rule[i]
	print(ret)
