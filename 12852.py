'''
문제정의
어떤 X가 주어졌을떄
3가지 연산을 활용하여 
최소한의 연산 횟수로 1을 만들기
'''
'''
문제해결방법
1. 순서대로 하나씩 해보기 (X)
2. 3의 배수로 만들기 (Case by Case) -> (경우의수 많음) 
3. bfs
4. memorization 활용
'''

X = int(input())
# 1번 방법
def first_solution(X, count):
	if X == 1:
		return count
	if X%3 == 0:
		return first_solution(X//3, count+1)
	if X%2 == 0:
		return first_solution(X//2, count+1)
	else:
		return first_solution(X-1, count+1)

# print(first_solution(X,0))

# 2번 방법
# arr = [3**i for i in range(13)]
def second_solution(X, count):
	print(X)
	if X in arr:
		return count + arr.index(x)
	else:		
		if X%2 == 0 and ((X//2)%3 == 0):
			return first_solution(X//2, count+1)
		else:
			return first_solution(X-1, count+1)
# print(second_solution(X, 0))

# 3번 방법
# from collections import deque

# queue = deque()
# queue.append([X])
# answer = []

# while 1:
# 	cur = queue.popleft()
# 	x = cur[-1]
# 	if x == 1:
# 		answer = cur
# 		break

# 	if x%3 == 0:
# 		tmp = cur + [x//3]
# 		queue.append(tmp)

# 	if x%2 == 0:
# 		tmp = cur + [x//2]
# 		queue.append(tmp)

# 	tmp = cur + [x-1]
# 	queue.append(tmp)

# print(len(answer) - 1)
# print(*answer)

# 4번방법
result = [[0,[]] for i in range(X+1)]
result[1][0] = 0 # 최소값
result[1][1] = [1] # 경로

for i in range(2, X+1):
	result[i][0] = result[i-1][0] + 1 # count
	result[i][1] = result[i-1][1] + [i] # 경로

	if i%3==0 and result[i//3][0]+1<result[i][0]:
		result[i][0] = result[i//3][0] + 1 # count
		result[i][1] = result[i//3][1] + [i] # 경로

	if i%2==0 and result[i//2][0]+1<result[i][0]:
		result[i][0] = result[i//2][0] + 1 # count
		result[i][1] = result[i//2][1] + [i] # 경로

print(result[X][0]) # 최소경로
print(*result[X][1][::-1])
