score_file = open("score.txt", "w", encoding="utf8")    # 쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")    # 이어쓰기
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100")
score_file.close()