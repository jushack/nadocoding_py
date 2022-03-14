# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

# 조건1: 운행 소요 시간은 5분 ~ 50분 사이
# 조건2: 당신은 소요시간 15분 이하의 승객만 매칭한다.

# 예제:
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 10분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

from random import *

count = 0

for i in range(1, 51):
    time = randrange(5, 51)
    if 5<= time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}".format(count))