#pip3 install plotnine
#pip3 install jupyter

import numpy as np
import pandas as pd
import plotnine

from plotnine import *
from plotnine.data import mtcars

plot = (ggplot(mtcars, aes('wt', 'mpg', color='cyl'))) + geom_point()

fig = plot.draw()
fig.show()

