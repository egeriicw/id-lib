import pandas as pd
import os
import matplotlib as mpl
import numpy as np
import scipy.stats.mstats as mstats
import datetime as dt

def idProcess(filename):

    # Set column names for interval data from Dominion
    cnames = ["Date","12:00 AM","12:30 AM", "1:00 AM","1:30 AM","2:00 AM","2:30 AM","3:00 AM","3:30 AM","4:00 AM","4:30 AM","5:00 AM","5:30 AM","6:00 AM","6:30 AM","7:00 AM","7:30 AM","8:00 AM","8:30 AM","9:00 AM","9:30 AM","10:00 AM","10:30 AM","11:00 AM","11:30 AM","12:00 PM","12:30 PM","1:00 PM","1:30 PM","2:00 PM","2:30 PM","3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM","5:30 PM","6:00 PM","6:30 PM","7:00 PM","7:30 PM","8:00 PM","8:30 PM","9:00 PM","9:30 PM","10:00 PM","10:30 PM","11:00 PM","11:30 PM"]

    # Import data

    parse_dates = [0]

    df = pd.read_csv(filename, sep=',', header=None, names=cnames, na_values=['NA'], parse_dates=parse_dates)

    print df


    #Melt data to reorganize into columnar fashion.
    melted = pd.core.reshape.melt(df, id_vars=['Date'])

    print "Melted: ", melted
    
    dates = np.array(melted['Date'])
    times = List(melted['variable'])
    values = np.array(melted['value'])


    print "Dates: ", dates
    print "times: ", type(times[1])
    print "values: ", values

    print "dtype_test: ", values.dtype
  
    datetimes_s = np.datetime64(dates + " " + times)
    
    
    drange = np.arange(0, len(datetimes_s), 1)

    data1 = np.array([drange, datetimes_s])
    data2 = np.array([drange, values])

    dataset1 = pd.DataFrame(data1.T, columns=['index', 'datetime']) 
    dataset2 = pd.DataFrame(data2.T, columns=['index', 'values'])

    dataset_m = pd.merge(dataset1, dataset2, how='left', on='index', right_index=False)
    
    melted.to_csv('../data/output/output.csv')


    return dataset_m

"""
def plot(x, y)
    mpl.plot(x,y, 'o')
    mpl.show()	
"""

def main():
    print "Success"
    filename = "../data/input/ckid.csv"
    dataset_r = idProcess(filename)
    dataset_r.to_csv('../data/output/returntest.csv')


    """
    dataset_copy = dataset_r.copy(deep=True)
    """
    dataset_r['values'] = dataset_r['values'].fillna(0)    
    dataset_argsort = dataset_r['values'].apply(np.argsort, axis=0)

    print "...sorted..."
    dataset_r.to_csv('../data/output/outtest.csv')
    #print "...complete..."
    dataset_rank = dataset_r.rank(axis=0, method='max', ascending=True)
    print dataset_rank['values']
    dataset_rank.to_csv('../data/output/ranktest.csv')

if __name__=="__main__":
    main()
