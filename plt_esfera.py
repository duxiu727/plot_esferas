# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import copy
from make_cmap import make_cmap

colores= {'g': 'Greens', 'green': 'Greens',          
          'k': 'Greys', 'black': 'Greys',
          'r': 'Reds', 'red': 'Reds',
          'b': 'Blues', 'blue': 'Blues',
          # 'yellow': make_cmap([(248,255,0),(187,180,120)], position=[0,1], bit=True),
          'yellow': make_cmap([(248,255,0),(187,180,120),(184,146,14)], position=[0,0.9,1], bit=True),
          'orange': 'Oranges',
          'seagreen': 'BuGn',
          'darkturquoise': 'GnBu',
          'deeppink': 'PuRd',
          'fuchsia': 'RdPu',
          'purple': 'Purples',
          'blueviolet': 'BuPu',
          'darkred': None
          }

def plot_esfera(ax, x, y, label=None, **kwargs):
  """Plot a curve with yellow spheres"""
  markersize= 6
  for ms in ['markersize','ms']:
    if ms in kwargs:
      markersize= kwargs[ms]

  # default values
  color= colores['black']
  cmap= None

  # if color is associated to a colormap, we set it
  for c in ['color','colour','c']:
    if c in kwargs:
      color= kwargs[c]
      if color in colores:
        cmap= colores[kwargs[c]]
  # argument cmap overwrites the colormap and if color exists, associate it
  if 'cmap' in kwargs:                    
    cmap = kwargs['cmap']
    for k,v in colores.iteritems():
      if cmap == v:
        color= k

  alpha=1.0
  if 'alpha' in kwargs:
    alpha= kwargs['alpha']

  origin= 'upper'
  if 'invert' in kwargs:
    if not kwargs['invert']: origin= False

  # Plot a circle of almost the same size below the curve.
  # This sets scales, labels, etc in the plot automatically using plot machinery
  # or at leat so I hope!
  if alpha < 0.9:
    alpha_l=0.001
  else:
    alpha_l= alpha
  line, = ax.plot(x,y,"o",mfc=color, mec=color, markersize=.5*markersize, label=label, alpha= alpha_l)


  # Read the image to plot
  zoom= 0.004*markersize
  img= plt.imread('sphere.png')

  if color == 'darkred':                  # Use original sphere
    imagebox = OffsetImage(img, zoom=zoom, alpha=alpha, origin=origin)
  else:                                   # Colorize the sphere
    lum_img=img[:,:,0]
    thresh= 1.e-9
    my_cmap = copy.copy(plt.cm.get_cmap(cmap)) # get a copy of the color map
    my_cmap.set_bad(alpha=0) # set how the colormap handles 'bad' values
    maximo= lum_img.max()
    lum_img[lum_img <= thresh] = np.nan # insert 'bad' values (the white)
    lum_img= maximo-lum_img
    imagebox = OffsetImage(lum_img, zoom=zoom, cmap= my_cmap, alpha=alpha, origin=origin)

  for xy in zip(x,y):
    ab = AnnotationBbox(imagebox, xy, xycoords='data', pad=0.1, frameon=False)
    ax.add_artist(ab)


plt.Axes.plot_esfera = plot_esfera


if __name__ == '__main__':
  cmaps = [('Sequential',['Blues', 'BuGn', 'BuPu',
                          'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
                          'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
                          'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
      ('Sequential (2)',['afmhot', 'autumn', 'bone', 'cool', 'copper',
                         'gist_heat', 'gray', 'hot', 'pink',
                         'spring', 'summer', 'winter']),
      ('Diverging',    ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
                        'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral','seismic']),
      ('Qualitative',    ['Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2',
                          'Set1', 'Set2', 'Set3']),
      ('Miscellaneous', ['gist_earth', 'terrain', 'ocean', 'gist_stern', 'brg',
                         'CMRmap', 'cubehelix', 'gnuplot', 'gnuplot2',
                         'gist_ncar', 'nipy_spectral', 'jet', 'rainbow',
                         'gist_rainbow', 'hsv', 'flag', 'prism'])]

  ms= 14
  x= np.linspace(0.1,10,11)
  y= .5*(1.1+ np.sin(x)/(.01+x))
  y1= y+2*len(cmaps[0:1])
  c= None
  for maps in cmaps[0:1]:
    fig= plt.figure(num=maps[0], figsize=(7,9))
    ax= fig.add_subplot(111, aspect='auto')
    for cmap in maps[1]:
      ax.plot_esfera( x,y1, color=c, ms=ms, label=cmap, cmap=cmap)      
      y1-=.9

  # Plot a simple "standard" line
  ax.plot(x,2+(.5+x)*y/(1+x)**2,'-k',lw=3, label='Line 1')
  # 
  ax.legend(loc='best', numpoints=1)
  # plt.savefig('resources/simple_example_2.png')
  plt.show()

  
