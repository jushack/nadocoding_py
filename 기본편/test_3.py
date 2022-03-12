# test_3

# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예: http://naver.com

# 규칙1: http:// 부분은 제외 -> naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                 nav                 5               1           !
# 생성된 비밀번호: nav51!

#url = "http://naver.com"
url = "http://google.com"

ps = url.replace("http://", "")                         # 규칙1
ps = ps[:ps.index(".")]                                 # 규칙2
ps = ps[:3] + str(len(ps)) + str(ps.count("e")) + "!"   # 규칙3

print("{0}의 비밀번호는 {1} 입니다".format(url, ps))
