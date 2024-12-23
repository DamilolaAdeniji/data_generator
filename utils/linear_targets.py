import pandas as pd
import numpy as np

"""
This can be used to generate a dataframe of linearly distributed values against set targets
This can only be used for integrs at the moment
"""
def linear_targets(start_value = 1, end_value = 1000, num_points=7):
    linear_numbers = np.linspace(start_value, end_value, num_points)
    linear_numbers = [int(x) for x in linear_numbers]
    print (linear_numbers)
    lin = [1]
    for num in range(1,num_points):
        lin.append(linear_numbers[num] - linear_numbers[num - 1])
    # Return the values as integers
    return lin

# using ....

def target_dataframe_gen(**kwargs):
    """
    I require the following to run successfully
    start_year,end_year,targets= {
        'target1':2000,
    'target2':1000...
    }
    """
    # get the values
    start_year = kwargs.get('start_year')
    end_year = kwargs.get('end_year')
    targets = kwargs.get('targets')

    # get the time range
    years = range(start_year,end_year)
    df = pd.DataFrame({'Date':years})

    # create cols by looping over each target
    for key, target_value in targets.items():
        df[key] = linear_targets(end_value=target_value, num_points=len(years))
    
    return df 



if __name__ == '__main__':
    df  = target_dataframe_gen(
        start_year = 2023,
        end_year = 2029,
        targets= {
        'target1':2500000,
        'target2':75000,
        'target3':1200000,
        'target4':45,
        'target5':150000000,
        'target6':200000000
        })

    df.to_csv('testing_this_out.csv',index=False)