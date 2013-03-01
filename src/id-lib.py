import pandas as pd
import os
import matplotlib as mpl
import numpy as np


from datetime import datetime

def idProcess(filename):

    # Set column names for interval data from Dominion
    cnames = ["Date","12:00 AM","12:30 AM", "1:00 AM","1:30 AM","2:00 AM","2:30 AM","3:00 AM","3:30 AM","4:00 AM","4:30 AM","5:00 AM","5:30 AM","6:00 AM","6:30 AM","7:00 AM","7:30 AM","8:00 AM","8:30 AM","9:00 AM","9:30 AM","10:00 AM","10:30 AM","11:00 AM","11:30 AM","12:00 PM","12:30 PM","1:00 PM","1:30 PM","2:00 PM","2:30 PM","3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM","5:30 PM","6:00 PM","6:30 PM","7:00 PM","7:30 PM","8:00 PM","8:30 PM","9:00 PM","9:30 PM","10:00 PM","10:30 PM","11:00 PM","11:30 PM"]

    # Import data

    df = pd.read_csv(filename, sep=',', header=None, names=cnames, na_values=['NA'], parse_dates=[1])

    #Melt data to reorganize into columnar fashion.
    melted = pd.core.reshape.melt(df, id_vars=['Date'])

    dates = np.array(melted['Date'])
    times = np.array(melted['variable'])
    values = np.array(melted['value'])
  
    datetimes_s = np.datetime64(dates + " " + times)
    drange = np.arange(0, len(datetimes_s), 1)
    

    data1 = np.array([drange, datetimes_s])
    data2 = np.array([drange, values])

    dataset1 = pd.DataFrame(data1.T, columns=['index', 'datetime']) 
    dataset2 = pd.DataFrame(data2.T, columns=['index', 'values'])

    

    print "dataset1 index: ", dataset1.index
    print "dataset2 index: ", dataset2.index
    
    

    dataset_c = pd.merge(dataset1, dataset2, how='left', on='index', left_index=False, suffixes=['_1', '_2']	)
    print "dataset_c: ", dataset_c

    print "dataset_c index: ", dataset_c.index

    melted.to_csv('../data/output/output.csv')
    dataset_c.to_csv('../data/output/test.csv')


"""
def plot(x, y)
    mpl.plot(x,y, 'o')
    mpl.show()	
"""

def main():
    print "Success"
    filename = "../data/input/ckid.csv"
    idProcess(filename)

if __name__=="__main__":
    main()
