'''
팩토리얼을 재귀형태로 구현하기
팩토리얼 = 1부터 n까지의 전체 곱
ex ) n=10 => 1*2*3*..10 = 36..
'''
import sys
from datetime import datetime
sys.setrecursionlimit(10**8)

def time_deco(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        ret = func(*args, **kwargs)
        end_time = datetime.now()
        duration = (end_time-start_time).total_seconds()
        print(f"함수 호출 시간 : {duration}")
        return ret
    return wrapper

@time_deco
def wrap_for(n):
    ret = 1
    for i in range(1, n+1):
        ret = ret * i
    return ret

@time_deco
def wrap_fac(n):
    def fac(n):
        if n == 1:
            return 1
        else:
            return n * fac(n-1)
    return fac(n)


memo_fac = [1]
@time_deco
def wrap_memo(n):
    if len(memo_fac) < n:
        for i in range(len(memo_fac), n+1):
            cur = memo_fac[-1] * i
            memo_fac.append(cur)
    return memo_fac[n-1]

# n 주어져야함
for i in range(10):
    n = int(input("n = "))
    ret = wrap_for(n)
    print(f"for문으로 해결 : {ret}")
    ret = wrap_fac(n)
    print(f"재귀함수로 해결 : {ret}")
    ret = wrap_memo(n)
    print(f"동적계획법으로 해결 : {ret}")

# 1번만 했을때는 for문이 가장 효과적일수도있다
# 하지만 여러번 반복을 하게되면 동적계획법이 가장 효율적이다
# 그 이유는 기록을 사용할수있기 때문
