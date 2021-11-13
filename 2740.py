'''
문제정의
행렬의 곱셈
'''
'''
행렬의 곱셈방식
앞의 행렬의 열의 갯수와
뒤의 행렬의 행의 갯수가 일치할때 계산가능
그 결과값은
앞의 행렬의 행의 갯수와
뒤의 행렬의 열의 갯수로 형태로 나온다
'''
matrix = []
# 첫번쨰 행렬
N,M = map(int, input().split())
temp_matrix = []
for i in range(N):
	temp = list(map(int, input().split()))
	temp_matrix.append(temp)
matrix.append(temp_matrix)

# 두번째 행렬
M,K = map(int, input().split())
temp_matrix = []
for i in range(M):
	temp = list(map(int, input().split()))
	temp_matrix.append(temp)
matrix.append(temp_matrix)

ret_matrix = []
for n in range(N):
	for k in range(K):
		temp = 0
		for m in range(M):
			temp+=matrix[0][n][m]*matrix[1][m][k]
		print(temp, end=" ")
	print()

