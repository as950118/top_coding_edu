'''
문제정의
점 3개가 주어졌을떄
다른 점 1개를 추가해서 만들수있는 평행사변형중에서
둘레가 가장 작은 것과
둘레가 가장 큰 것의 
둘레차이를 차이를 출력
'''
'''
문제해결방법
1. 평행사변형을 만드는 점들의 위치를 찾기
2. 해당하는 점들을 토대로 만든 평행사변형의 둘레들 구하기
3. 최대-최소값 출력
'''

# 점들의 위치를 다양한 자료구조를 이용해서 받아보기
dots = {}
dots['A'] = {}
dots['A']['x'] = None
dots['A']['y'] = None
dots['B'] = {}
dots['B']['x'] = None
dots['B']['y'] = None
dots['C'] = {}
dots['C']['x'] = None
dots['C']['y'] = None

dots['A']['x'],dots['A']['y'],dots['B']['x'],dots['B']['y'],dots['C']['x'],dots['C']['y'] = map(int, input().split())
# ax, ay, bx, by, cx, cy =  map(int, input().split())

# D를 찾는 과정
# 1. AB와 CD를 각각 윗변과 밑변으로 가지는경우
# 2. AC와 BD를 각각 윗변과 밑변으로 가지는경우
# 3. AD와 CB를 각각 윗변과 밑변으로 가지는경우

# dots['D'] = {}
# dots['D']['x'] = []
# dots['D']['y'] = []

# def findD(first,second,third):
# 	dif_x = first['x'] - second['x']
# 	dif_y = first['y'] - second['y']

# 	x = []
# 	y = []
# 	x.append(third['x'] + dif_x)
# 	y.append(third['y'] + dif_y)
# 	x.append(third['x'] - dif_x)
# 	y.append(third['y'] - dif_y)

# 	return x, y

# x, y = findD(dots['A'],dots['B'],dots['C'])
# dots['D']['x'] += x
# dots['D']['y'] += y
# x, y = findD(dots['B'],dots['C'],dots['A'])
# dots['D']['x'] += x
# dots['D']['y'] += y
# x, y = findD(dots['C'],dots['A'],dots['B'])
# dots['D']['x'] += x
# dots['D']['y'] += y

def findRound(a,b,c):
	lines = []
	line = ((a['x']-b['x'])**2 + (a['y']-b['y'])**2)**0.5
	lines.append(line)
	line = ((b['x']-c['x'])**2 + (b['y']-c['y'])**2)**0.5
	lines.append(line)
	line = ((c['x']-a['x'])**2 + (c['y']-a['y'])**2)**0.5
	lines.append(line)
	return lines
# 평행사변형이 안되는 경우
# 겹치는 점이 있는 경우
clash = dots['A'] == dots['B'] 
clash = clash or dots['B'] == dots['C']
clash = clash or dots['C'] == dots['A']

# 한줄에 있는 경우 == 기울기가 같은경우
clash = clash or (dots['A']['x'] - dots['C']['x']) * (dots['A']['y'] - dots['B']['y']) == \
(dots['A']['x'] - dots['B']['x']) * (dots['A']['y'] - dots['C']['y']):
if clash:
	print(-1)
else:
	lines = findRound(dots['A'],dots['B'],dots['C'])
	ret_max = max(lines[0]+lines[1], lines[1]+lines[2], lines[2]+lines[0])
	ret_min = min(lines[0]+lines[1], lines[1]+lines[2], lines[2]+lines[0])
	print( (ret_max-ret_min) * 2)



















