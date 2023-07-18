import random
import matplotlib.pyplot as plt

N = 100000
a = 50
b = 150


def rand_number():
    U = random.uniform(0, 1)
    if U <= 0.1:
        return 1
    if 0.1 < U <= 0.5:
        return 2
    if 0.5 < U <= 0.7:
        return 3
    if 0.7 < U <= 1.0:
        return 4


def draw_number_discrete():
    distribution = []
    for _ in range(N):
        distribution.append(rand_number())
    print(distribution)
    plt.hist(distribution)
    plt.show()


def reverse_distribution():
    return random.uniform(0, 100) + 50


def draw_number_real():
    distribution = []
    test_distr = [0 for _ in range(10)]
    x = [50 + i * 10 for i in range(10)]
    for _ in range(N):
        u = reverse_distribution()
        distribution.append(u)
        test_distr[int(u % 10)] += 1
    for i in range(10):
        print(x[i], ": ", test_distr[i])
    plt.hist(distribution, bins=10)
    plt.show()


def main():
    draw_number_discrete()
    draw_number_real()


if __name__ == '__main__':
    main()
