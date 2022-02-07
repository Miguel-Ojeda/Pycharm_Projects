import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [i for i in range(10)]
    y = [i**2 for i in range(10)]

    plt.plot(x, y)
    plt.show()