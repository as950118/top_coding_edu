'''
문제정의
적정체중의 *2와 *(1/2)범위일때는 행복
초과혹은 미만시 슬픔
0이하시 사망
'''
'''
문제해결방법
시나리오를 잘 짜준다
'''

class Pet:
	def __init__(self, target_weight, weight):
		self.weight = weight
		self.target_weight = target_weight

	def exercise(self, minutes):
		self.weight -= minutes

	def feed(self, n):
		self.weight += n

	def status(self):
		# 죽음
		if self.weight <= 0:
			return -1
		# 행복
		elif self.target_weight*2 > self.weight > self.target_weight*0.5:
			return 1
		# 슬픔
		else:
			return 0

i = 0
while True:
	i += 1
	o, w = map(int, input().split())
	if o == 0 and w == 0: #종료
		break
	pet = Pet(o, w)
	while True:
		n, m = input().split()
		m = int(m)
		if n == '#' and m == 0: # 시나리오 종료
			break

		# 죽었을 경우
		status = pet.status()
		if status == -1:
			continue

		# 운동시키기
		if n =='E':
			pet.exercise(m)
		# 밥먹이기
		else:
			pet.feed(m)

	# 상태 확인
	status = pet.status()
	if status == -1:
		print(i, "RIP")
	elif status == 1:
		print(i, ":-)")
	else:
		print(i, ":-(")



