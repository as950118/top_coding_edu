'''
N개의 숫자에서 M개를 중복없이 뽑는 경우의 수 찾기
ex) 1 2 3 != 2 1 3
'''
'''
N개의 숫자를 하나씩 골라서
그 숫자를 제외한 모든 숫자와의 경우의 수를 찾는다
'''
'''
대소관계를 이용하는 방식
1234
4321
'''
n, m = map(int, input().split()) # map(맵핑할 함수, 맵핑할 대상)
def update(the_list, n, result):
	templist = the_list[n:]
	templist.sort()
	the_list = the_list[:n]+templist
	result.append(the_list.copy())
	return the_list

def permutation(num):
	source = [x for x in range(1, int(num) + 1)]
	resource = [x for x in range(int(num), 0, -1)]
	result = [source.copy()]
	while source != resource:
		for i in range(len(source)-1, 0, -1):
			if source[i] > source[i-1]:
				for j in range(i, len(source)):
					if source[i-1] > source[j]:
						temp = source[i-1]
						source[i-1] = source[j-1]
						source[j-1] = temp
						source = update(source, i, result)
						break
					elif j == len(source) - 1:
						temp = source[i-1]
						source[i-1] = source[j]
						source[j] = temp
						source = update(source, i, result)
						break
				break
	return result
ret = permutation(n)
for elem in ret:
	print(elem)





