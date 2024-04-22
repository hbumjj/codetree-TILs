N = int(input())

arr = []

for i in range(N):
    order = list(input().split(" "))
    
    if order[0] == "push_back":
        arr.append(int(order[1]))
    
    elif order[0] == "pop_back":
        arr.pop()
        
    elif order[0] == "size":
        print(len(arr))
        
    elif order[0] == "get":
        print(arr[int(order[1])-1])