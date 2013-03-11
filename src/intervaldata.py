#! /usr/bin/env python

import csv
import datetime as dt
import json

class IntervalData:
    #
    #
    #
    #

    filename = ""
    idata = list()
    fdataList = list()
    fdataDict = dict()
    dataframedata = ""
    mDim = ""
    nDim = ""
    cnames = ""
    shape = ""
    headerset = False
    headerrow = list()


    def __init__(self, filename=None):
        #
        #
        #
        #
        
        print "__Init__"
        self.idata = list()
        self.fdataList = list()
        self.fdataDict = dict()
        self.headerrow = list()
        self.headerset = False
        self.filename = filename
        

    def setFilename(self, filename):
        self.filename = filename


    def read_CSV(self, filename=None, header=None):

        #
        #
        #
        #

        print "read_CSV"

        if filename != None or self.filename != None:

            # What happens if both filenames are different
            # self.filename takes precedence

            location = filename or self.filename
            print "Location: ", location

            try:
                print "trying"
                with open(location, 'rb') as infile:
                    print "File: ", self.filename, " Open."
                    if header == None:
                        for line in infile:
                                self.idata.append(line.strip('\r\n').split(','))
                    else:
                        for line in infile:
                            if self.headerset == False:
                                self.headerrow = line.strip('\r\n').split(',')
                                self.headerset = True
                            else:
                                self.idata.append(line.strip('\r\n').split(','))

            except IOError as e:
                print "IOException: ", e
            finally:
                infile.close()
        else:
            print "Requires a filename."


    def melt(self):
        print "...Melt..."

        #
        #
        #
        #
        
        for i in range(0,len(self.idata)):
            for j in range(1, len(self.idata[i])):
            
               # Create List Representation
                datetime_str = self.idata[i][0] + " " + self.headerrow[j]
                datetimes = dt.datetime.strptime(datetime_str, "%m/%d/%Y %I:%M %p")
                self.fdataList.append([datetimes, self.idata[i][j]])

                # Create Dict Representation
                self.fdataDict.setdefault(self.idata[i][0], {})
                self.fdataDict[self.idata[i][0]][dt.datetime.strptime(self.headerrow[j], "%I:%M %p").strftime("%H:%M")] = self.idata[i][j] 

        print "Melt Complete."
                
    def write_JSON(self, filename=None):
        #
        #
        #
        #

        print "Writing to JSON."

        if filename != None:
            try:
                with open( "../data/output/" + filename, 'wb') as outfile:
                    outfile.write(json.dumps(self.fdataDict, sort_keys=True, indent=4))
            except IOError as e:
                print "IOException: ", e
            finally:
                outfile.close()
                print "JSON saved to ", filename
        else:
            print "Output JSON file name required."
        
    def write_CSV(self, filename=None):
        #
        #
        #
        #

        print "Writing to CSV."

        if filename != None:
            try:
                with open( "../data/output/" + filename, 'wb') as outfile:
                    writer = csv.writer(outfile, delimiter=',', dialect='excel')
                    for row in self.fdataList:
                        writer.writerow(row)
            except IOError as e:
                print "IOException: ", e
            finally:
                outfile.close()
                print "CSV saved to ", filename

        else:
            print "Output CSV file name required."

    def getDataList(self):
        #
        #
        #
        #

        print "Get Data"
        
##        if type(datatype) == list():
##            print "list"
##            return self.fdataList
##        elif type(datatype) == dict:
##            return self.fdataDict
##        else:
##            return 0

        return self.fdataList

    def getDataDict(self):
        #
        #
        #
        #

        return self.fdataDict

        


##    def createDataFrame(self):
##        print "...Create Data Frame..."
##        self.dataframedata = pd.DataFrame(self.fdata)
##        print "Columns: ", self.dataframedata.columns[0], self.dataframedata.columns[1]
##        self.dataframedata.columns = ["Date", "Value"]
##        print "Columns: ", self.dataframedata.columns[0], self.dataframedata.columns[1]
##        print "Index: ", self.dataframedata.index
##        print "Date: ", self.dataframedata["Date"]
##        print "Values: ", self.dataframedata["Value"]
##
##    def sort(self):
##        print "...Sort..."
##        return 0
##
##    def getShape(self):
##        print "...getShape..."
##        return 0
##    
##    def getFFT(self):
##        # return FFT of interval data
##        return 0
        
def main():
    name = "../data/input/ckid.csv"
    d = IntervalData(name)
    d.read_CSV(name, header=True)
    d.melt()
    d.write_CSV("csvtest.csv")
    d.write_JSON("jsontest.json")
    test = d.getDataList()

    print test[0:10000]

    

if __name__ == "__main__":
    print "...Start..."
    main()
