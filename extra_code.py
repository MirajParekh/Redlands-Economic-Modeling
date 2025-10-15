
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

######## old unemployment calculations (logic error) #############

for _ in range(len(years)):
    unemployed = pop[_]-popEm[_]
    year = years[_]

    total_unemployment_list.append(unemployed)
    graph_years.append(year)




######### combination graph scratch work ###########

def plot_estimates_part6():
    # plt.plot(total_unemployment_list, years_for_unemployment, label = 'line1')
    # plt.plot(employed_population, years_for_unemployment, label = 'line2')
    # plt.show()
    

    print(total_unemployment_list)
    
    # plot lines 
    # plt.plot(years_for_unemployment, employed_population, label = "line 1") 
    # plt.plot(years_for_unemployment, unemployed_population, label = "line 2") 

    plt.legend() 
    plt.show()



simulation
t_0 = 2022
p_0 = 1000
#def plot_estimates_future_pop():
system = System(t_0 = 2022,
            p_0 = 1000,
            alpha = 25 / 1000,
            beta = -1.8 / 1000,
            t_end = 2100)




def growth_func_quad(t, pop, system):
   return system.alpha * pop + system.beta * pop**2




results = run_simulation(system, growth_func_quad)


show(results.tail())


results.plot(color='gray', label='model')
decorate(xlabel='Year',
        ylabel='World population (billions)',
        title='Quadratic model projection')

    
""" printing debugs """
# print("Employed populations and years")
# print(len(new_years_employment))
# print(len(new_population_employment))

# print("\n")

# print("Unmeployed populations and years")
# print(len(unemployed_population))
# print(len(years_for_unemployment))

# print(years_for_unemployment)
# print(new_years_employment)


######### averaging function ###########

def average_data(data_list: list, num_values_reduction: int):
    """Takes a list and reduction value, iterates through list and takes 
    reduction val number of elements and gets the average before adding it to a new list
    till data_list is empty"""
    new_list = [] #empty list
    sum = 0
    while len(data_list) > 0: #iterates through 12 vals
        for i in range(0, num_values_reduction):
            if len(data_list) > 0 :
                sum += data_list[0] #add data_list value
                data_list = data_list[1:] #slice off first value
            else:
                sum += 0
        sum = sum//num_values_reduction
        new_list.append(sum) #add new val to list
    
    return new_list

# Some Test code
# data_list = [1,2,3,4,5,6,7,8,9,10]
# print(average_data(data_list,5)) #expected is 15/ 5 and 40/5. 3 and 8


# total_unemployment_list
# years_for_unemployment
new_list = average_data(employed_population, 12)


######### something something ###########

