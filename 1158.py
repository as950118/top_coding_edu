N, K = map(int, input().split())
arr = [i for i in range(1,N+1)]
ret = []
cur = K - 1
while len(arr):
	if cur >= len(arr):
		cur = cur % len(arr)
	else:
		ret.append(str(arr.pop(cur)))
		cur += K-1
print(f"<{', '.join(ret)}>")
