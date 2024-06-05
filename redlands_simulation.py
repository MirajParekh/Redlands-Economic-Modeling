from os.path import basename, exists
import matplotlib.pyplot as plt

"""Function to download correct file"""
def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)
download('https://github.com/AllenDowney/ModSimPy/raw/master/modsim.py')

from pandas import read_html
from modsim import *

birth_rate = (7.5 + 6.8)/100
death_rate = 7.8/100

growth_rate = birth_rate - death_rate

# start and end year
t_0 = 2022
t_end = 2050

# population
p_0 = 73853


system = System(t_0=t_0, 
                t_end=t_end,
                p_0=p_0,
                annual_growth=annual_growth)

