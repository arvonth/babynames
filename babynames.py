import csv
import matplotlib.pyplot as plt

#index references for a name entry
name_index = 0  #index of the name in the 'name' variable
pop_index = 2  #index of the number of occurrences of a name in the 'name' variable
year_index = 3  #index of the year in the 'name' variable
rank_index = 4  #index of the rank in the 'name' variable

def get_tops(name_file,number,gender):
    """get the most popular baby names for
    a year given a file of baby names, gender,
    and the number of names to return.
    This function assumes the baby names are listed in order
    of popularity"""
    tops = []
    num = 0
    f = open(name_file)
    reader = csv.reader(f)
    for row in reader:
        if row.__contains__(gender.upper()):
            row[2] = int(row[2])
            tops.append(row)
            num = num + 1
        if num == number:
            break
    return tops

def read_all_names(start,end,gender,datadir):
    """read all of the names into list and add the year into
    the list created for each entry
    >>> name_dict = read_all_names(1880,2012,'m','names')
    >>> name_dict['Zyden']['intro_year_pop'] #1
    7
    >>> name_dict = read_all_names(1990,2012,'m','names')
    >>> name_dict['Zyden']['pops']['2012'] #2
    5
    """
    names = []
    name_dict = {}

    for year in range(start,end+1):
        year_names = []
        year = str(year)
        try:
            path = r"{0}/yob{1}.txt".format(datadir,year)
            f = open(path)
            reader = csv.reader(f)
            rank = 1
            for name in reader:
                if name[1].upper() == gender.upper():
                    #first time name appears
                    if name[0] not in name_dict:
                        name_dict[name[0]] = {}
                        name_dict[name[0]].update({'gender':gender.upper()})
                        name_dict[name[0]].update({'intro_year_pop':int(name[pop_index])})
                        name_dict[name[0]].update({'intro_year':year})
                        name_dict[name[0]].update({'intro_year_rank':rank})
                        name_dict[name[0]].update({'pops':{year:int(name[pop_index])}})
                        name_dict[name[0]].update({'ranks':{year:rank}})
                    #every time the name appears
                    name_dict[name[0]]['pops'].update({year:int(name[pop_index])})
                    name_dict[name[0]]['ranks'].update({year:rank})
                    rank = rank + 1
                    year_names.append(name[name_index])
            names.extend(year_names)
            f.close()
        except IOError:
        	print("{0} not found".format(path))
    return name_dict


def graph_name(name_object,name):
    name_pops = name_object['pops'].items()
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    #ax2 = fig.add_subplot(2, 1, 2)
    title_string = 'Number of '+name+"'s"
    plt.title(title_string)
    plt.xlabel('Year')
    ax1.get_xaxis().get_major_formatter().set_useOffset(False)
    #ax1.plot(*zip(*name_pops),marker='x')
    ax1.bar(*zip(*name_pops),align='center')
    plt.show()

def name_totals(name_object,name):
    """print out the total number of a given name"""
    total_names = {}
    total_names[name] = sum(name_object['pops'].values())
    return total_names

if __name__ == "__main__":
    import doctest
    doctest.testmod()
