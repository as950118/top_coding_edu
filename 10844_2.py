import sys
sys.setrecursionlimit(1000000000)

dp = [0]*1000000 #Memorizaton 그전값들을 기록해서 푸는방식
ret = 0
mod = 1000000000

def func(n, i, k):#횟수 위치 (계단수) 현재값
    global ret
    # 만약 수의 끝에 도달했을때
    if n<=i:
        ret = ret+1
        # 정답을 10억으로 나눈 결과를 원하기에
        if ret==mod:
            ret = 0
        return # 함수 종료를 위한 return
    if k<1 or k>8:
        if k==0:
            func(n, i+1, k+1)
        elif k==9:
            func(n, i+1, k-1)
        else: #10이 넘어가거나 , -값이 되었을떄
            return # 함수 종료를 위한 return
    else: # 1<=K<=8
        func(n, i+1, k+1)
        func(n, i+1, k-1)

N = int(input())
for k in range(1, 10):
    func(N, 1, k)
print(ret)
