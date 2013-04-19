from xkcdify import xkcdify
import matplotlib.pyplot as pp
import numpy as np

# construct some data -- two dsitributions with different centers
x = np.linspace(-3,3, 1000)
y1 = 3*np.exp(-(x-1)**2)
y2 = np.exp(-(x+1)**2)


# plot the data, along with a black line in between
pp.plot(x, y1, 'b', lw=1, label='cats')
pp.plot([-0.3, -0.3], [0, 1.1*max(y1)], 'k', lw=1)
pp.plot(x, y2, 'r', lw=1, label='not cats')

pp.legend()
pp.xlabel('score')
pp.ylabel('freq')

# use the xkcdify code from jakevp
# http://jakevdp.github.io/blog/2012/10/07/xkcd-style-plots-in-matplotlib/
xkcdify()
pp.tight_layout()
pp.savefig('classifier2.png')

# then I went into gimp and made a few mofifications to shrink the plot further
