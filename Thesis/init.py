#installing packages
#pip install "fastf1"
#import fastf1
#%%

#installing libraries
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm

import fastf1 as ff1
from fastf1.core import Laps
from fastf1 import utils
from fastf1 import plotting
plotting.setup_mpl()

from timple.timedelta import strftimedelta
#%%

#directing to cache folder for data storage
ff1.Cache.enable_cache('"C:\\Users\\andre\\OneDrive\\Desktop\\Thesis\\cache"')

#%%

#checking that some data is loaded
#https://pandeyparul.medium.com/accessing-formula-1-races-historical-data-using-python-b7c80e544f50

abu_dhabi_qualification = ff1.get_session(2021, 'Abu Dhabi', 'Q')
print(abu_dhabi_qualification.date)

#%%

