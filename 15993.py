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
짝수개수는 
n-1번쨰의 홀수개수+
n-2번쨰의 홀수개수+
n-3번쨰의 홀수개수이고
홀수개수는 
n-1번쨰의 짝수개수+
n-2번쨰의 짝수개수+
n-3번쨰의 작수개수이다
'''
size = 100001
div=1000000009
# 0=홀, 1=짝
arr=[[0,0] for i in range(size)]
arr[1][0] = 1 
arr[1][1] = 0 
arr[2][0] = 1
arr[2][1] = 1 
arr[3][0] = 2 
arr[3][1] = 2
for i in range(4, size):
	arr[i][0]=arr[i-1][1]+arr[i-2][1]+arr[i-3][1]
	arr[i][1]=arr[i-1][0]+arr[i-2][0]+arr[i-3][0]
	arr[i][0]%=div
	arr[i][1]%=div

t = int(input())
for i in range(t):
	n = int(input())
	print(arr[n][0], arr[n][1])
