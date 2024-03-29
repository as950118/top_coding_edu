'''
문제정의
정사각형 모양의 별을 규칙대로 찍기
1. N은 3의 거듭제곱(3,9,27,81...)
2. N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태
'''
'''
해결방법
적절한 알고리즘을 활용
분할정복
'''

'''
# n=3
***
* * ==> $
***
# n=9
*********
* ** ** *
*********
***   ***     $$$
* *   * * ==> $ $ ==> @
***   ***     $$$
*********
* ** ** *
*********
# n=27
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
*********         *********
* ** ** *         * ** ** *
*********         *********
***   ***         ***   ***     @@@
* *   * *         * *   * * ==> @ @
***   ***         ***   ***     @@@
*********         *********
* ** ** *         * ** ** *
*********         *********
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
'''

n = int(input())

# 승수 구하기
k = 1
while True:
	if 3**k == n:
		break
	k+=1

# 초기패턴 선언
pattern = ["*"]

# n과 k에 맞게 반복
for i in range(k):
	new_pattern = []
	for row in pattern:
		new_pattern.append(row*3)
	for row in pattern:
		new_pattern.append(row + " "*int(3**(i)) + row)
	for row in pattern:
		new_pattern.append(row*3)
	pattern = new_pattern

# 출력
for row in pattern:
	print(row)
