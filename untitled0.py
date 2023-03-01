import matplotlib.pyplot as plt
import numpy as np

x_axis= np.random.randint(10,50,5)
y_axis= np.random.randint(10,50,5)


class Dataplot:
    def line():
        plt.plot(x_axis,marker='*',linestyle="dashdot")
        plt.plot(y_axis,marker='o',linestyle="dotted")
        plt.grid(color="green")
        plt.show()
    def bar():
        plt.bar(x_axis,y_axis,width=1)
        plt.grid(color="green")
        plt.show()
    def pi():
        explode=np.array([0.1,0.2,0,0,0,])
        plt.pie(x_axis,labels=y_axis,shadow=True,explode=explode)
        plt.legend(title="Stuff")
        plt.show()
    def scat():
        colors=np.array([10,20,30,40,50])
        plt.scatter(x_axis,y_axis,c=colors,cmap='viridis')
        plt.colorbar()
        plt.show()

Dataplot.line()
Dataplot.bar()
Dataplot.pi()
Dataplot.scat()