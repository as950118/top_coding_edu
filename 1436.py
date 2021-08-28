'''
문제정의
6이 3개이상 반복되는 숫자들 중에서
작은 숫자부터 순서를 매겨서
N번째에 해당하는 숫자가 무엇인지 출력
'''
'''
문제해결방법
브루트포스로 전수조사
666부터 시작하고
'''
N = int(input())
cur_number = 666
count = 0
while True:
	if str(cur_number).find('666') != -1:
		count += 1
	if count == N:
		break
	cur_number += 1
print(cur_number)

