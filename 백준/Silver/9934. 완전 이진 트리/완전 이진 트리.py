
from collections import deque


def build_tree(numlist):
    if not numlist:
        return []
    
    mid = len(numlist) //2
    root = numlist[mid]

    left_subtree = build_tree(numlist[:mid])
    right_subtree = build_tree(numlist[mid+1:])

    return [root,left_subtree,right_subtree]

def print_tree(tree):
    # 비어있는 트리인 경우
    if not tree:
        return
    
    # 너비 우선 탐색(BFS)을 위한 큐
    queue = deque([tree])
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            root = node[0]  # 현재 노드의 루트 값
            level_nodes.append(root)
            
            # 왼쪽 서브트리와 오른쪽 서브트리가 있다면 큐에 추가
            if node[1]:
                queue.append(node[1])
            if node[2]:
                queue.append(node[2])
        
        # 현재 레벨의 노드들 출력
        print(" ".join(map(str, level_nodes)))

N = int(input())
numlist = list(map(int,input().split()))

tree = build_tree(numlist)

print_tree(tree)
    