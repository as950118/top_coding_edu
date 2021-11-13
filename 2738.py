'''
문제정의
행렬 계산
'''
'''
행렬=2차원 리스트
'''
n,m = map(int, input().split())

matrix = []
# 첫번째 행렬
temp_matrix = []
for i in range(n):
	temp = list(map(int, input().split()))
	temp_matrix.append(temp)
matrix.append(temp_matrix)

# 두번째 행렬
temp_matrix = []
for i in range(n):
	temp = list(map(int, input().split()))
	temp_matrix.append(temp)
matrix.append(temp_matrix)

ret_matrix = []
# first_matrix = matrix[0]
# second_matrix = matrix[1]
for i in range(n):
	temp_row = []
	for j in range(m):
		temp = matrix[0][i][j] + matrix[1][i][j]
		temp_row.append(temp)
	ret_matrix.append(temp_row)

for i in range(n):
	for j in range(m):
		print(ret_matrix[i][j], end=" ")
	print("")



