my_name = str(input())
number = int(input())
my_L = my_name.count("L")
my_O = my_name.count("O")
my_V = my_name.count("V")
my_E = my_name.count("E")

max_ret = -1
max_lover = None
for i in range(number):
	lover = str(input())
	lover_L = lover.count("L")
	lover_O = lover.count("O")
	lover_V = lover.count("V")
	lover_E = lover.count("E")
	L = my_L + lover_L
	O = my_O + lover_O
	V = my_V + lover_V
	E = my_E + lover_E
	ret = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
	if ret > max_ret:
		max_lover = lover
		max_ret = ret
	# 확률이 같을떄에는 알파벳순으로
	if ret == max_ret:
		if lover < max_lover:
			max_lover = lover
			max_ret = ret
print(max_lover)
