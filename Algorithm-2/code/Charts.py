import matplotlib.legend
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')


def create_chart(xaxis, yaxis, lable1=" ", xname=" ", yname=" ", title=" "):
    plt.plot(xaxis, yaxis, label=lable1)
    plt.ylabel(yname)
    plt.xlabel(xname)
    plt.suptitle(title)


def add_line(y, xaxis, lable1):
    plt.plot([xaxis[0], xaxis[len(xaxis) - 1]], [y, y], label = lable1)


def show_chart():
    plt.legend()
    plt.show()


def create_all_chart(xaxis, yaxis1, yaxis2 ,yaxis3, lable1=" ", lable2=" ", lable3=" ", xname=" ", yname=" ", title=" "):
    plt.plot(xaxis, yaxis1, label=lable1)
    plt.plot(xaxis, yaxis2, label=lable2)
    plt.plot(xaxis, yaxis3, label=lable3)
    plt.ylabel(yname)
    plt.xlabel(xname)
    plt.suptitle(title)
    plt.legend(loc="upper left")
    plt.show()

def create_all_chart_tabu(xaxis, yaxis1, yaxis2, yaxis3, yaxis4, lable1=" ", lable2=" ",  lable3=" ",lable4=" ", xname=" ", yname=" ",
                         title=" "):
    plt.plot(xaxis, yaxis1, label=lable1)
    plt.plot(xaxis, yaxis2, label=lable2)
    plt.plot(xaxis, yaxis3, label=lable3)
    plt.plot(xaxis, yaxis4, label=lable4)
    plt.ylabel(yname)
    plt.xlabel(xname)
    plt.suptitle(title)
    plt.legend(loc="upper left")
    plt.show()


def clear_chart():
    plt.clf()