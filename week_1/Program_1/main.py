"""
    Name: Arterio Rodrigues
    Email: arterio.rodrigues47@myhunter.cuny.edu
    Resources:  python3.8 documents 
"""

def make_dictionary(data, kind = "min"):
    """
    Creating a dictionary with a key of the remote unit ID + turnstile unit number.
    Depending on kind, the resulting dictionary will store the minimum entry
    number seen (as an integer), the maximum entry number seen (as an integer),
    or the station name (as a string).
    Returns the resulting dictionary.

    Keyword arguments:
    type -- type of dictionary to be created:  min, max, station
    """

    #Placeholder-- replace with your code
    new_dict = {}
    if(kind == "station"):
        for line in data:
            line = line.strip()
            line = line.split(',')

            new_dict[line[1]+','+line[2]] = line[3]
        return new_dict

    data_dict = {}

    for line in data:
        line = line.strip()
        line = line.split(',')
        
        data_dict[line[1]+','+line[2]] = []
        new_dict[line[1]+','+line[2]] = 0

    for line in data: 
        line = line.strip()
        line = line.split(',')

        data_dict[line[1]+','+line[2]].append(line[9])

    for element in data_dict:
        entries_arr = data_dict[element]

        if(kind == "min"):
            value = int(entries_arr[0])
        else:
            value = 0
        #print(element, entries_arr[:5] , entries_arr[-5:], end ='')

        for i in range(1, len(entries_arr)): 
            if(kind == "min"):
                if( value > (int(entries_arr[i]) - int(entries_arr[i-1]))):
                    value = int(entries_arr[i]) - int(entries_arr[i-1])
            else:
                 if( value < (int(entries_arr[i]) - int(entries_arr[i-1]))):
                    value = int(entries_arr[i]) - int(entries_arr[i-1])
        new_dict[element] = value
        #print(" *****", value)
   
       

    return new_dict

def get_turnstiles(station_dict, stations = None):
    """
    If stations is None, returns the names of all the turnstiles stored as keys
    in the inputted dictionary.
    If non-null, returns the keys which have value from station in the inputed dictionary.
    Returns a list.

    Keyword arguments:
    stations -- None or list of station names.   
    """

    #Placeholder-- replace with your code
    lst = []
    if(stations == None):
        for element in station_dict:
            lst.append(element)
    else:
        for element in station_dict:
            for station in stations:
                if station_dict[element] == station:
                    lst.append(element)
    return lst

def compute_ridership(min_dict,max_dict,turnstiles = None):
    """
    Takes as input two dictionaries and a list, possibly empty, of turnstiles.
    If no value is passed for turnstile, the default value of None is used
    (that is, the total ridership for every station in the dictionaries).
    Returns the ridership (the difference between the minimum and maximum values)
    across all turnstiles specified.

    Keyword arguments:
    turnstiles -- None or list of turnstile names    
    """

    #Placeholder-- replace with your code
    total = 0
    if(turnstiles == None):
        for i in range(len(min_dict)):
            total += max_dict[i] - min_dict[i]
    else:
        for turnstile in turnstiles: 
            total += max_dict[turnstile]-min_dict[turnstile]

    return total

def main():
    """
    Opens a data file and computes ridership, using functions above.
    """
    file_name = './datasets/turnstile_220611.txt'
    #Store the file contents in data:
    with open(file_name,encoding='UTF-8') as file_d:
        lines = file_d.readlines()
    #Discard first line with headers:
    data = lines[1:]

    #Set up the three dictionaries:
    min_dict = make_dictionary(data, kind = "min")
    max_dict = make_dictionary(data, kind = "max")
    station_dict = make_dictionary(data, kind = "station")
    
    #Print out the station names, alphabetically, without duplicates:
    print(f'All stations: {sorted(list(set(station_dict.values())))}')

    #All the turnstiles from the data:
    print(f'All turnstiles: {get_turnstiles(station_dict)}')
    #Only those for Hunter & Roosevelt Island stations:
    print(get_turnstiles(station_dict, stations = ['68ST-HUNTER CO','ROOSEVELT ISLND']))
    
    #Checking the ridership for a single turnstile
    ridership = compute_ridership(min_dict,max_dict,turnstiles=["R051,02-00-00"])
    print(f'Ridership for turnstile, R051,02-00-00:  {ridership}.')

    #Checking the ridership for a station
    hunter_turns = get_turnstiles(station_dict, stations = ['68ST-HUNTER CO'])
    ridership = compute_ridership(min_dict,max_dict,turnstiles=hunter_turns)
    print(f'Ridership for Hunter College: {ridership}.')

if __name__ == "__main__":
    main()

#194015   R527,R122,00-05-00,90 ST-ELMHURST,7,IRT,06/04/2022,00:00:00,REGULAR,1188687309,1639063620 
#194056   R527,R122,00-05-00,90 ST-ELMHURST,7,IRT,06/10/2022,20:00:00,REGULAR,1188679966,1639060777  