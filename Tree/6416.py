import sys

case = 0
finish = -1
tree = []

while True:
    case += 1
    n = []
    count = 0
    p_node = []
    test = -1
       
    """while True:
        a, b = list(map(int, sys.stdin.readline().split())) # 부모,자식 노드 list형태로 입력
        n.append([a,b])
        if n[-1][0] == 0: break
        elif n[-1][0] == -1:
            finish = 0 # 종료 조건
            break"""     
            
    isInput = True
    while isInput:
        buf = sys.stdin.readline().rstrip().split("  ")
        if buf[0] == '':
            continue
        for temp in buf:
            a, b = list(map(int, temp.split(" "))) # 부모,자식 노드 list형태로 입력
            n.append([a,b])
            if n[-1][0] == 0:
                isInput = False
                break
            elif n[-1][0] == -1: 
                isInput = False
                finish = 0 # 종료 조건
                break
            
    

    if finish == 0: break
    if n[0][0] == 0:
        tree.append(f"Case {case} is a tree.") # 0 0도 트리임
        continue

    # 1. 들어오는 간선이 하나도 없는 단 하나의 노드가 존재.

    del n[-1]
    n.sort()
    p_node.append(n[0][0])
    for i in range(len(n)-1):
        if n[i][0] != n[i+1][0]:p_node.append(n[i+1][0])

    for i in range(len(n)): # p_node가 c_node가 되는 경우가 존재하면 count
        if n[i][1] in p_node: count += 1
    if len(p_node)-1 != count: tree.append(f"Case {case} is not a tree.")

    # 2. 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재.

    else: 
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if n[i][1] == n[j][1]:
                    tree.append(f"Case {case} is not a tree.")
                    test = 0 # case test 끝남
                    break
            if test == 0: break
            if i == len(n)-1: tree.append(f"Case {case} is a tree.")
    
    #print(f'{n}\n p_node : {p_node}\n count : {count}')

    
for i in range(len(tree)):
    print(tree[i])

