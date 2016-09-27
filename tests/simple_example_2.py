# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt
import plt_esfera

if __name__ == '__main__':
  plt.style.use('dark_background')
  fig= plt.figure(figsize=(12,9))
  ax= fig.add_subplot(111, aspect='auto',)

  x= np.linspace(0.1,10,31)
  y= 1.5*(1+ np.sin(x)/(.01+x))
  y1= y
  for c in plt_esfera.colores.keys():
    if len(c) > 1:
      y1 -= .2
      ax.plot_esfera( x,y1, color=c, markersize=14, label=c)
      
  # Add a "standard" line
  ax.plot(x,2+(.5+x)*y/(1+x)**2,'-',lw=3, label='Line 1')
  # 
  ax.legend(loc='best', numpoints=1)
  plt.savefig('resources/simple_example_2.png', dpi=72)
  # plt.savefig('resources/simple_example_400.png', dpi=200)
  plt.show()

