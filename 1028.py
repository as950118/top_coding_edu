'''
 문제정의
0,1로 이루어진 2차원 배열에서
1로 이루어진 다이아몬드 모양의 최대 크기 찾기 
'''
'''
 해결방법
1. 큰거부터 다 찾아보기(컴퓨팅 파워)
2. 알고리즘 활용
'''
'''
1. 1*1 + 3*3 + 5*5 = 2*n//2(n//2+1)(n+1)/6 = n^3
'''
'''
2. 
'''
# (r, c)를 시작점으로 했을 때 특정 방향으로 1이 최대 몇개까지 이어지는지
d1 = [[-1] * 1000 for i in range(1000)] # 북동
d2 = [[-1] * 1000 for i in range(1000)] # 남동
d3 = [[-1] * 1000 for i in range(1000)] # 남서
d4 = [[-1] * 1000 for i in range(1000)] # 북서
# row와 column 입력받기
R, C = map(int, input().split())
# 광산 지도 입력받기
arr = []
for i in range(R):
	temp = list(map(int, input()))
	arr.append(temp)
def outOfBoundary(cur_r, cur_c):
	return cur_r<0 or cur_r>=R or cur_c<0 or cur_c>=C
for i in range(R+C+1):
	for cur_c in range(C):
		cur_r = i - cur_c
		if outOfBoundary(cur_r, cur_c):
			continue
		if outOfBoundary(cur_r+1, cur_c-1):
			if arr[cur_r][cur_c] == 1:
				d3[cur_r][cur_c] = 1
			else:
				d3[cur_r][cur_c] = 0
		else:
			if arr[cur_r][cur_c]==1:
				d3[cur_r][cur_c] = d3[cur_r+1][cur_c-1]+1
			else:
				d3[cur_r][cur_c] = 0
	for cur_r in range(R):
		cur_c = i - cur_r
		if outOfBoundary(cur_r, cur_c):
			continue
		if outOfBoundary(cur_r-1, cur_c+1):
			if arr[cur_r][cur_c] == 1:
				d1[cur_r][cur_c] = 1
			else:
				d1[cur_r][cur_c] = 0
		else:
			if arr[cur_r][cur_c]==1:
				d1[cur_r][cur_c] = d1[cur_r-1][cur_c+1]+1
			else:
				d1[cur_r][cur_c] = 0

for j in range(1-C, R):
	# 북서
	for cur_r in range(R):
		cur_c = cur_r - j
		# 범위를 벗어난 경우
		if outOfBoundary(cur_r, cur_c):
			continue
		# 끝지점인 경우
		if outOfBoundary(cur_r-1, cur_c-1):
			if arr[cur_r][cur_c] == 1:
				d4[cur_r][cur_c] = 1
			else:
				d4[cur_r][cur_c] = 0
		else:
			if arr[cur_r][cur_c]==1:
				d4[cur_r][cur_c] = \
				d4[cur_r-1][cur_c-1]+1
			else:
				d4[cur_r][cur_c] = 0
	# 남동
	for cur_r in range(R-1, -1, -1):
		cur_c = cur_r - j
		# 범위를 벗어난 경우
		if outOfBoundary(cur_r, cur_c):
			continue
		# 끝지점인 경우
		if outOfBoundary(cur_r+1, cur_c+1):
			if arr[cur_r][cur_c] == 1:
				d2[cur_r][cur_c] = 1
			else:
				d2[cur_r][cur_c] = 0
		else:
			if arr[cur_r][cur_c]==1:
				d2[cur_r][cur_c] = \
				d2[cur_r+1][cur_c+1]+1
			else:
				d2[cur_r][cur_c] = 0

MAX = 0
for cur_r in range(R):
	for  cur_c in range(C):
		temp = min(d1[cur_r][cur_c], d2[cur_r][cur_c])
		if temp<MAX:
			continue
		for i in range(temp, MAX, -1):
			if cur_c + 2 * (i-1) >= C:
				continue
			if min(d3[cur_r][cur_c+2*(i-1)], 
				d4[cur_r][cur_c+2*(i-1)]) >= i:
				MAX = max(MAX, i)
				break
print(MAX)
