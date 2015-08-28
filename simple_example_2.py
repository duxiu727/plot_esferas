# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt
import plt_esfera

if __name__ == '__main__':
  fig= plt.figure()
  ax= fig.add_subplot(111, aspect='auto')

  x= np.linspace(0.1,10,41)
  y= 1.5*(1+ np.sin(x)/(.01+x))
  y1= y[::2]

  for c in plt_esfera.colores.values():
    y1 = y1 + .1
    ax.plot_esfera( x[::2],y1, color=c, markersize=8, label=c)

  # Plot a simple "standard" line
  plt.plot(x,2+(.5+x)*y/(1+x)**2,'-k',lw=3, label='Line 1')
  # 
  plt.legend(loc='best', numpoints=1)
  plt.savefig('simple_example_2.png')
  plt.show()

