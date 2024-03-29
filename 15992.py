'''
문제정의
어떤수 n을만들떄
순서를 고려하여서
m개의 숫자를 활용하여
만들 수 있는 경우의 수 구하기
'''
'''
문제해결방법
어떤수 n에 대하여
1,2,3을 활용하여 만드는 방법의 수는
n-1번째에 1을 더해주는 경우
n-2번째에 2을 더해주는 경우
n-3번째에 3을 더해주는 경우
들의 수와 같다
단, 나타내는 방법의 수는 +1 된다
'''
'''
1,1 => 1
2,1 => 2
2,2    1+1
3,1 => 3
3,2 => 2+1, 1+2
3,3 => 1+1+1
4,1 => X
4,2 => 2+2
4,3 => 2+1+1, 1+2+1, 1+1+2
4,4 => 1*4
5,1 => X
5,2 => X
5,3 => 2+1+1, 1+2+1, 1+1+2
5,4 => 1*4
5,5 => 1*5
'''
size = 1001
arr=[[0 for j in range(size)] for i in range(size)]
arr[1][1] = 1
arr[2][1] = 1
arr[2][2] = 1
arr[3][1] = 1
arr[3][2] = 2
arr[3][3] = 1
div=1000000009
for i in range(4, size):
	for j in range(1,i+1):
		arr[i][j]=(arr[i-1][j-1]+
			arr[i-2][j-1]+arr[i-3][j-1])%div

t = int(input())
for i in range(t):
	n,m = map(int, input().split())
	print(arr[n][m])

