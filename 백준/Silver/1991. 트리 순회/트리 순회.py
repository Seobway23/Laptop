class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


n = int(input())
idx = 0
tree = {}

for _ in range(n):
    parent, left, right = input().split()

    # 부모 노드 없으면 샏성
    if parent not in tree:
        tree[parent] = Node(parent)

    # 왼쪽 자식 노드 처리
    if left != ".":
        tree[left] = Node(left)
        tree[parent].left = tree[left]  # 부모 -> 자식 연결

    # 오른쪽 자식 처리
    if right != '.':
        tree[right] = Node(right)
        tree[parent].right = tree[right]    # 부모 자식 연결


# 루트는 항상 A로 명시됨
root = tree['A']


def preorder(node):
    if node:
        print(node.value, end='')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end='')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end='')


# 결과 축력
preorder(root)
print()
inorder(root)
print()
postorder(root)