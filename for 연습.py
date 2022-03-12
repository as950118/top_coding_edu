# iterable = 순서대로 셀수있는것
# range(시작,끝)
# range(끝)
# python에서 어떤 범위표현식은 끝을 포함하지않음
for n in range(2, 10):
    print(f"{n}단 시작")
    for m in range(2, 10):
        print(f"{n}x{m}={n*m}")
    print(f"{n}단 끝")
