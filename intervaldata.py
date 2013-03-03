import csv
import datetime as dt

class IntervalData:

    def __init__(self, filename):
        self.filename = filename
        self.idata = []
        self.fdata = []
        self.mDim = 0
        self.nDim = 0
        self.cnames = ["Date","12:00 AM","12:30 AM", "1:00 AM","1:30 AM","2:00 AM","2:30 AM","3:00 AM","3:30 AM","4:00 AM","4:30 AM","5:00 AM","5:30 AM","6:00 AM","6:30 AM","7:00 AM","7:30 AM","8:00 AM","8:30 AM","9:00 AM","9:30 AM","10:00 AM","10:30 AM","11:00 AM","11:30 AM","12:00 PM","12:30 PM","1:00 PM","1:30 PM","2:00 PM","2:30 PM","3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM","5:30 PM","6:00 PM","6:30 PM","7:00 PM","7:30 PM","8:00 PM","8:30 PM","9:00 PM","9:30 PM","10:00 PM","10:30 PM","11:00 PM","11:30 PM"]
 
        
    def getIntervalData(self):
        return self.fdata

    def read_csv(self):
        print "read_csv"
        with open(self.filename, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                self.idata.append(list(row))
        self.idata = map(list, zip(*self.idata))
        self.mDim = len(self.idata)
        self.nDim = len(self.idata[1])
    
    def write_csv(self):
        with open( "../data/output/testoutput.csv", 'wb') as f:
            writer = csv.writer(f, delimiter=',', dialect='excel')
            for row in self.fdata:
                writer.writerow(row)
        f.close()

    def print_csv(self):
        print "print_csv"
        
    def printParameters(self):
        print "Columns: ", self.mDim
        print "Rows: ", self.nDim
        
    def melt(self):
        transposed = zip(*self.idata)
        
        for trans in range(0, len(transposed)):
            temp = transposed[trans]
            for t in range(1, len(self.cnames)):
                datetime_str = temp[0] + " " + self.cnames[t]
                datetimes = dt.datetime.strptime(datetime_str, "%m/%d/%Y %H:%M %p")
                self.fdata.append([datetimes, temp[t]])

def main():
    filename = "../data/input/ckid.csv"
    d = IntervalData(filename)
    d.read_csv()
    d.melt()
    d.write_csv()
    

if __name__ == "__main__":
    print "...Start..."
    main()
