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
    >>> name_dict,most_pop,top_10 = read_all_names(1880,2012,'m','names')
    >>> name_dict['Zyden']['intro_year_pop'] #1
    7
    >>> most_pop[2003]
    'Jacob'
    >>> most_pop[1937]
    'Robert'
    >>> most_pop[1880]
    'John'
    >>> name_dict,most_pop,top_10 = read_all_names(1990,2012,'m','names')
    >>> name_dict['Zyden']['pops'][2012] #2
    5
    >>> top_10[2009]
    ['Jacob', 'Ethan', 'Michael', 'Alexander', 'William', 'Joshua', 'Daniel', 'Jayden', 'Noah', 'Christopher']
    """
    names = []
    most_pop = {}
    top_names = {}
    name_dict = {}
    top_number = 10

    for year in range(start,end+1):
        year_names = []
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
            #output the most popular name in a dictionary with the year as the key
            most_pop.update({year:year_names[0]})
            top_names_list = []
            for i in range(top_number):
                top_names_list.append(year_names[i])
            top_names.update({year:top_names_list})
            f.close()
        except IOError:
        	print("{0} not found".format(path))
    return name_dict,most_pop,top_names

def JohnJacob(names_dict):
    john_pops = []
    john_ranks = []
    john_years = []
    jacob_pops = []
    jacob_ranks = []
    jacob_years = []
    mason_pops = []
    mason_years = []
    mason_ranks = []
    john_dict = names_dict['John']
    jacob_dict = names_dict['Jacob']
    mason_dict = names_dict['Mason']
    for item in sorted(john_dict['pops'].items()):
        john_years.append(item[0])
        john_pops.append(item[1])
    for item in sorted(john_dict['ranks'].items()):
        john_ranks.append(-1*item[1])

    for item in sorted(jacob_dict['pops'].items()):
        jacob_years.append(item[0])
        jacob_pops.append(item[1])
    for item in sorted(jacob_dict['ranks'].items()):
        jacob_ranks.append(-1*item[1])

    for item in sorted(mason_dict['pops'].items()):
        mason_years.append(item[0])
        mason_pops.append(item[1])
    for item in sorted(mason_dict['ranks'].items()):
        mason_ranks.append(-1*item[1])

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    plt.title('Ranks of John, Jacob and Mason')
    ax2 = fig.add_subplot(2, 1, 2)
    plt.title('Number of Johns, Jacobs and Masons')
    plt.xlabel('Years')
    ax1.plot(john_years,john_ranks,'x',label = 'John');
    ax1.plot(jacob_years,jacob_ranks,'^',label = 'Jacob');
    ax1.plot(mason_years,mason_ranks,'o',label = 'Mason');
    ax1.legend(loc='lower right')
    ax2.plot(john_years,john_pops,'x',label = 'John');
    ax2.plot(jacob_years,jacob_pops,'^',label = 'Jacob');
    ax2.plot(mason_years,mason_pops,'o',label = 'Mason');
    ax2.legend()
    plt.show()

def MarySophia(names_dict):
    john_pops = []
    john_ranks = []
    john_years = []
    jacob_pops = []
    jacob_ranks = []
    jacob_years = []
    mason_pops = []
    mason_years = []
    mason_ranks = []
    john_dict = names_dict['Mary']
    jacob_dict = names_dict['Sophia']
    mason_dict = names_dict['Emma']
    for item in sorted(john_dict['pops'].items()):
        john_years.append(item[0])
        john_pops.append(item[1])
    for item in sorted(john_dict['ranks'].items()):
        john_ranks.append(-1*item[1])

    for item in sorted(jacob_dict['pops'].items()):
        jacob_years.append(item[0])
        jacob_pops.append(item[1])
    for item in sorted(jacob_dict['ranks'].items()):
        jacob_ranks.append(-1*item[1])

    for item in sorted(mason_dict['pops'].items()):
        mason_years.append(item[0])
        mason_pops.append(item[1])
    for item in sorted(mason_dict['ranks'].items()):
        mason_ranks.append(-1*item[1])

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    plt.title('Ranks of Mary, Sophia and Emma')
    ax2 = fig.add_subplot(2, 1, 2)
    plt.title('Number of Marys, Sophia and Emmas')
    plt.xlabel('Years')
    ax1.plot(john_years,john_ranks,'x',label = 'Mary');
    ax1.plot(jacob_years,jacob_ranks,'^',label = 'Sophia');
    ax1.plot(mason_years,mason_ranks,'o',label = 'Mason');
    ax1.legend(loc='lower right')
    ax2.plot(john_years,john_pops,'x',label = 'Mary');
    ax2.plot(jacob_years,jacob_pops,'^',label = 'Sophia');
    ax2.plot(mason_years,mason_pops,'o',label = 'Emma');
    ax2.legend()
    plt.show()

def graph_name(name_object,name):
    years = []
    pops = []
    for item in sorted(name_object['pops'].items()):
        years.append(item[0])
        pops.append(item[1])
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    title_string = 'Number of '+name+"'s"
    plt.title(title_string)
    plt.xlabel('Year')
    ax1.get_xaxis().get_major_formatter().set_useOffset(False)
    #ax1.plot(years,pops,'x')
    ax1.bar(years,pops,align='center')
    plt.show()

def name_totals(name_object,name):
    """print out the total number of a given name"""
    total_names = {}
    total_names[name] = sum(name_object['pops'].values())
    return total_names

if __name__ == "__main__":
    import doctest
    doctest.testmod()
