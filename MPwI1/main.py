from anytree import Node


"""comb = []
perms = []


def printTraverseTree(root, perm):
    if root.name != "root":
        perm.append(root.name)
    if not root.children:
        print(perm)
        return
    for node in root.children:
        printTraverseTree(node, perm)
        perm.pop(-1)


def generateTraverseTreeCombination(root, perm):
    if root.name != "root":
        perm.append(root.name)
    if not root.children:
        comb.append(list(perm))
        return
    for node in root.children:
        generateTraverseTreeCombination(node, perm)
        perm.pop(-1)


def combinations(set, limit):
    root = Node("root")
    set.sort()
    for nodeNumber in set:
        node = Node(nodeNumber, parent=root)
        set.remove(nodeNumber)
        createTreeVarNoRep(node, set, 1, limit)
        set.append(nodeNumber)
        set.sort()
    generateTraverseTreeCombination(root, [])
    for node in comb:
        node.sort()
    comb.sort()
    last = None
    for i in range(len(comb)):
        if last != comb[i]:
            print(comb[i])
        last = comb[i]


def combinationsRepetitions(set, limit):
    root = Node("root")
    for nodeNumber in set:
        node = Node(nodeNumber, parent=root)
        createTreeVarRep(node, set, 1, limit)
    generateTraverseTreeCombination(root, [])
    for node in comb:
        node.sort()
    comb.sort()
    last = None
    for i in range(len(comb)):
        if last != comb[i]:
            print(comb[i])
        last = comb[i]


def createTreeVarRep(root, set, depth, limit):
    if depth == limit:
        return
    for nodeNumber in set:
        node = Node(nodeNumber, parent=root)
        depth = depth + 1
        createTreeVarRep(node, set, depth, limit)
        depth = depth - 1


def mVarationsOfNSetRepetitions(set, limit):
    root = Node("root")
    for nodeNumber in set:
        node = Node(nodeNumber, parent=root)
        createTreeVarRep(node, set, 1, limit)
    printTraverseTree(root, [])


def createTreeVarNoRep(root, set, depth, limit):
    if depth == limit:
        return
    for nodeNumber in set:
        node = Node(nodeNumber, parent=root)
        set.remove(nodeNumber)
        depth = depth + 1
        createTreeVarNoRep(node, set, depth, limit)
        depth = depth - 1
        set.append(nodeNumber)
        set.sort()


def mVarationsOfNSet(set, limit):
    root = Node("root")
    set.sort()
    for nodeNumber in set:
        node = Node(nodeNumber, parent=root)
        set.remove(nodeNumber)
        createTreeVarNoRep(node, set, 1, limit)
        set.append(nodeNumber)
        set.sort()
    printTraverseTree(root, [])


def getTraverseTree(root, perm):
    if root.name != "root":
        perm.append(root.name)
    if not root.children:
        perms.append(list(perm))
        return
    for node in root.children:
        getTraverseTree(node, perm)
        perm.pop(-1)


def createTreePerms(root, set):
    if not set:
        return
    for nodeNumber in set:
        node = Node(nodeNumber, parent=root)
        set.remove(nodeNumber)
        createTreePerms(node, set)
        set.append(nodeNumber)
        set.sort()


def permutations(set):
    root = Node("root")
    set.sort()
    for nodeNumber in set:
        node = Node(nodeNumber, parent=root)
        set.remove(nodeNumber)
        createTreePerms(node, set)
        set.append(nodeNumber)
        set.sort()
    getTraverseTree(root, [])
    permsRep = {tuple(x) for x in perms}
    for p in permsRep:
        print(p)"""


counter = 0


def variations(numbers, m, depth, result):
    if depth == m:
        print(result)
        global counter
        counter = counter + 1
        result.pop(-1)
        return
    for i in numbers:
        result.append(i)
        variations(numbers, m, depth + 1, result)
    if result:
        result.pop(-1)


def main():
    #permutations([1, 2, 3])
    #mVarationsOfNSet([1, 2, 3], 2)
    #mVarationsOfNSetRepetitions([1, 2, 3, 4, 5], 2)
    #combinations([1, 2, 3], 2)
    #combinationsRepetitions([1, 2, 3], 2)
    n = int(input("Input n: "))
    m = int(input("Input m: "))
    numbers = [i for i in range(1, n + 1)]
    variations(numbers, m, 0, [])
    print(counter)


if __name__ == '__main__':
    main()
