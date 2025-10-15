from os.path import basename, exists
import matplotlib.pyplot as plt
import random as rand

"""Function to download correct file"""
def download(url):
    filename = basename(url)
    if not exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded ' + local)
download('https://github.com/AllenDowney/ModSimPy/raw/master/modsim.py')

import pandas as pd
import matplotlib as plt
from pandas import read_excel
from pandas import read_csv
from modsim import *
import numpy as np
import matplotlib.pyplot as pyplt #access to pyplot functions. Otherwise its plt.pyplot]


# we must implement an equation to make our projection for future population 
# for each given year that we define. In Project 2, we were given that data 
# through 'world_population_estimates.html'. So before we can start 
# creating our system, we have to produce our data with math 

#(Births - deaths) + (in_migration - out_migration) = population change

# for this equation, we must first predict future # of births,deaths,migrations
# patterns. So initially let us model existing data from the past

"""Modeling past data of Redlands, so far only considering total population over time (years)"""
filename = '/home/parekhm/Desktop/final_project/redlands_data/redlands_pop_data.xlsx'
tables = read_excel(filename, header=1, index_col=0, decimal='M')

years = tables.index
pop = tables.values

""" years var for all plots  """
last_decade = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2022]
graph_years = []
for year in years:
    graph_years.append(year)


redlands_pop_list = [] 
for number in pop:
    redlands_pop_list.append(number[0])


""" plotting population over time """
def plot_estimates_part1():
    plt.plot(graph_years, redlands_pop_list)
    decorate(title = 'Redlands Total Population Over Time',
             xlabel = 'Years',
             ylabel = 'Population')
    
    pop_plot = plt.gca()
    pop_plot.set_ylim(0)
    


def growth_func_quad(t, pop, system):
    '''
    quadratic growth function from Chap7
    '''
    return system.alpha * pop + system.beta * pop**2

def run_simulation(system, growth_func):
    '''
    This run_simulation function can run with any models because it takes the growth func as a param.
    '''
    results = TimeSeries()
    results[system.t_0] = system.p_0

    for t in range(system.t_0, system.t_end):
        growth = growth_func(t, results[t], system)
        results[t+1] = results[t] + growth

    return results


"""
This was an attempt at projecting population in redlands. Reasons for failure was lack 
of available data we could use to make it accurate (ie birth rate, death rate, etc)
"""
# #from 2022 and beyond? if so then p_0 is 72853
# def plot_estimates_part1_future(): #time is in thousands
#     '''modeling population growth ahead of present 2022 data.'''
#     birth_rate = 14.3/1000
#     death_rate = 7.8/1000


#     growth_rate = birth_rate - death_rate
       
#     system = System(t_0 = 2022,
#                     t_end = 2072,
#                     alpha = 25 / 1000,#not billion but instead thousands
#                     beta = -1.8 / 1000,
#                     p_0 = 73853/1e4)
#     results = run_simulation(system, growth_func_quad)
#     print(results.tail()) #instead of show
#     future_pop_plot = results.plot(color = 'green', label = 'Redlands population growth')
#     decorate(xlabel='Year',
#             ylabel='Population (ten-thousands)',
#             title='Quadratic model projection')
#     plot_estimates_part1()
#     decorate(title='Redlands Total Population Over Time')
#     future_pop_plot.set_ylim(bottom=0)


# part 2 - total number of people in labor force
#  
# current data is that redlands has a 63 percent labor force participation rate,
# in order to calculate future factors, we will use this percent as a constant 
# in the scope of this project to find number of people in labor force over years

labor_force = [] 
participation_rate = .63

for pop in redlands_pop_list:
    labor_force.append(pop * participation_rate)

""" Modeling labor force participation rate """
def plot_estimates_part2():
    plt.plot(graph_years, labor_force)
    decorate(title = 'Number in Labor Force',
             xlabel = 'Years',
             ylabel = 'Number of People in Labor Force')
    
    labor_force_plot = plt.gca()
    labor_force_plot.set_ylim(0)


# Part 3 - Unemployment and employment #
"""Modeling past data of Redlands, so far only considering total unemployment over time (years)"""


"""Modeling past data of Redlands, so far only considering total employment over time (years)"""
filename_Employment = '/home/parekhm/Desktop/final_project/redlands_data/employment.csv'
tablesEm = read_csv(filename_Employment, header=1, index_col=0, decimal='M')

yearsEm = tablesEm.index
popEm = tablesEm.values

filename_unemployment = '/home/parekhm/Desktop/final_project/redlands_data/unemployment_rate.csv'
unemployment_table = read_csv(filename_unemployment)

popUnem = unemployment_table.values

unemployed_population_rate = []
total_unemployment_rate_list = [] 

employed_population = [] 
total_employed_list = []


# fill up unemployed_population & employed_population
for number in popUnem:
    unemployed_population_rate.append(number[1])

for number in popEm:
    employed_population.append(number[0])



# for the unemployed population
counter = 0 

for pop in unemployed_population_rate:
    if counter == 11:
        total_unemployment_rate_list.append(pop)
        counter = 0 

    else:
        counter += 1


# for the employed  population
for pop in employed_population:
    if counter == 11:
        total_employed_list.append(pop)
        counter = 0 

    else:
        counter += 1



# cutting off last 2 values to match number of data points 
for _ in range(2):
    total_unemployment_rate_list.pop(-1)
    total_employed_list.pop(-1)


""" plotting the total number of people employed in Redlands """
def plot_estimates_part3a():
    plt.plot(graph_years, total_employed_list)
    decorate(xlabel='Years',
             ylabel='Number Employed', 
             title='Total # of People Employed over Years')
    emPlot = plt.gca()
    emPlot.set_ylim(0)


# 3b - rotal number of people unemployed #
total_unemployed_list = []

for _ in range(len(graph_years)):
    number_unemployed = int((unemployed_population_rate[_]/10) * labor_force[_])
    total_unemployed_list.append(number_unemployed)


""" plotting the total number of people unemployed in Redlands """
def plot_estimates_part3b():
    plt.plot(years, total_unemployed_list)
    decorate(xlabel='Year', ylabel='Total Unemployment', )
    
    unem_plot = plt.gca()
    unem_plot.set_ylim(0)



# part 4 - median personal individual income # 

filename_individual_income = '/home/parekhm/Desktop/final_project/redlands_data/redlands_individual_income.csv'
tables_income = read_csv(filename_individual_income, header=1, index_col=0, decimal='M')

individual_income = tables_income.values
individual_income_list = []

for income in individual_income:
    individual_income_list.append(income[0])


"""Plotting median individual income"""
def plot_estimates_part4():
    plt.plot(last_decade, individual_income_list)

    decorate(xlabel='Year',
             ylabel = 'Income',
             title='Median Income of Population')
    
    individual_income_plot = plt.gca()
    individual_income_plot.set_ylim(0)


# part 5 - Poverty Rate # 

filename_poverty = '/home/parekhm/Desktop/final_project/redlands_data/poverty_rate.csv'
tables_poverty = read_csv(filename_poverty, header=1, index_col=0, decimal='M')

poverty_rate_list = [] 

for number in tables_poverty.values:
    poverty_rate_list.append(float(number[0]))

def plot_estimates_part5():
    plt.plot(last_decade, poverty_rate_list)

    decorate(xlabel='Year',
             ylabel = 'poverty rate',
             title='Redlands Poverty Rate')
    
    poverty_plot = plt.gca()
    poverty_plot.set_ylim(0)


# part 6 - combination graph 1 (total people employed vs total people unemployed) 

"""Combo plot 1 (Employment): employed vs unemployed vs labor force"""
def plot_estimates_part6():
    plt.plot(graph_years, total_unemployed_list, label = "# of Unemployed")
    plt.plot(graph_years, total_employed_list, label = "# of Employed")
    plt.plot(graph_years, labor_force, label = "# in Labor Force")

    decorate(title="Combo plot 1: # Employed vs # Unemployed vs # in Labor Force")
    combo_plot_1 = plt.gca()
    combo_plot_1.set_ylim(0)


# part 7 - # of people in povery (takes poverty rate & total population over years)
#
# poverty num = rate(yr) * total pop(yr) --> we take this equation to calculate to number of people in poverty at every year 

poverty_num_list = [] 
pop_counter = 2011-1990

for _ in range(len(last_decade)):
    poverty_num_list.append(int(poverty_rate_list[_] * redlands_pop_list[pop_counter]))
    pop_counter += 1 


"""Total number of people in poverty over years"""
def plot_estimates_part7():
    plt.plot(last_decade, poverty_num_list)

    decorate(xlabel='Year',
             ylabel = 'Number of People',
             title='Total # of People in Poverty over Years')
    
    poverty_num_plot = plt.gca()
    poverty_num_plot.set_ylim(0)

# part 8 - Combo graph 2 (labor force, employed, unemployed, poverty, total population)

"""Plot combo graph 2 """
def plot_estimates_part8():
    plt.plot(graph_years, redlands_pop_list, label="Total Population")
    plt.plot(graph_years, total_unemployed_list, label = "# of Unemployed")
    plt.plot(graph_years, total_employed_list, label = "# of Employed")
    plt.plot(graph_years, labor_force, label = "# in Labor Force")
    plt.plot(last_decade, poverty_num_list, label = "# in Poverty")

    decorate(xlabel='Year',
             ylabel='Population',
             title='Population Metrics')
    combo2 = plt.gca()
    combo2.set_ylim(0)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')



### HELPER METHODS FOR PART 10 ###

"""rate of change over last year"""
def final_year_change(data_list):
    return data_list[-1] - data_list[-2]

"""rate of change over entirety of list"""
def average_change(data_list):
    return (data_list[-1] - data_list[0]) / len(data_list)

"""returns the last element in a list"""
def get_last_value(data_list):
    myVar = data_list[-1]

    return data_list[-1]


# part 10 - simulating future individual median income 
#
# simulation part, our algorithm takes 2022 modeled numbers from all the other factors and uses them to add or remove 
# from the median income projection. Then, we randomize the weight of the impact for each factor in order to account 
# for noise in the simulation. We do this for each year.


#other values that we get the change range of each, one is recent and one is overtime
#poverty
long_change_poverty = average_change(poverty_num_list)
recent_change_poverty = final_year_change(poverty_num_list)
#labor force
long_change_labor = average_change(labor_force)
recent_change_labor  = final_year_change(labor_force)
#population
long_change_pop = average_change(redlands_pop_list)
recent_change_pop = final_year_change(redlands_pop_list)
#unemployed
long_change_unemployed = average_change(total_unemployed_list)
recent_change_unemployed = final_year_change(total_unemployed_list)
#employed
long_change_employed = average_change(total_employed_list)
recent_change_employed= final_year_change(total_employed_list)

#median income individual 
long_change_indiv_income = average_change(individual_income_list)
recent_change_indiv_income = final_year_change(individual_income_list)

start_indiv_value = get_last_value(individual_income_list)


""" calculates the values for projected median income for an inputted end_yr """
def plot_estimates_part10_algorithm(lo_impact_val, hi_impact_val, initial_val, indiv_income, poverty,labor,population,unemployed,employed, end_yr): #all rates
    indiv_income_rate = indiv_income
    
    #impacts of every rate
    #Looking at long change
    start_year = 2022
    randomized_value_list = [initial_val]
    years_list = [start_year]
    iterate_year_value = start_year

    for _ in range(end_yr - start_year): #makes years list
        iterate_year_value+=1
        years_list.append(iterate_year_value)


    while start_year < end_yr:
        indiv_income_rate = indiv_income
        # indiv_income_rate = indiv_income
        if rand.randint(0,2) > 1: #randomly increases by its actual predicted rate
            indiv_income_rate += indiv_income

        if poverty >0: #higher poverty means lower income
            low_impact = poverty/ lo_impact_val
            high_impact = poverty/hi_impact_val#high and low impact randomness simulates the 'noise' in the model
            indiv_income_rate -= rand.uniform(low_impact, high_impact)

        if unemployed >0: #higher unemployment means lower income
            low_impact = unemployed/lo_impact_val
            high_impact = unemployed/hi_impact_val#high and low impact randomness simulates the 'noise' in the model
            indiv_income_rate -= rand.uniform(low_impact, high_impact)

        if employed >0: #higher employment means higher income
            low_impact = employed/lo_impact_val
            high_impact = employed/hi_impact_val#high and low impact randomness simulates the 'noise' in the model
            indiv_income_rate += rand.uniform(low_impact, high_impact)

        if labor>0: #higher labor means higher income
            low_impact = labor/lo_impact_val
            high_impact = labor/hi_impact_val#high and low impact randomness simulates the 'noise' in the model
            indiv_income_rate += rand.uniform(low_impact, high_impact)

        if population>0: #neutral for now.
            indiv_income_rate = indiv_income_rate

        randomized_value_list.append(indiv_income_rate)
        start_year += 1 

    return years_list, randomized_value_list

""" Plots our results from the algorithm to make a projection for future individual median income """
def plot_estimates_part10(years_list, impacted_value_list): 
    plt.plot(years_list, impacted_value_list)
    decorate(title="Projected Median Individual Income",
             xlabel='Years',
             ylabel="Money")
    
    projected_income_plot = plt.gca()
    projected_income_plot.set_ylim(0)


# part 11 - inflation combo graph 
#
# according to the st louis fed, the past 30 year inflation per year on 
# average has been 2.5 percent, this is what we will use as our constant
# to add onto our projected income growth by inflation 
years_list, impacted_value_list = plot_estimates_part10_algorithm(0.05,0.045,start_indiv_value,recent_change_indiv_income, recent_change_poverty,recent_change_labor,recent_change_pop,recent_change_unemployed,recent_change_employed, 2100)

inflation_rate = 0.025
inflated_value_list = []

for i in range(len(impacted_value_list)):
    # Calculate the inflation factor for each year
    inflation_factor = (1 + inflation_rate) ** i
    # Adjust the income value for inflation
    inflated_value = impacted_value_list[i] * inflation_factor
    inflated_value_list.append(inflated_value)

"""Projected Income vs Projected Income Considering Inflation"""
def plot_estimates_part11():
    plt.plot(years_list, impacted_value_list, label="Projected Median Income for Redlands Resident")
    plt.plot(years_list, inflated_value_list, label="Projected Median Income for Redlands Resident Considering Inflation")

    plt.xlabel('Year')
    plt.ylabel('Dollars')
    plt.title('Projected Income vs Projected Income Considering Inflation')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()






