'''
문제정의
L이상 U이하의 모든 정수의 각 자리수의 합
'''
'''
문제해결방법
1. 전부다해보기
2. 공식을 찾아서 풀기
'''
'''
각자리 수의 합 구하기
1. 나머지 10*n 의 몫을 구하고
2. 남은 나머지를 다시 10*(n-1) 로 나누어서 1번 반복
'''
L, U = map(int, input().split())

def func(n):
	answer = [0 for i in range(10)]
	l = 1
	r = n
	base = 1
	while l<=r:
		while r%10 != 9:
			temp = r
			while temp:
				answer[temp%10] += base
				temp = temp//10
			r = r-1
		if r<1:
			break
		while l%10 != 0:
			temp = l
			while temp:
				answer[temp%10] += base
				temp = temp//10
			l = l+1
		r = r//10
		l = l//10
		for i in range(10):
			answer[i] += (r-l+1) * base
		base *= 10
	ret = 0
	for i in range(10):
		ret += answer[i]*i
	return ret
print(func(U) - func(L-1))
'''
i = 10의 승
45 * (10**i) * 3 - 45 * (10**(i-1)) *2
'''
'''
L = 10 / U = 19 ==> 10*1
1 + 1 + 1 .. = 1*10
0 + 1 + 2 .. = 45
45 + 앞자리수*10 (L = 20 / U = 29 = 45 + 2 * 10 = 65)

L = 100 / U = 199 ==> 10*2
1 + 1 + 1 .. = 1 * 100
0*10 + 1*10 .. = 450
0 + 1 + 2 + .. = 450

L = 1000 / U = 1999 ==? 10*3
1 + 1 + 1 .. = 1 * 1000
0*100 + 1*100 .. = 4500
(0*10 + 1*10..) * 10 = 4500
(0 + 1 + 2..) * 100 = 4500

L = 100 / U = 999
1* 100 + 2* 100 ... = (1+2+3..)*100 = 45 * 100
450 * 9
450 * 9
4500 + 4500 + 4500 - 900
'''
