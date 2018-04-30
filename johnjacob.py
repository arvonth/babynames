import matplotlib.pyplot as plt
import babynames as bn

def JohnJacob(names_dict):
    """John was the most popular boy's name in the US for a long time.
    Jacob and Mason have become popular recently"""
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

if __name__ == "__main__":
    names_dict,most_pop,top_names = bn.read_all_names(1880,2016,'m','names')
    JohnJacob(names_dict)
