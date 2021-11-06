import sys
input = sys.stdin.readline # 시간절약

n = int(input())
S = set() # 중복을 허용하지 않음
for i in range(n):
	inp = input().strip().split()
	if len(inp) == 1:
		func = inp[0]
	else:
		func, param = inp[0], int(inp[1]) # parameter는 숫자로 바꿔주기

	if func=='all':
		S = set([i for i in range(1,21)])		
	elif func=='empty':
		S = set()
	elif func=='add':
		S.add(param)
	elif func=='remove':
		S.discard(param) # 오류없이 제거
	elif func=='check':
		print(1 if param in S else 0)
	elif func=='toggle':
		S.discard(param) if param in S else S.add(param)
		
