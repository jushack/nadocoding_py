# 1명은 치킨, 3명은 커피 쿠폰을 받게 된다.

# 조건1: 댓글은 20명이 작성했고 아이디는 1 ~ 20이라 가정
# 조건2: 내용과 상관없이 무작위 추첨하되 중복불가
# 조건3: random 모듈의 shuffle과 sample을 사용

# 예제:
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다  --

from random import *

users = range(1, 21)
users = list(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print(winners)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다  --")