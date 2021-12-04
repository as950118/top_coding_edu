'''
문제정의
다각형의 면적구하기
'''
'''
문제해결방법
1. 가장 큰 사각형 구하기
2. 빈공간을 만드는 좌표들을 찾기
3. 빈공간의 크기를 구하는 방식
'''

N = int(input())
arr_x = []
arr_y = []
ret = 0
for i in range(N):
	x,y = map(int, input().split())
	arr_x.append(x)
	arr_y.append(y)
arr_x.append(arr_x[0])
arr_y.append(arr_y[0])
for i in range(N):
	ret += (arr_x[i]*arr_y[i+1]-(arr_x[i+1]*arr_y[i]))
print(round(abs(ret/2),1))

