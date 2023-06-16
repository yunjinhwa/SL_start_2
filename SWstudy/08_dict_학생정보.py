'''
    학과 학번 이름:
    
    학생 정보를 사전에 저장하고, (학번, 이름)
    특정 학생의 정보(학번)를 입력하여 학생을 찾아주세요:

    알고리즘
    1.학생 정보 저장 사전 만들기 - 빈 사전 만들기
    2. 학생 정보 입력 - 사전에 저장 (z키를 누르면 종료 - 무한반복)
    3. 학번으로 검색하여 학생 찾기 (학번이 빈칸이면 검색 종료 - 무한반복)
'''

student=dict()

print("----학생 정보 입력----")
while True:
    num = input("학번: ")
    if num == "z":
        break
    name = input("이름: ")
    student[num] = name
print("입력종료")
print("학생 검색")

while True:
    find_num = input("찾으시는 학생의 학번을 입력하세요")
    if find_num == "":
        print("프로그램을 종료합니다.")
        break
    elif find_num in student:
        print(student[find_num])
    else:
        print("찾으시는 학생의 정보가 없습니다.")





