'''
    학생 관리 시스템
    "학생 관리" 프로그램을 작성하시오.
    이 프로그램은 종료 시킬 때까지 무한 반복된다.
    -"작업 선택: "에서 0 입력 시 프로그램이 종료된다.
    -"작업 선택: "에서 1 입력 시 관리하는 학생 목록이 조회된다.
    -"작업 선택: "에서 2 입력 시 학생을 추가할 수 있다.
    -"작업 선택: "에서 3 입력 시 학생을 삭제할 수 있다.
    이때 입력한 학생은 관리하는 학생 목록에 있는 데이터만 삭제 가능하도록 하며
    목록에 없는 학생을 삭제하고자 할 때는
    '삭제할 학생이 없습니다. 다시 입력하세요!'를 화면에 출력한다

    알고리즘
    1. 무한반복 시작
    2. 작업 선택을 입력받는다.
        1) 0 입력시 프로그램 종료
        2) 1 입력시
            a. 리스트에 존재하는 학생 정보 출력
        3) 2 입력시
            a. 학생의 정보를 입력받으면
            b. 해당 학생의 정보 삭제
        4) 3 입력시
            a. 학생의 정보를 입력받으면
            b. 해당 학생의 정보 삭제
'''

students = ["현탁", "진환", "나현", "유진", "형종"]

while True:

    print("------학생 관리-------")
    print("     0. 종료")
    print("     1. 학생 조회")
    print("     2. 학생 추가")
    print("     3. 학생 삭제")
    print("----------------------")
    
    project = int(input())
    print()

    if project == 0:
        break

    elif project == 1:
            print(students)
            print()

    elif project == 2:
        student_add = input("추가할 학생의 이름 입력: ")
        print()
        students.append(student_add)
        print("추가되었습니다.")
        print()

    elif project == 3:
        student_remove = input("삭제할 학생의 이름 입력: ")
        print()
        if student_remove in students:
            students.remove(student_remove)
            print("삭제되었습니다.")
            print()
        else:
            print("삭제할 학생이 없습니다. 다시 입력하세요!")
            print()



