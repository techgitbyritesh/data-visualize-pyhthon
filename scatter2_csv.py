import pandas as pd
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9]
y=[2,3,4,5,6,7,8,9,11]
plt.scatter(x,y,label='star',color='green',marker='*',s=30)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter_plot')
plt.legend()
plt.show()