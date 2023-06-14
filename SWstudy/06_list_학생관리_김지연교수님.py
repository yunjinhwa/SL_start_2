student = []

print("------학생 관리-------")
print("     0. 종료")
print("     1. 학생 조회")
print("     2. 학생 추가")
print("     3. 학생 삭제")
print("----------------------")

while True:
    menu = int(input("작업 선택: "))
    if menu == 1:
        print("1. 학생 조회: ",student)
    elif menu == 2:
        student.append(input("2. 학생 추가: "))
    elif menu == 3:
        del_student = input("삭제할 학생 입력: ")
        if student.count(del_student) == 0:
            print("삭제할 학생이 없습니다.")
            continue
        else:
            student.remove(del_student)
    elif menu == 0:
        print("프로그램을 종료합니다.")
        break