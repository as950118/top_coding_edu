'''
문제정의
어떤 x가 주어졌을때
해당 수를 뒤집은 수를 reverse x 할때
주어진 x, y에 대해
reverse x + reverse y 를 구해라 
'''
'''
문제해결방법
reverse 하는 방법을 구하기
indexing 활용

iter_object[start:end:step]
기본값 => start=0 / end=iter_object길이 / step=1
즉,
iter_object[::-1]
iter_object[0:len(iter_object):-1]
'''
def reverse(number:str):
	return int(number[::-1])

x, y = map(str, input().split())
x_y = reverse(x) + reverse(y)
str_x_y = str(x_y)
print(reverse(str_x_y))







