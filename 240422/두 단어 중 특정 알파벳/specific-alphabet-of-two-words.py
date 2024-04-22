dic = {'a': 0,
       'b': 0,
       'c': 0,
       'd': 0,
       'e': 0,
       'f': 0,
       'g': 0,
       'h': 0,
       'i': 0,
       'j': 0,
       'k': 0,
       'l': 0,
       'm': 0,
       'n': 0,
       'o': 0,
       'p': 0,
       'q': 0,
       'r': 0,
       's': 0,
       't': 0,
       'u': 0,
       'v': 0,
       'w': 0,
       'x': 0,
       'y': 0,
       'z': 0,}


N = int(input())
for i in range(N):
    ss = list(input().split(" "))
    
    dic1 = {}
    dic2 = {}
    
    for i in range(len(ss[0])):
        if ss[0][i] not in dic1:
            dic1[ss[0][i]] = 1
        else:
            dic1[ss[0][i]] +=1
    
    for j in range(len(ss[1])):
        if ss[1][j] not in dic2:
            dic2[ss[1][j]] = 1
        else:
            dic2[ss[1][j]] +=1
    
    # 합치는 과정
    for f in dic2:
        if f not in dic1: # 없을 경우에는
            dic1[f] = dic2[f]
        
        elif f in dic1:
            if dic2[f] > dic1[f]:
                dic1[f] = dic2[f]
    
    # 개수 추가하기
    for f_2 in dic1:
        dic[f_2] += dic1[f_2]

for x in list(dic.values()):
    print(x)