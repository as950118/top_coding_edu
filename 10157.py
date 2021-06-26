
# 가로 c, 세로 r, 대기번호 k
c, r = map(int, input().split())
k = int(input())

# 범위내에 없을 경우
if c*r < k:
	print(0)
else:
	# 규칙 찾기
	i,j = 0,0
	odd = 0
	start, end = 1, r
	while True:
		if k <= end:
			break
		start = end
		if odd: # 1일때는 행, 0일때는 열
			i += 1
			end += (r-i)
			odd = 0
		else:
			j += 1
			end += (c-j)
			odd = 1

	if odd: # 열 사이에 있음
		# 한바퀴 도는 시점이 2
		if j%2: # 오른쪽일때
			x = c - (j//2)
			x -= (end-k)
		else: # 왼쪽일때
			x = 1 + (j//2)
			x += (end-k)

		if i%2: # 위쪽일때
			y = 1 + (i//2)
		else: # 아래쪽일떄
			y = r - (i//2)

	else: # 행 사이에 있음
		# 한바퀴 도는 시점이 2
		if j%2: # 오른쪽일때
			x = c - (j//2)
		else: # 왼쪽일때
			x = 1 + (j//2)

		if i%2: # 위쪽일때
			y = 1 + (i//2)
			y += (end-k)
		else: # 아래쪽일떄
			y = r - (i//2)
			y -= (end-k)

	print(x, y)





# 직접 찾기
