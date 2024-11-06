
# 학생들의 점수 리스트
notes = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# 모든 점수의 합계를 계산하는 함수
def somme_notes(notes):
    return sum(notes)  # sum() 함수를 사용하여 리스트의 모든 요소를 더함

# 합계 출력
print somme_notes(notes)

# 점수의 평균을 계산하는 함수
def moyenne_notes(notes):
    return somme_notes(notes) / float(len(notes))  # 합계를 점수 개수로 나누어 평균 계산
