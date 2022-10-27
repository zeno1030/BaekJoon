import sys

n = int(sys.stdin.readline().strip())
tree = {}

for i in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root]=[left,right]

def preorder(root):
    if root != '.':
        print(root,end ='')
        preorder(tree[root][0])
        preorder(tree[root][1])
def inorder(root):
    if root != '.' :
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')
    
