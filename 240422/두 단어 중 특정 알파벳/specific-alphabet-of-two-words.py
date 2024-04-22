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
    co = []
    for s in ss:
        co_2 = []
        for i in range(len(s)):
            if s[i] not in co:
                dic[s[i]] +=1
                co_2.append(s[i])
            elif s[i] in co:
                pass
        co.extend(co_2)


for x in list(dic.values()):
    print(x)