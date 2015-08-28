# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

colores= {'gr': 'green',
          'or':'orange',
          'da': 'darkred',
          'bl': 'blue',
          'li': 'lightblue',
          'sk': 'skyblue',
          'ye': 'yellow',
          'pi': 'pink',
          }

def plot_esfera(ax, x, y, label=None, **kwargs):
  """Plot a curve with yellow spheres"""
  markersize= 6
  for ms in ['markersize','ms']:
    if ms in kwargs:
      markersize= kwargs[ms]

  color= colores['or']
  for c in ['color','colour','c']:
    if c in kwargs:
      color= colores[kwargs[c][0:2].lower()]
  
  # Read the image to plot
  zoom= 0.004*markersize
  img= plt.imread('{}_sphere.png'.format(color))

  # Plot a circle of almost the same size below the curve.
  # This sets scales, labels, etc in the plot automatically using plot machinery
  # or at leat so I hope!
  line, = ax.plot(x,y,"o",mfc=color, mec=color, markersize=.95*markersize, label=label)

  handles= []
  for xy in zip(x,y):
    imagebox = OffsetImage(img, zoom=zoom, cmap=plt.get_cmap('Blues'))
    ab = AnnotationBbox(imagebox, xy, xycoords='data', pad=0.1, frameon=False)
    ax.add_artist(ab)

plt.Axes.plot_esfera = plot_esfera


