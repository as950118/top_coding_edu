'''
유진수
어떤 자연수를 앞뒤로 나눠서 
앞뒤의 각각의 자리수를 곱했을때 같을 경우
'''
'''
문제정의
어떤 수가 주어졌을때
이수가 유진수인지 판단
'''
'''
문제해결방법
각 자리수별로 나눠서 계산해보기
'''
def func(number:str):
	ret = 1 # result:결과값
	for i in number:
		ret *= int(i)
	return ret

def main():
	N = str(input())
	length = len(N)

	for i in range(1,length):
		former = N[:i] # 문자열이므로 인덱싱가능
		latter = N[i:]
		if func(former) == func(latter):
			return "YES"
	return "NO"

print(main())
