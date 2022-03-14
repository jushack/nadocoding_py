# 표준 체중 구하기

# 남자: 키 * 키 * 22
# 여자: 키 * 키 * 21

# 조건1: 함수명: std_weight
#        전달값: 키(height), 성별(gender)
# 조건2: 소수점 둘째자리까지 표시

# 예시:
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender): # m단위
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21
    
height = 175                   # cm단위
gender = '남자'
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))