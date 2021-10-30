'''
문제정의
2개의 명단을 입력받아서
중복되는 이름 찾기
'''
'''
문제해결방법
A명단과 B명단을 입력받고
A명단과 B명단을 1개씩 비교
'''
N,M = map(int, input().split())
A_dic = dict() #A명단의 딕셔너리
arr = list() #중복되는 이름을 저장할 리스트

# A명단
for i in range(N):
	name = input()
	A_dic[name] = name

# B명단 입력받으면서 중복되는 값 찾기
# B명단은 따로 저장하지 않고 중복되는 이름만 저장
for i in range(M):
	name = input()
	if name in A_dic:
		arr.append(name)

# 사전순으로 정렬
arr.sort()

# 출력
print(len(arr))
for name in arr:
	print(name)







