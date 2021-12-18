'''
문제정의
2차원 평면의 숫자들을 고르게 만들기
를 최소시간안에 수행
깍기 : 2초
채우기 : 1초
단, 채우기는 채울 숫자가 있어야함
'''
'''
문제해결방법
최악의 경우

'''
import sys
input = sys.stdin.readline
n,m,b = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
ret = 10**8
layer = 0
for i in range(256+1):
	mow = 0
	fill = 0
	for row in arr:
		for elem in row:
			if elem > i:
				mow += elem-i
			else:
				fill += i-elem
	# 가능여부
	if fill > mow + b:
		continue
	tmp = mow*2 + fill
	if ret >= tmp:
		ret = tmp
		layer = i
		# print(f"{i}층 : {mow}, {fill}")
print(ret, layer)
