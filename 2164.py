'''
문제정의
1부터 n까지의 카드를
특정 규칙에 따라 반복한 후
마지막에 남는 카드 번호를 출력하는 프로그램
'''
'''
문제해결방법
1. 주어진 규칙 반복
2. 적절한 알고리즘으로 규칙 최적화
'''
'''
적절한 알고리즘
현재 카드덱에서 홀수번쨰 위치에 있는 숫자를 제거
'''
n = int(input())
deck = [i for i in range(1, n+1)]

while len(deck) != 1:
	if len(deck)%2 == 0: # 짝수
		deck = [deck[i] for i in range(1, len(deck), 2)]
	else:
		poped = deck[1]
		deck = [deck[i] for i in range(3, len(deck), 2)]
		deck.append(poped)
print(deck[0])
