import matplotlib.pyplot as plt

M = pow(2, 31) - 1
N = 100000
c = 1
a = 69069
start = 15


def linearFormula(xn):
    return (a * xn + c) % M


def linearGenerator():
    result = [linearFormula(start)]
    for i in range(1, N):
        result.append(linearFormula(result[i - 1]))
    intervals = [0 for _ in range(10)]
    for res in result:
        index = int(10 * res / M)
        intervals[index] = intervals[index] + 1
    for inter in intervals:
        print(inter)
    plt.hist(result, density=False, bins=10)
    plt.title("Linear generator distribution")
    plt.show()


def drawFloat(register):
    result = int()
    for j in range(len(register) - 1, 0, -1):
        result = result + int(register[j]) * pow(2, j)
    return result


def registerGenerator():
    register = '1101011'
    p = 7
    q = 3
    result = []
    for j in range(N):
        for i in range(len(register), len(register) + 24):
            if register[i - q] == '0':
                iq = False
            else:
                iq = True
            if register[i - p] == '0':
                ip = False
            else:
                ip = True
            register = register + str(int(iq != ip))
        result.append(drawFloat(register))
        newReg = ""
        for i in range(7):
            newReg = newReg + register[len(register) - 8 + i]
        register = newReg
    intervals = [0 for _ in range(10)]
    for res in result:
        index = int(10 * res / M)
        intervals[index] = intervals[index] + 1
    for inter in intervals:
        print(inter)
    plt.hist(result, density=False, bins=10)
    plt.title("Register generator distribution")
    plt.show()


def main():
    print("Linear generation")
    linearGenerator()
    print("Register generation")
    registerGenerator()


if __name__ == '__main__':
    main()
