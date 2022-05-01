# Read the CSV file in python using this code:
import csv

def test_raag_data(raag):
  pass

def read_raag_data():
    # Read the CSV file in python using this code:
    filename = 'ragadata.csv'
    #create handle to open file in memory
    csvfile = open(filename, 'r')
    # create a reader that reads file as a dictionary
    dict_handle = csv.DictReader(csvfile)
    raag = dict()
    # look through the values in the reader and print:
    for d in dict_handle:
      	assert(len(d.keys())==4)
        raag[d['name']] = d
    return raag