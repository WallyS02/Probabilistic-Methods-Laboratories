import random


def drawX1():
    U = random.uniform(0, 1)
    if U <= 0.1:
        return 1
    elif 0.4 >= U > 0.1:
        return 2
    elif 0.75 >= U > 0.4:
        return 3
    else:
        return 4


def drawX2(x1):
    match x1:
        case 1:
            return 2
        case 2:
            U = random.uniform(0, 1)
            if U <= 0.333:
                return 1
            else:
                return 3
        case 3:
            U = random.uniform(0, 1)
            if U <= 0.574:
                return 2
            else:
                return 4
        case 4:
            U = random.uniform(0, 1)
            if U <= 0.6:
                return 3
            else:
                return 4


def main():
    distribution = [0, 0, 0, 0, 0, 0, 0]
    legend = [[1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 4]]
    for _ in range(10000):
        x1 = drawX1()
        x2 = drawX2(x1)
        if x1 == 1 and x2 == 2:
            distribution[0] += 1
        elif x1 == 2 and x2 == 1:
            distribution[1] += 1
        elif x1 == 2 and x2 == 3:
            distribution[2] += 1
        elif x1 == 3 and x2 == 2:
            distribution[3] += 1
        elif x1 == 3 and x2 == 4:
            distribution[4] += 1
        elif x1 == 4 and x2 == 3:
            distribution[5] += 1
        elif x1 == 4 and x2 == 4:
            distribution[6] += 1
    print(legend)
    print(distribution)


if __name__ == '__main__':
    main()
