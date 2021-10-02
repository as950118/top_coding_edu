'''
완전제곱수
n**2 에 해당하는 숫자들
'''
'''
문제정의
m,n 사이의 완전제곱수를 구해서
합을 구하고
최소값을 구함
'''
'''
문제해결방법
1. 완전제곱수들을 다 구해놓고 해당하는 값들을 추출사용
2. root를 활용
'''
import math
m = int(input())
n = int(input())
root_m = math.ceil(m**(1/2)) #올림
root_n = int(n**(1/2)) #내림

ret = 0
for i in range(root_m, root_n+1):
	ret += i**2
if ret == 0:
	print(-1)
else:
	print(ret)
	print(root_m**2)








