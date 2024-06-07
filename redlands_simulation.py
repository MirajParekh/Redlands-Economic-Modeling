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

from pandas import read_excel
from modsim import *



# we must implement an equation to make our projection for future population 
# for each given year that we define. In Project 2, we were given that data 
# through 'world_population_estimates.html'. So before we can start 
# creating our system, we have to produce our data with math 

#(Births - deaths) + (in_migration - out_migration) = population change

# for this equation, we must first predict future # of births,deaths,migrations
# patterns. So initially let us model existing data from the past

"""Modeling past data of Redlands, so far only considering total population over time (years)"""
filename = '/home/parekhm/Documents/redlands_pop_data.xlsx'
tables = read_excel(filename, header=1, index_col=0, decimal='M')

years = tables.index
pop = tables.values

#print(years, "\n", pop)
def plot_estimates():
    tables.plot(style=':', label='Redlands Population')
    decorate(xlabel='Year', ylabel='Total Population')


"""migration and projected data will be focused on later"""
# in_migration = 6,521 #2022
# birth_rate = (7.5 + 6.8)/100
# death_rate = 7.8/100

# growth_rate = birth_rate - death_rate

# # start and end year
# t_0 = 2022
# t_end = 2050
# elapsed_time = t_end - t_0

# # population
# p_0 = 73853
# # p_end = to be projected




# system = System(t_0=t_0, 
#                 t_end=t_end,
#                 p_0=p_0,
#                 annual_growth=annual_growth)

