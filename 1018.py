# 체스판에서 블랙으로 시작할 경우 몇개 전환이 필요한지
def check(temp_arr):
	is_black=False
	count = 0
	for row in temp_arr:
		# 줄 바뀔때마다 체인지
		if is_black:
			is_black =  False
		else:
			is_black =  True
		for elem in row:
			if is_black:
				if elem != 'B':
					count += 1
				is_black = False
			else:
				if elem != 'W':
					count += 1
				is_black = True
	return min(count, 64-count)
# 전체 크기에서 체스판 크기만큼 쪼개서 확인해보기
min_count = 10**8
for i in range(N-7):
	for j in range(M-7):
		temp_arr = []
		for k in range(i,i+8):
			temp_arr.append(arr[k][j:j+8])
		cur_count = check(temp_arr)
		min_count = min(min_count, cur_count)
print(min_count)
