import pandas as pd
import numpy as np
import urllib
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
from functools import reduce

# The dictionaries for months, UTs and States
months = {
    'Jan' : '01', 'Feb' : '02',
    'Mar' : '03', 'Apr' : '04',
    'May' : '05', 'Jun' : '06', 
    'Jul' : '07', 'Aug' : '08', 
    'Sep' : '09', 'Oct' : '10', 
    'Nov' : '11', 'Dec' : '12'
}
# Considering Delhi as a state
states = {
    'ap' : 'Andhra Pradesh',
    'ar' : 'Arunachal Pradesh',
    'as' : 'Assam',
    'br' : 'Bihar',
    'nl' : 'Nagaland',
    'mz' : 'Mizoram',
    'sk' : 'Sikkim',
    'rj' : 'Rajasthan',
    'or' : 'Odisha',
    'hp' : 'Himachal Pradesh',
    'up' : 'Uttar Pradesh',
    'jh' : 'Jharkhand',
    'ct' : 'Chhattisgarh',
    'pb' : 'Punjab',
    'kl' : 'Kerala',
    'tn' : 'Tamil Nadu',
    'ut' : 'Uttarakhand',
    'hr' : 'Haryana',
    'jk' : 'Jammu And Kashmir',
    'mh' : 'Maharashtra',
    'ka' : 'Karnataka',
    'gj' : 'Gujarat',
    'dl' : 'Delhi',
    'tg' : 'Telangana',
    'tr' : 'Tripura',
    'mp' : 'Madhya Pradesh',
    'wb' : 'West Bengal',
    'mn' : 'Manipur',
    'ga' : 'Goa'
}
union_territories = {
    'an' : 'Andaman and Nicobar Islands',
    'py' : 'Puducherry',
    'ch' : 'Chandigarh',
    'py' : 'Puducherry',
    'dn' : 'Dadara & Nagar Haveli & Daman & Diu',
    'la' : 'Ladakh',
    'ld' : 'Lakshadweep'   
}

def generate_date(record):
    day = record['date'][:2]
    month = months[record['date'][3:6]]
    year = record['date'][7:]
#     Assuming that dates before 1920 wouldn't be present in the data
    if year <= '20':
        year = '20' + year
    else:
        year = '19' + year
    date_of_record = year + '-' + month + '-' + day
    return date_of_record

def Q1_1(json_file_path, start_date, end_date):
    """Q1_1 function
    Count the total number of “Confirmed”, “Recovered” and “Deceased” 
    from start_date to end date and report the numbers.
    
    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json(json_file_path, orient = 'index')

    confirmed_count = 0
    recovered_count = 0
    deceased_count = 0

    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    for param in record:
                        if param in states or param in union_territories:
                            confirmed_count += int(record[str(param)])
                elif record['status'] == 'Recovered':
                    for param in record:
                        if param in states or param in union_territories:
                            recovered_count += int(record[str(param)])
                elif record['status'] == 'Deceased':
                    for param in record:
                        if param in states or param in union_territories:
                            deceased_count += int(record[str(param)])
                        
    print('confirmed_count:',confirmed_count, 'recovered_count:',recovered_count, 'deceased_count:',deceased_count)

    return confirmed_count, recovered_count, deceased_count

def Q1_2(json_file_path, start_date, end_date):
    """Q1_2 function
    Count the total number of “Confirmed”, “Recovered” and “Deceased” for 
    the state Delhi from start_date to end date and report the numbers.

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json(json_file_path, orient = 'index')

    confirmed_count = 0
    recovered_count = 0
    deceased_count = 0

    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    confirmed_count += int(record['dl'])
                elif record['status'] == 'Recovered':
                    recovered_count += int(record['dl'])
                elif record['status'] == 'Deceased':
                    deceased_count += int(record['dl'])
                        
    print('confirmed_count:',confirmed_count, 'recovered_count:',recovered_count, 'deceased_count:',deceased_count)
    
    return confirmed_count, recovered_count, deceased_count

def Q1_3(json_file_path, start_date, end_date):
    """Q1_3 function
    Count the total number of “Confirmed”, “Recovered” and “Deceased” for 
    the state Delhi and Maharashtra (Sum) from start_date to end date and report the numbers.

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json(json_file_path, orient = 'index')

    confirmed_count = 0
    recovered_count = 0
    deceased_count = 0

    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    confirmed_count += int(record['dl']) + int(record['mh'])
                elif record['status'] == 'Recovered':
                    recovered_count += int(record['dl']) + int(record['mh'])
                elif record['status'] == 'Deceased':
                    deceased_count += int(record['dl']) + int(record['mh'])

    print('confirmed_count:',confirmed_count, 'recovered_count:',recovered_count, 'deceased_count:',deceased_count)
    
    return confirmed_count, recovered_count, deceased_count

def Q1_4(json_file_path, start_date, end_date):
    """Q1_4 function
    Report the highest affected state in terms of “Confirmed”, “Recovered” and “Deceased”
    with the count from the start_date to the end_date

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json(json_file_path, orient = 'index')

    states_count = {state : [0,0,0] for state in states}

    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    for param in record:
                        if param in states:
                            states_count[str(param)][0] += int(record[str(param)])
                elif record['status'] == 'Recovered':
                    for param in record:
                        if param in states:
                            states_count[str(param)][1] += int(record[str(param)])
                elif record['status'] == 'Deceased':
                    for param in record:
                        if param in states:
                            states_count[str(param)][2] += int(record[str(param)])
    
    confirmed_state = []
    confirmed_state_val = -1
    recovered_state = []
    recovered_state_val = -1
    deceased_state = []
    deceased_state_val = -1

    for state in states_count:
        if states_count[state][0] > confirmed_state_val:
            confirmed_state_val = states_count[state][0]
            confirmed_state = [states[str(state)]]
        if states_count[state][1] > recovered_state_val:
            recovered_state_val = states_count[state][1]
            recovered_state = [states[str(state)]]
        if states_count[state][2] > deceased_state_val:
            deceased_state_val = states_count[state][2]
            deceased_state = [states[str(state)]]
    #     If multiple states have the same value
        if states_count[state][0] == confirmed_state_val:
            confirmed_state.append(states[str(state)])
        if states_count[state][1] == recovered_state_val:
            recovered_state.append(states[str(state)])
        if states_count[state][2] == deceased_state_val:
            deceased_state.append(states[str(state)])

    # Remove duplicates
    confirmed_state = list(set(confirmed_state))
    recovered_state = list(set(recovered_state))
    deceased_state = list(set(deceased_state))

    print('Confirmed')
    print('Highest affected State(s) is:', ' '.join(confirmed_state))
    print('Highest affected State count is: ', confirmed_state_val)
    print('Recovered')
    print('Highest affected State(s) is:', ' '.join(recovered_state))
    print('Highest affected State count is:', recovered_state_val)
    print('Deceased')
    print('Highest affected State(s) is:', ' '.join(deceased_state))
    print('Highest affected State count is:', deceased_state_val)

    return confirmed_state, confirmed_state_val, recovered_state, recovered_state_val, deceased_state, deceased_state_val


def Q1_5(json_file_path, start_date, end_date):
    """Q1_5 function
    Report the lowest affected state in terms of “Confirmed”, “Recovered” and “Deceased”
    with the count from the start_date to the end_date

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json(json_file_path, orient = 'index')

    states_count = {state : [0,0,0] for state in states}

    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    for param in record:
                        if param in states:
                            states_count[str(param)][0] += int(record[str(param)])
                elif record['status'] == 'Recovered':
                    for param in record:
                        if param in states:
                            states_count[str(param)][1] += int(record[str(param)])
                elif record['status'] == 'Deceased':
                    for param in record:
                        if param in states:
                            states_count[str(param)][2] += int(record[str(param)])

    # Assuming no state has 10 Cr cases in any field
    upper_cap = 100000000
    confirmed_state = []
    confirmed_state_val = upper_cap
    recovered_state = []
    recovered_state_val = upper_cap
    deceased_state = []
    deceased_state_val = upper_cap

    for state in states_count:
        if states_count[state][0] < confirmed_state_val:
            confirmed_state_val = states_count[state][0]
            confirmed_state = [states[str(state)]]
        if states_count[state][1] < recovered_state_val:
            recovered_state_val = states_count[state][1]
            recovered_state = [states[str(state)]]
        if states_count[state][2] < deceased_state_val:
            deceased_state_val = states_count[state][2]
            deceased_state = [states[str(state)]]
    #     If multiple states have the same value
        if states_count[state][0] == confirmed_state_val:
            confirmed_state.append(states[str(state)])
        if states_count[state][1] == recovered_state_val:
            recovered_state.append(states[str(state)])
        if states_count[state][2] == deceased_state_val:
            deceased_state.append(states[str(state)])

    # Remove duplicates
    confirmed_state = list(set(confirmed_state))
    recovered_state = list(set(recovered_state))
    deceased_state = list(set(deceased_state))

    print('Confirmed \n')
    print('Lowest affected State(s) is:', ' '.join(confirmed_state))
    print('Lowest affected State count is: ', confirmed_state_val)
    print()
    print('Recovered \n')
    print('Lowest affected State(s) is:', ' '.join(recovered_state))
    print('Lowest affected State count is:', recovered_state_val)
    print()
    print('Deceased \n')
    print('Lowest affected State(s) is:', ' '.join(deceased_state))
    print('Lowest affected State count is:', deceased_state_val)
    
    return confirmed_state, confirmed_state_val, recovered_state, recovered_state_val, deceased_state, deceased_state_val


def Q1_6(json_file_path, start_date, end_date):
    """Q1_6 function
    Find the day and count with the highest spike in a day in the number of cases for the
    state Delhi for “Confirmed”, “Recovered” and “Deceased” between start_date and end_date

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json(json_file_path, orient = 'index')

    confirmed_date = []
    confirmed_date_val = -1
    recovered_date = []
    recovered_date_val = -1
    deceased_date = []
    deceased_date_val = -1

    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    if confirmed_date_val < int(record['dl']):
                        confirmed_date = [date_of_record]
                        confirmed_date_val = int(record['dl'])
                    elif confirmed_date_val == int(record['dl']):
                        confirmed_date.append(date_of_record)
                elif record['status'] == 'Recovered':
                    if recovered_date_val < int(record['dl']):
                        recovered_date = [date_of_record]
                        recovered_date_val = int(record['dl'])
                    elif recovered_date_val == int(record['dl']):
                        recovered_date.append(date_of_record)
                elif record['status'] == 'Deceased':
                    if deceased_date_val < int(record['dl']):
                        deceased_date = [date_of_record]
                        deceased_date_val = int(record['dl'])
                    elif deceased_date_val == int(record['dl']):
                        deceased_date.append(date_of_record)

    # Remove duplicates
    confirmed_date = list(set(confirmed_date))
    recovered_date = list(set(recovered_date))
    deceased_date = list(set(deceased_date))

    print('Confirmed \n')
    print('Day(s): ', ' '.join(confirmed_date))
    print('Count: ', confirmed_date_val)
    print()
    print('Recovered \n')
    print('Day(s): ', ' '.join(recovered_date))
    print('Count: ', recovered_date_val)
    print()
    print('Deceased \n')
    print('Day(s): ',' '.join(deceased_date))
    print('Count: ', deceased_date_val)

    return confirmed_date, confirmed_date_val, recovered_date, recovered_date_val, deceased_date, deceased_date_val

def Q1_7(json_file_path, start_date, end_date):
    """Q1_7 function : 
    Report active cases (Assume active = Confirmed - (Recovered + Deceased)) state wise
    for all states separately on the end_date

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json(json_file_path, orient = 'index')

    states_count = {state : 0 for state in states}
    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    for param in record:
                        if param in states:
                            states_count[str(param)] += int(record[str(param)])
                elif record['status'] == 'Recovered':
                    for param in record:
                        if param in states:
                            states_count[str(param)] -= int(record[str(param)])
                elif record['status'] == 'Deceased':
                    for param in record:
                        if param in states:
                            states_count[str(param)] -= int(record[str(param)])
                            
    result = {states[key] : states_count[key] for key in states_count}
    print("Active cases in each state")
    print('\n'.join(f'{k}: {v}' for k,v in result.items())) # print any way you want
    
    return result


def Q2_1(json_file_path, start_date, end_date):
    """Q2 function
    Plot the area trend line for total “Confirmed”, “Recovered” and “Deceased”
    cases from start_date to end_date

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json('data.json', orient = 'index')

    df_confirmed = pd.DataFrame()
    df_recovered = pd.DataFrame()
    df_deceased = pd.DataFrame()

    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            confirmed_count = 0
            recovered_count = 0
            deceased_count = 0
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    for param in record:
                        if param in states or param in union_territories:
                            confirmed_count += int(record[str(param)])
                    df_confirmed[date_of_record] = [confirmed_count]
                elif record['status'] == 'Recovered':
                    for param in record:
                        if param in states or param in union_territories:
                            recovered_count += int(record[str(param)])
                    df_recovered[date_of_record] = [recovered_count]
                elif record['status'] == 'Deceased':
                    for param in record:
                        if param in states or param in union_territories:
                            deceased_count += int(record[str(param)])
                    df_deceased[date_of_record] = [deceased_count]

    # Merge the Dataframes
    frames = [df_confirmed, df_recovered, df_deceased]
    df = reduce(lambda left, right: pd.merge(left, right, how = 'outer'), frames)

    # Saving and loading as Excel file
    df.to_excel('Daywise_Cases.xlsx', index = False)
    df = pd.read_excel('Daywise_Cases.xlsx')

    # Renaming record names
    df.index = ['Confirmed Cases', 'Recovered Cases', 'Deceased Cases']
    df.columns = list(map(str, df.columns))

    # Plotting Area Graph
    df = df.transpose()
    df.plot(kind = 'area', stacked = False, figsize = (18, 8))
    plt.title('Cases per day for India')
    plt.ylabel('Number of Cases')
    plt.xlabel('Dates')
    plt.savefig('Q_2_1.png')
    plt.show()
    

def Q2_2(json_file_path, start_date, end_date):
    """Q2 function
    Plot the area trend line for total “Confirmed”, “Recovered” and “Deceased”
    cases for Delhi from start_date to end_date

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json('data.json', orient = 'index')

    df_confirmed = pd.DataFrame()
    df_recovered = pd.DataFrame()
    df_deceased = pd.DataFrame()

    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            confirmed_count = 0
            recovered_count = 0
            deceased_count = 0
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    confirmed_count += int(record['dl'])
                    df_confirmed[date_of_record] = [confirmed_count]
                elif record['status'] == 'Recovered':
                    recovered_count += int(record['dl'])
                    df_recovered[date_of_record] = [recovered_count]
                elif record['status'] == 'Deceased':
                    deceased_count += int(record['dl'])
                    df_deceased[date_of_record] = [deceased_count]

    # Merge the Dataframes
    frames = [df_confirmed, df_recovered, df_deceased]
    df = reduce(lambda left, right: pd.merge(left, right, how = 'outer'), frames)

    # Saving and loading as Excel file
    df.to_excel('Daywise_Cases_Delhi.xlsx', index = False)
    df = pd.read_excel('Daywise_Cases.xlsx')
    
    # Renaming record names
    df.index = ['Confirmed Cases', 'Recovered Cases', 'Deceased Cases']
    df.columns = list(map(str, df.columns))

    # Plotting Area Graph
    df = df.transpose()
    df.plot(kind = 'area', stacked = False, figsize = (18, 8))
    plt.title('Cases per day for Delhi')
    plt.ylabel('Number of Cases')
    plt.xlabel('Dates')
    plt.savefig('Q_2_2.png')
    plt.show()
    


def Q2_3(json_file_path, start_date, end_date):
    """Q2 function
    Plot the area trend line for active cases. Assume 
    active = Confirmed - (Recovered + Deceased) from start_date to end_date

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    data = pd.read_json('data.json', orient = 'index')

    df_active = pd.DataFrame()

    count = 0
    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    for param in record:
                        if param in states or param in union_territories:
                            count += int(record[str(param)])
                elif record['status'] == 'Recovered':
                    for param in record:
                        if param in states or param in union_territories:
                            count -= int(record[str(param)])
                elif record['status'] == 'Deceased':
                    for param in record:
                        if param in states or param in union_territories:
                            count -= int(record[str(param)])
                    df_active[date_of_record] = [count]

    # Saving and loading as Excel file
    df_active.to_excel('Daywise_Active_Cases.xlsx', index = False)
    df = pd.read_excel('Daywise_Active_Cases.xlsx')

    # Renaming the Record name
    df.index = ['Active Cases']
    df.columns = list(map(str, df.columns))

    # Plotting the area graph
    df = df.transpose()
    df.plot(kind = 'area', stacked = False, figsize = (18, 8))
    plt.title('Active Cases per day')
    plt.ylabel('Number of Cases')
    plt.xlabel('Dates')
    plt.savefig('Q_2_3.png')
    plt.show()

def Q3(json_file_path, start_date, end_date):
    """Q3 function
    Implement a linear regression on the state Delhi data over dates, separately for
    “Confirmed”, “Recovered” or “Deceased” and report intercept and slope coefficients for
    all 3 cases from the start_date to end_date

    Args:
        json_file_path (TYPE): File path of the JSON file to access
        start_date (TYPE): Start date of data retrieval
        end_date (TYPE): End date of data retrieval
    """
    # Line is y = mx + c
    data = pd.read_json('data.json', orient = 'index')

    days = 1
    confirmed = []
    recovered = []
    deceased = []

    for i in data:
        for record in data[i]:
            date_of_record = generate_date(record)
            if date_of_record <= end_date and date_of_record >= start_date:
                if record['status'] == 'Confirmed':
                    confirmed.append(int(record['dl']))
                elif record['status'] == 'Recovered':
                    recovered.append(int(record['dl']))
                elif record['status'] == 'Deceased':
                    deceased.append(int(record['dl']))
                    days += 1

    # X co-ordinates 
    dates = [i for i in range(1, days)]

    m = np.mean(dates)
    v = np.var(dates)

    # Calculation of Slope and intercept of Confirmed cases
    confirmed_slope = np.cov(dates, confirmed)[0][1] / v
    confirmed_intercept = np.mean(confirmed) - (m * confirmed_slope)

    # Calculation of Slope and intercept of Recovered cases
    recovered_slope = np.cov(dates, recovered)[0][1] / v
    recovered_intercept = np.mean(recovered) - (m * recovered_slope)

    # Calculation of Slope and intercept of Deceased cases
    deceased_slope = np.cov(dates, deceased)[0][1] / v
    deceased_intercept = np.mean(deceased) - (m * deceased_slope)

    print('Confirmed Slope:', confirmed_slope, 'Confirmed Intercept:', confirmed_intercept)
    print('Recovered Slope:', recovered_slope, 'Recovered Intercept:', recovered_intercept)
    print('Deceased Slope:', deceased_slope, 'Deceased Intercept:', deceased_intercept)

    return confirmed_intercept, confirmed_slope, recovered_intercept, recovered_slope, deceased_intercept, deceased_slope


if __name__ == "__main__":
    # execute only if run as a script
    print(OUTPUT) # Please put this first

    # The start date and end date will be represented in the form of YYYY-MM-DD
    start_date = '2020-03-14'
    end_date = '2020-09-05'
    
    file_path = 'data.json'
    
    # Function testing, uncomment to test
    # Q1_1(file_path, start_date, end_date)
    # Q1_2(file_path, start_date, end_date)
    # Q1_3(file_path, start_date, end_date)
    # Q1_4(file_path, start_date, end_date)
    # Q1_5(file_path, start_date, end_date)
    # Q1_6(file_path, start_date, end_date)
    # Q1_7(file_path, start_date, end_date)
    Q2_1(file_path, start_date, end_date)
    # Q2_2(file_path, start_date, end_date)
    # Q2_3(file_path, start_date, end_date)
    # Q3(file_path, start_date, end_date)