import sys
import os
import numpy as np

def loadDataFromFile(filename, delimiter='\t'):
    return np.genfromtxt(filename, delimiter='\t')

def collatePoints(array):
    data = {} #empty dictionary

    for row in array:
        x, y = row #unpack the row into x and y values
        if x in data:
            # We've already seen data at this X, so append the y value to our list of seen y values at this X
            data[x].append(y)
        else:
            # We haven't seen data at this X yet, so add the y value in a new list (so we can add more later, if needed)
            data[x] = [y]
    return data

def averagePoints(point_dict):
    averages = []
    for x, values in point_dict.items():
        y = np.average(values)
        averages.append([x,y])
    return np.array(averages)

def main():
    inputfilename = sys.argv[1]
    outputfilename = inputfilename + ".out.txt"
    arr = loadDataFromFile(inputfilename)

#trim the third column
    arr = arr[:,0:2]

    collated = collatePoints(arr)

    averages = averagePoints(collated)

    try:
        os.remove(outputfilename)
    except FileNotFoundError:
        pass
    with open(outputfilename, 'w') as output:
        output.write(inputfilename + "\n")
        for x, y in averages:
            output.write("{},{}\n".format(x,y))

    return 0

if __name__ == '__main__':
    sys.exit(main())
