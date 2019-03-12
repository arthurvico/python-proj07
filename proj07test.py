import pylab   # needed for plotting

STATUS = ['Approved','Denied','Settled'] 

def open_file():
    '''This function will be used to open a given file and make sure that it is a valid file'''
    #Create a try and except error
    while True:
        #While this is true, we can open the file
        try:
            #try to open the file here
            file_name = input("Enter a file name: ")
            file_open = open(file_name, "r")
            #We return the opened file
            return file_open
        #If this is false, We return an error and promt for a new file
        except:
            #if error, try again
            print("Error. Please try again.")

def read_file(fp):
    '''This function will take in a file, analyse it and return a list of organized data'''
    header = fp.readline()
    final_list = []
    for line in fp:
        new_money1 = ""
        new_money2 = ""
        data_list = []
        line_list = line.split(",")
        if line_list[1] == "":
            continue
        if line_list[4] == "":
            continue
        if line_list[9] == "":
            continue
        if line_list[10] == "":
            continue
        if line_list[11] == "":
            continue
        money_value = line_list[9]
        for ch in money_value:
            money_value = money_value.replace(";","")
        a = len(money_value)
        money_value = money_value[1:a]
        line_list[9] = money_value
        money_value = line_list[11]
        for ch in money_value:
            money_value = money_value.replace(";","")
        a = len(money_value)
        money_value = money_value[1:a]
        line_list[11] = money_value
        data_list.append(str(line_list[1].strip()))
        data_list.append(str(line_list[4].strip()))
        data_list.append(float(line_list[9]))
        data_list.append(str(line_list[10].strip()))
        data_list.append(float(line_list[11]))
        data_tuple = tuple(data_list)
        final_list.append(data_tuple)
    return final_list
        
        

def process(data):
    '''This function will take in a list of tuples of different data. 
    It will analyze the data and return averages and maximums of the different information'''
    total_claims = 0
    total_closeout = 0
    max_claim = 0
    year_total_claims = 0
    approved_claims = 0
    denied_claims = 0
    i = 0
    final_list=[]
    list1 = [0,0,0,0,0,0,0,0]
    list2 = [0,0,0,0,0,0,0,0]
    list3 = [0,0,0,0,0,0,0,0]
    for item in data:
        if item[3] == 'Approved' or item[3] == 'Settled' or item[3] == 'Denied':
            total_claims += 1
        if item[3] == 'Approved' or item[3] == 'Settled':
            total_closeout += item[4]
            i += 1
        avg_closeout = total_closeout/i
        if item[2] > max_claim:
            max_claim = item[2]
            airport_max = item[1]
        a = len(item[0])
        date = item[0]
        year = date[a-2:a]
        year = int(year)
        index_list = year-2
        if item[3] == 'Approved' or item[3] == 'Settled' or item[3] == 'Denied':
            list1[index_list] += 1
        if item[3] == 'Approved' or item[3] == 'Settled':
            list2[index_list] += 1
        if item[3] == 'Denied':
            list3[index_list] += 1
    final_list.append(list1)
    final_list.append(list2)
    final_list.append(list3)
    final_list.append(total_claims)
    final_list.append(avg_closeout)
    final_list.append(max_claim)
    final_list.append(airport_max)
    final_tuple = tuple(final_list)
    print(final_tuple)
    return final_tuple
    
            
        
            
            
        
    
    

def display_data(tup):
    '''Docstring goes here.'''
    print("TSA Claims Data: 2002 - 2009")
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format(" ",'2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'))
    
def plot_data(accepted_data, settled_data, denied_data):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(8)   # create 8 items to hold the data for graphing
    # assign each list's values to the 8 items to be graphed, include a color and a label
    pylab.bar(X, accepted_data, color = 'b', width = 0.25, label="total")
    pylab.bar(X + 0.25, settled_data, color = 'g', width = 0.25, label="settled")
    pylab.bar(X + 0.50, denied_data, color = 'r', width = 0.25,label="denied")

    # label the y axis
    pylab.ylabel('Number of cases')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2002","2003","2004","2005","2006","2007","2008","2009"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    # pylab.savefig("plot.png")
    
def main():
    '''Docstring goes here.'''
    fp = open_file()
    data = read_file(fp)
    process(data)
if __name__ == "__main__":
    main()