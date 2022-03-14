import sys
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr)

# 시험성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subjects, score in scores.items():
    print(subjects.ljust(3), str(score).rjust(3), sep=" : ")


# 은행대기순번
# 001 002 003 ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
