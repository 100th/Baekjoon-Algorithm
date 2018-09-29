def my_tree(r):
    return [r, [], []]

root = None

# 값을 추가
def add(data, left, right):
    global root
    if root is None:
        if data != '.':
            root = my_tree(data)
        if left != '.':
            root[1] = my_tree(left)
        if right != '.':
            root[2] = my_tree(right)
        return root
    else:
        return search(root, data, left, right)

# 어느 위치에 추가할 것인지 위치를 찾아줌
def search(root, data, left, right):
    if root is None or root == []:
        return root

    elif root[0] == data:
        if left != '.':
            root[1] = my_tree(left)
        if right != '.':
            root[2] = my_tree(right)
        return root

    else:
        search(root[1], data, left, right)
        search(root[2], data, left, right)


for i in list_[1:]:
    add(i[0], i[1], i[2])


def preorder(root):
    if root:
        print(root[0], end='')
        if root[1]:
            preorder(root[1])
        if root[2]:
            preorder(root[2])

def inorder(root):
    if root:
        if root[1]:
            inorder(root[1])
        print(root[0], end='')
        if root[2]:
            inorder(root[2])

def postorder(root):
    if root:
        if root[1]:
            postorder(root[1])
        if root[2]:
            postorder(root[2])
        print(root[0], end='')


preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
