import numpy as np
import matplotlib.pyplot as plt

blue = (31/255.0, 119/255.0, 180/255.0)
orange = (255/255.0, 127/255.0, 14/255.0)

def f(x):

    return x*x

def makeData(x, f, sig):

    y0 = f(x)

    yerr = sig * np.random.randn(*x.shape)

    return y0+yerr


if __name__ == "__main__":


    a = 0
    b = 10
    sig = 10.0
    
    x = np.linspace(a, b, 100)
    y = f(x)

    Xdat = np.linspace(a, b, 1000)
    Ydat = makeData(Xdat, f, sig)


    fig = plt.figure(figsize=(12,9))

    ax1 = fig.add_subplot(1,1,1)

    ax1.plot(x, y, ls='dashed', lw=4, color=blue, label="Model")
    ax1.plot(Xdat, Ydat, ls='None', marker='o', ms=10, color=orange, alpha=0.5, label="Data")

    ax1.set_xlabel(r"$X = \mathcal{F}^2$", fontsize=24)
    ax1.set_ylabel(r"$Y = \int \mathcal{F}_2$", fontsize=24)
    ax1.legend(loc="upper left", fontsize=24)

    ax1.tick_params(labelsize=18)

    fig.tight_layout()

    fig.savefig("plot.png")
    fig.savefig("plotBIG.png", dpi=300)
    fig.savefig("plot.pdf")


    plt.show()
