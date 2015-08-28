==============
 plot_esferas
==============

This is a short hack to use spheres as markers in matplotlib plot.
Main idea was borrowed/taken/(use your choice of words) from:
http://matplotlib.1069221.n5.nabble.com/custom-markers-from-images-tp4166p4173.html

I put this together for an easier use in a small function and added it as a method to matplotlib Axes, and I am sharing it in case somebody else finds it useful.

I am sure that there are many better ways to obtain the same result, and I'll be *really* very glad to learn about it.

What does it do?
================

A picture is worth a thousand ...

.. image:: resources/simple_example_1.png


How to use it?
==============
.. code:: python
          
  import numpy as np 
  import matplotlib.pyplot as plt
  import plt_esfera
  
  if __name__ == '__main__':
    fig= plt.figure(figsize=(7,9))
    ax= fig.add_subplot(111, aspect='auto')
  
    x= np.linspace(0.1,10,31)
    y= 1.5*(1+ np.sin(x)/(.01+x))
    y1= y
    for c in plt_esfera.colores.values():
      y1 = y1 + .1
      ax.plot_esfera( x,y1, color=c, markersize=8, label=c)
  
    # Plot a simple "standard" line
    plt.plot(x,2+(.5+x)*y/(1+x)**2,'-k',lw=3, label='Line 1')
    # 
    plt.legend(loc='best', numpoints=1)
    plt.savefig('resources/simple_example_2.png')
    plt.show()

