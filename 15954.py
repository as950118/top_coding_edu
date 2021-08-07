'''
문제정의
일렬로 정렬된 인형들을 연속으로 k개 이상 골랐을떄 
표준편차가 최소가 되는 값을 출력
'''
import math

# 표준편차 구하기
def mean(arr):
	return sum(arr)/len(arr)

def variance(arr):
	m = mean(arr)
	ret = 0
	for elem in arr:
		ret += (elem - m) ** 2
	return ret/len(arr)

def std(var):
	return math.sqrt(var)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ret_list = []
for i in range(n -k + 1):
	for j in range(n - k -i + 2):
		temp = arr[i:i+k+j]
		var = variance(temp)
		ret_list.append(var)
ret = min(ret_list)
print(std(ret))
