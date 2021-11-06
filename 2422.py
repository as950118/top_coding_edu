'''
문제정의
N개중에서 3개를 택하는 경우들 중에
제외해야하는 3개 집합을 제외한 경우의 수
'''
'''
문제해결방법
1. N개 아이스크림에 대한 조합(combination) 구하기
2. 맛이없는 조합이 포함된 조합은 제외
'''
'''
순열(permutation)과 조합(combination)의 차이
순열 : 순서를 고려
조합 : 순서를 고려하지 않음
예 : 1,2,3 / 2,3,1 집합이 있을때
순열은 둘이 다르다고 판단
조합은 둘이 같다고 판단
'''
n,m = map(int, input().split())
icecream = [i for i in range(1,n+1)]
no_mat = {i:[] for i in range(1,n+1)}
for i in range(m):
	num1, num2 = map(int, input().split())
	num1, num2 = min(num1, num2),max(num1, num2)
	no_mat[num1].append(num2)

ret = 0
for i in range(1, n+1-2):
	for j in range(i+1, n+1-1):
		if j in no_mat[i]:
			continue
		for k in range(j+1, n+1):
			if k in no_mat[i] or k in no_mat[j]:
				continue
			else:
				ret += 1

print(ret)






