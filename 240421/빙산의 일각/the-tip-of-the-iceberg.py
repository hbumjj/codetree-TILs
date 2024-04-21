N = int(input())

arr = []
max_ = 0
min_ = 1000000001

for i in range(N):
    f = int(input())
    arr.append(f)
    
    max_ = max(max_, f)
    min_ = min(min_, f)


# arr = [3,5,2,3,1,4,2,3]
# max_ = 5
# min_ = 1

answer = 0

for depth in range(min_, max_):
    group = 0
    flag = False
    for f in arr: # 깊이에 따른 그룹
        if f > depth:
            if flag == True:  # 이미 플래그가 들어왔을 때
                pass
            elif flag == False: # 처음으로 플래그에 들어올 때
                flag = True
        
        else:
            if flag == True: # 플래그에 있다가 나왔을 때
                group +=1
                flag = False
    if flag == True:
        group+=1
    
    answer = max(answer, group)

print(answer)