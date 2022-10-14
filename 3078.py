from sys import stdin

n, k = map(int,input().split())
students = [0] * n
data = [0] * 21
count = 0

for rank in range(n):
    name = len(stdin.readline().rstrip()) #학생들 이름 입력
    #print(name)
    students[rank] = name # 학생 등수와 이름의 길이 저장
    print(students)
    if rank > k: # 학생의 등수가 K 보다 커지는 경우
        data[students[rank - k - 1]] -= 1 #자신과 상관 없는 등수의 학생을 제거
        #print(data)
    count += data[name]     # 자신과 이름의 길이가 같은 친구를 쌍으로 추가
    #print(count)
    data[name] += 1 # 이름의 길이를 저장하는 리스트에 자신을 추가

print(count)